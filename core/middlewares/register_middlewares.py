from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .exception_logging_middleware import ExceptionLoggingMiddleware
from os import getenv

ALLOW_ORIGINS = getenv("ALLOW_ORIGINS", "https://localhost:5173").split(",")


def register_middlewares(app: FastAPI) -> None:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=ALLOW_ORIGINS,
        allow_credentials=True,
        allow_methods=["GET", "POST", "PUT", "DELETE"],
        allow_headers=["Content-Type", "Authorization", "Accept"],
    )
    app.add_middleware(ExceptionLoggingMiddleware)
