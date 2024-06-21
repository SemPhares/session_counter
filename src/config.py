from pydantic_settings import BaseSettings, SettingsConfigDict

from dotenv import load_dotenv

# Charger les variables d'environnement du fichier .env
load_dotenv("src/.env")


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file="src/.env",env_file_encoding = 'utf-8',extra = "allow")
    DATABASE_NAME : str = model_config.get("DATABASE_NAME") # type: ignore
    DATABASE_USER : str = model_config.get("DATABASE_USER") or ""  # Provide a default value of an empty string if DATABASE_USER is None
    DATABASE_HOST : str = model_config.get("DATABASE_HOST") or ""
    DATABASE_PASSWORD : str = model_config.get("DATABASE_PASSWORD") or ""
    MAIL_PASSWORD : str = model_config.get("MAIL_PASSWORD") or ""
    SENDER_EMAIL : str = model_config.get("SENDER_EMAIL") or ""