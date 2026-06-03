from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from config.settings import settings
from models.database import engine, Base
from datetime import datetime

# Create tables
Base.metadata.create_all(bind=engine)

# Initialize FastAPI app
app = FastAPI(
    title=settings.APP_NAME,
    description="نظام محاسبي متكامل شامل",
    version=settings.APP_VERSION
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Health check endpoints
@app.get("/")
async def root():
    return {
        "message": "مرحباً بك في نظام يحيى للمحاسبة",
        "version": settings.APP_VERSION,
        "status": "running"
    }

@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "timestamp": datetime.now().isoformat()
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host=settings.HOST, port=settings.PORT)