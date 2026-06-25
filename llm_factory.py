from langchain_cohere import ChatCohere

from config import (
    COHERE_API_KEY,
    LLM_MODEL
)

llm = ChatCohere(
    model=LLM_MODEL,
    cohere_api_key=COHERE_API_KEY,
    temperature=0.2
)