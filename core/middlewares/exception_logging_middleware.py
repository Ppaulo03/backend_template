from fastapi import Request
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware
from typing import Callable
from loguru import logger


class ExceptionLoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next: Callable) -> JSONResponse:
        middleware_logger = logger.bind(
            method=request.method,
            path=request.url.path,
            client_ip=request.client.host if request.client else "unknown",
        )

        try:
            return await call_next(request)
        except Exception:
            middleware_logger.bind(status_code=500).exception(
                "Erro interno no servidor"
            )
            return JSONResponse(
                status_code=500, content={"detail": "Erro interno no servidor"}
            )
