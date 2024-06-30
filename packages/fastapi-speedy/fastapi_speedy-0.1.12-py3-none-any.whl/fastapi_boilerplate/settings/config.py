from functools import lru_cache

from pydantic_settings import BaseSettings


class AppSettings(BaseSettings):
    debug: bool = True
    app_title: str = "FastAPI Boilerplate"
    app_description: str = "FastAPI Boilerplate"
    api_version: str = "v1"
    api_prefix: str = "/v1"


@lru_cache()
def get_app_settings() -> AppSettings:
    return AppSettings()


settings = get_app_settings()
