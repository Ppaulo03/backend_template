from contextlib import asynccontextmanager
from core import register_middlewares
from routes import register_routes
from os import getenv
from fastapi import FastAPI


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Initialize resources or connections here if needed
    yield
    # Cleanup resources or connections here if needed


IN_PRODUCTION = getenv("IN_PROD", "false").lower() in ("true", "1", "yes")

app = FastAPI(
    docs_url=None if IN_PRODUCTION else "/docs",
    redoc_url=None if IN_PRODUCTION else "/redoc",
    openapi_url=None if IN_PRODUCTION else "/openapi.json",
    lifespan=lifespan,
)

register_middlewares(app)
register_routes(app)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "application:app",
        host="0.0.0.0",
        port=81,
        reload=True,
    )
