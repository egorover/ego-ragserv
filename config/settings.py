"""
Configuration module for RAG Vector Demo project.
Loads environment variables and provides centralized settings.

Environment Variables:
    OPENAI_API_KEY: OpenAI API key for embedding generation
    EMBEDDING_MODEL: OpenAI embedding model (default: text-embedding-3-large)
    EMBEDDING_DIMENSION: Dimension of embedding vectors (default: 3072)
    PINECONE_API_KEY: Pinecone API key
    PINECONE_ENVIRONMENT: Pinecone environment/region
    PINECONE_INDEX_NAME: Pinecone index name
    WEAVIATE_URL: Weaviate instance URL
    WEAVIATE_API_KEY: Weaviate API key (optional for local)
    RELEVANCE_PROJECT: Relevance AI project ID
    RELEVANCE_API_KEY: Relevance AI API key
    RELEVANCE_DATASET_ID: Relevance AI dataset ID
    PROXYAPI_API_KEY: ProxyAPI API key (optional)
    PROXYAPI_BASE_URL: ProxyAPI base URL (optional)
    PROXYAPI_ENABLED: Enable ProxyAPI routing (default: false)
"""

import os
from typing import Optional
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


class Settings:
    """Centralized configuration settings for the RAG application."""
    
    # OpenAI Configuration
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY", "")
    EMBEDDING_MODEL: str = os.getenv("EMBEDDING_MODEL", "text-embedding-3-large")
    EMBEDDING_DIMENSION: int = int(os.getenv("EMBEDDING_DIMENSION", "3072"))
    
    # Pinecone Configuration
    PINECONE_API_KEY: str = os.getenv("PINECONE_API_KEY", "")
    PINECONE_ENVIRONMENT: str = os.getenv("PINECONE_ENVIRONMENT", "")
    PINECONE_INDEX_NAME: str = os.getenv("PINECONE_INDEX_NAME", "rag-demo-index")
    
    # Weaviate Configuration
    WEAVIATE_URL: str = os.getenv("WEAVIATE_URL", "http://localhost:8080")
    WEAVIATE_API_KEY: Optional[str] = os.getenv("WEAVIATE_API_KEY")
    WEAVIATE_CLASS_NAME: str = "RAGDocument"
    
    # Relevance AI Configuration
    RELEVANCE_PROJECT: str = os.getenv("RELEVANCE_PROJECT", "")
    RELEVANCE_API_KEY: str = os.getenv("RELEVANCE_API_KEY", "")
    RELEVANCE_DATASET_ID: str = os.getenv("RELEVANCE_DATASET_ID", "rag-demo-dataset")
    
    # ProxyAPI Configuration
    PROXYAPI_API_KEY: str = os.getenv("PROXYAPI_API_KEY", "")
    PROXYAPI_BASE_URL: str = os.getenv("PROXYAPI_BASE_URL", "")
    PROXYAPI_ENABLED: bool = os.getenv("PROXYAPI_ENABLED", "false").lower() == "true"
    
    @classmethod
    def validate(cls) -> bool:
        """
        Validate that all required configuration values are present.
        
        Returns:
            bool: True if all required settings are present, False otherwise.
        """
        required_fields = {
            "OPENAI_API_KEY": cls.OPENAI_API_KEY,
            "PINECONE_API_KEY": cls.PINECONE_API_KEY,
            "PINECONE_ENVIRONMENT": cls.PINECONE_ENVIRONMENT,
            "WEAVIATE_URL": cls.WEAVIATE_URL,
            "RELEVANCE_PROJECT": cls.RELEVANCE_PROJECT,
            "RELEVANCE_API_KEY": cls.RELEVANCE_API_KEY,
        }
        
        # ProxyAPI is optional, only validate if enabled
        if cls.PROXYAPI_ENABLED and not cls.PROXYAPI_API_KEY:
            print("⚠️  ProxyAPI is enabled but PROXYAPI_API_KEY is not set")
            return False
        
        missing_fields = [
            field for field, value in required_fields.items() 
            if not value
        ]
        
        if missing_fields:
            print(f"⚠️  Missing required configuration fields: {', '.join(missing_fields)}")
            return False
        
        return True
    
    @classmethod
    def print_config(cls) -> None:
        """Print current configuration (without exposing sensitive data)."""
        print("=" * 60)
        print("RAG Vector Demo - Configuration")
        print("=" * 60)
        print(f"OpenAI Model: {cls.EMBEDDING_MODEL}")
        print(f"Embedding Dimension: {cls.EMBEDDING_DIMENSION}")
        print(f"Pinecone Index: {cls.PINECONE_INDEX_NAME}")
        print(f"Weaviate URL: {cls.WEAVIATE_URL}")
        print(f"Weaviate Class: {cls.WEAVIATE_CLASS_NAME}")
        print(f"Relevance Project: {cls.RELEVANCE_PROJECT}")
        print(f"Relevance Dataset: {cls.RELEVANCE_DATASET_ID}")
        print(f"ProxyAPI Enabled: {cls.PROXYAPI_ENABLED}")
        if cls.PROXYAPI_ENABLED:
            print(f"ProxyAPI Base URL: {cls.PROXYAPI_BASE_URL or '(default)'}")
        print("=" * 60)


# Create a singleton instance
settings = Settings()

