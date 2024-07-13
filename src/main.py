from fastapi import FastAPI

from src.routes.api import router as api_router

app = FastAPI(title="Pilar")

app.include_router(api_router)
