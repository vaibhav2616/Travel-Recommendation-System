import os
from pathlib import Path
from dotenv import load_dotenv

# Load .env file from backend directory if present
BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env")

class Settings:
    PROJECT_NAME: str = "Indian Travel Recommendation System"
    VERSION: str = "1.0.0"
    API_V1_STR: str = "/api"
    GEMINI_API_KEY: str = os.getenv("GEMINI_API_KEY", "")
    DEFAULT_GEMINI_MODEL: str = os.getenv("DEFAULT_GEMINI_MODEL", "gemini-2.5-flash")
    HOST: str = os.getenv("HOST", "0.0.0.0")
    PORT: int = int(os.getenv("PORT", 8000))
    CORS_ORIGINS: list[str] = ["*"]

settings = Settings()

