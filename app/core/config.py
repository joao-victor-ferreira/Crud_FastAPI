from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "FastAPI Server Base"
    API_VERSION: str = "v1"
    MONGODB_URI: str
    DB_NAME: str  # ✅ adiciona esta linha para aceitar o valor do .env

    class Config:
        env_file = ".env"

settings = Settings()
