from fastapi import FastAPI
from app.api.health import router as health_router

app = FastAPI(
    title = "AI PR Review System",
    description = "AI Powered Pull Request Review & Security Analysis",
    version="1.0.0",
)

app.include_router (health_router)

