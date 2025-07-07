from fastapi import Request, FastAPI
from fastapi.responses import Response, JSONResponse
from .base_route import Route
from auth import JWTToken


def public() -> JWTToken:
    return JWTToken(user_id="public", session_id="")


class HomeRoute(Route):
    def __init__(self, app: FastAPI) -> None:
        super().__init__(validate_access=public)
        self.add_to_router("/", self.index, methods=["GET"])
        app.include_router(self.router, prefix="")

    async def index(self) -> JSONResponse:

        return JSONResponse(
            content={"message": "Bem-vindo ao backend!"}, status_code=200
        )
