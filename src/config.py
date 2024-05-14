from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file="src/.env",env_file_encoding = 'utf-8',extra = "allow")
    DATABASE_NAME: str 
    DATABASE_USER: str 
    DATABASE_HOST: str 
    DATABASE_PASSWORD: str 
    MAIL_PASSWORD: str
    SENDER_EMAIL: str