from fastapi import FastAPI
from .api.v1.routes import router as v1_api_router


def create_app() -> FastAPI:
    app = FastAPI()
    app.include_router(v1_api_router, prefix='/v1')
    return app