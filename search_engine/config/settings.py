from pydantic import BaseSettings

class Settings(BaseSettings):
    VECTOR_DB_HOST: str = "vector_db"
    VECTOR_DB_PORT: int = 6333
    MODEL_NAME: str = "openai/clip-vit-base-patch32"
    MAX_RESULTS: int = 20
    
    class Config:
        env_file = ".env"

settings = Settings()
