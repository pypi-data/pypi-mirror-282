import json
from .models import DetectedEntities, EntityType
from .utils import preprocess_response
from typing import Dict, Optional
from abc import ABC, abstractmethod
from .config import get_llm
from .llm_factory import get_llm

class LLMInterface(ABC):
    @abstractmethod
    def generate(self, prompt: str, **kwargs) -> str:
        pass

class OllamaLLM(LLMInterface):
    def __init__(self, host: str, model: str):
        from ollama_instructor.ollama_instructor_client import OllamaInstructorClient
        self.client = OllamaInstructorClient(host=host)
        self.model = model

    def generate(self, prompt: str, **kwargs) -> str:
        response = self.client.chat_completion(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            format="json"
        )
        return response['message']['content']

class OpenAILLM(LLMInterface):
    def __init__(self, api_key: str, model: str):
        import openai
        openai.api_key = api_key
        self.model = model

    def generate(self, prompt: str, **kwargs) -> str:
        import openai
        response = openai.Completion.create(
            engine=self.model,
            prompt=prompt,
            max_tokens=kwargs.get('max_tokens', 100),
            n=1,
            stop=None,
            temperature=kwargs.get('temperature', 0.5),
        )
        return response.choices[0].text.strip()

class DataFog:
    def __init__(self, llm: LLMInterface = None, entity_types: Optional[Dict[str, str]] = None):
        self.llm = llm or get_llm()
        self.entity_types = entity_types or {e.name: e.value for e in EntityType}

    def detect_entities(self, text: str) -> DetectedEntities:
        prompt = f"Identify and classify named entities in the following text: '{text}'"
        response = self.llm.generate(prompt)

        try:
            content = json.loads(response) if isinstance(response, str) else response
            if isinstance(content, dict) and 'entities' in content:
                return DetectedEntities.model_validate(content)
            else:
                preprocessed_response = preprocess_response(content, self.entity_types)
                return DetectedEntities.model_validate(preprocessed_response)
        except Exception as e:
            raise ValueError(f"Error processing response: {e}. Raw response: {response}")


    def add_entity_type(self, name: str, value: str):
        self.entity_types[name.upper()] = value

    def remove_entity_type(self, name: str):
        if name.upper() in self.entity_types:
            del self.entity_types[name.upper()]

    def get_entity_types(self) -> Dict[str, str]:
        return self.entity_types
