from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "FastAPI Scaffold"
    database_url: str = "sqlite:///./test.db"
    debug: bool = True

    class Config:
        env_file = ".env"


settings = Settings()
