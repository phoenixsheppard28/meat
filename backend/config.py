from dotenv import load_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field

load_dotenv()


class Config(BaseSettings):
    DATABASE_URL: str = Field(default="NOTHING_HERE_TO_SEE")

    model_config = SettingsConfigDict(env_file=".env.development")


config = Config()


def get_config() -> Config:
    return config
