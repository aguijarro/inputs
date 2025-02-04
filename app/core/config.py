# Environment variables and configurations
import logging

from functools import lru_cache
from typing import List
from pydantic_settings import BaseSettings

log = logging.getLogger("uvicorn")


class Settings(BaseSettings):
    PROJECT_NAME: str = "rembg"
    VERSION: str = "1.0.0"
    API_V1_STR: str = "/api/v1"
    DEBUG: bool = False
    FIREBASE_CREDENTIALS_BASE64: str = ""  # Base64 encoded credentials
    ALLOWED_ORIGINS: str = "http://localhost:3000"
    ENVIRONMENT: str = "development"
    
    @property
    def cors_origins(self) -> List[str]:
        return [origin.strip() for origin in self.ALLOWED_ORIGINS.split(",")]
    
    class Config:
        env_file = ".env.development"
        case_sensitive = True

@lru_cache
def get_settings() -> Settings:
    return Settings() 

settings = get_settings() 


