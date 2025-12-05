"""Application configuration settings."""
from functools import lru_cache
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""
    
    # Database
    database_url: str = "postgresql://user:password@localhost:5432/islamic_guidance"
    
    # AI/ML
    embedding_model: str = "all-MiniLM-L6-v2"
    embedding_dimension: int = 384
    
    # Vector Store
    vector_store_persist_dir: str = "./chroma_db"
    
    # API
    api_title: str = "Islamic Guidance API"
    api_version: str = "1.0.0"
    api_description: str = "Semantic search API for Islamic texts"
    
    # CORS
    cors_origins: list[str] = ["*"]
    
    # Search
    default_top_k_per_type: int = 2
    max_results: int = 5
    
    class Config:
        env_file = ".env"
        case_sensitive = False


@lru_cache()
def get_settings() -> Settings:
    """Get cached settings instance."""
    return Settings()
