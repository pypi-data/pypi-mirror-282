from .config import config

def get_llm():
    from .core import OllamaLLM, OpenAILLM
    
    if config.llm_backend == "ollama":
        return OllamaLLM(config.llm_host, config.llm_model)
    elif config.llm_backend == "openai":
        return OpenAILLM(config.openai_api_key, config.llm_model)
    else:
        raise ValueError(f"Unsupported LLM backend: {config.llm_backend}")