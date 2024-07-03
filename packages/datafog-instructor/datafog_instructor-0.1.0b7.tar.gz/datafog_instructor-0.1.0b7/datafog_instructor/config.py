import os
from dotenv import load_dotenv

class Config:
    def __init__(self):
        load_dotenv()  # Load environment variables from .env file
        self.llm_backend = os.getenv("DATAFOG_LLM_BACKEND", "ollama")
        self.llm_host = os.getenv("DATAFOG_LLM_HOST", "http://localhost:11434")
        self.llm_model = os.getenv("DATAFOG_LLM_MODEL", "phi3")
        self.openai_api_key = os.getenv("OPENAI_API_KEY")

config = Config()

