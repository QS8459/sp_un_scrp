from pydantic_settings import BaseSettings;
from pydantic import PostgresDsn;

class Settings(BaseSettings):
    pg_uri: PostgresDsn;
    s_base: str;
    u_base_api: str;

    class Config:
        env_file = ".env";
        env_file_encoding = 'utf-8';

settings = Settings()
