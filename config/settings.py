from pydantic_settings import BaseSettings
from typing import Optional
import os
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    # Application
    APP_NAME: str = "نظام يحيى للمحاسبة"
    APP_VERSION: str = "1.0.0"
    DEBUG: bool = os.getenv("DEBUG", "True").lower() == "true"
    
    # Server
    HOST: str = os.getenv("HOST", "0.0.0.0")
    PORT: int = int(os.getenv("PORT", 8000))
    
    # Database - PostgreSQL
    DB_USER: str = os.getenv("DB_USER", "postgres")
    DB_PASSWORD: str = os.getenv("DB_PASSWORD", "password")
    DB_HOST: str = os.getenv("DB_HOST", "localhost")
    DB_PORT: int = int(os.getenv("DB_PORT", 5432))
    DB_NAME: str = os.getenv("DB_NAME", "yahia_accountant")
    DATABASE_URL: str = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    
    # MongoDB
    MONGO_URL: str = os.getenv("MONGO_URL", "mongodb://localhost:27017")
    MONGO_DB_NAME: str = os.getenv("MONGO_DB_NAME", "yahia_accounting")
    
    # JWT
    SECRET_KEY: str = os.getenv("SECRET_KEY", "your-secret-key-change-in-production")
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    REFRESH_TOKEN_EXPIRE_DAYS: int = 7
    
    # Redis
    REDIS_HOST: str = os.getenv("REDIS_HOST", "localhost")
    REDIS_PORT: int = int(os.getenv("REDIS_PORT", 6379))
    REDIS_DB: int = int(os.getenv("REDIS_DB", 0))
    REDIS_URL: str = f"redis://{REDIS_HOST}:{REDIS_PORT}/{REDIS_DB}"
    
    # Celery
    CELERY_BROKER_URL: str = REDIS_URL
    CELERY_RESULT_BACKEND: str = REDIS_URL
    
    # CORS
    ALLOWED_ORIGINS: list = [
        "http://localhost:3000",
        "http://localhost:5173",
        "http://127.0.0.1:3000",
    ]
    
    # File Upload
    UPLOAD_DIR: str = "uploads"
    MAX_FILE_SIZE: int = 10 * 1024 * 1024  # 10MB
    ALLOWED_FILE_EXTENSIONS: list = ["pdf", "xlsx", "xls", "csv", "jpg", "png"]
    
    # Timezone
    TIMEZONE: str = "Africa/Cairo"  # التوقيت المصري
    
    # Currency
    DEFAULT_CURRENCY: str = "EGP"  # الجنيه المصري
    CURRENCY_SYMBOL: str = "ج.م"
    
    # Tax Settings
    DEFAULT_TAX_RATE: float = 0.14  # 14% ضريبة القيمة المضافة
    INCOME_TAX_RATE: float = 0.20  # 20% ضريبة الدخل
    
    # Email
    SMTP_SERVER: str = os.getenv("SMTP_SERVER", "smtp.gmail.com")
    SMTP_PORT: int = int(os.getenv("SMTP_PORT", 587))
    SMTP_EMAIL: str = os.getenv("SMTP_EMAIL", "")
    SMTP_PASSWORD: str = os.getenv("SMTP_PASSWORD", "")
    
    # Logging
    LOG_LEVEL: str = "INFO"
    LOG_FILE: str = "logs/app.log"
    
    class Config:
        env_file = ".env"
        case_sensitive = True

settings = Settings()