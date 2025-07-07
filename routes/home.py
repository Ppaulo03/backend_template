from fastapi import FastAPI, Request
from fastapi.responses import Response, JSONResponse
from .base_route import Route
from auth import JWTToken


def public() -> JWTToken:
    return JWTToken(user_id="public", session_id="")


class HomeRoute(Route):
    def __init__(self, app: FastAPI) -> None:
        super().__init__(app, validate_access=public)

    def register_routes(self) -> None:
        self.add_to_router("/", self.index, methods=["GET"])
        self.add_to_router("/", self.post, methods=["POST"], public=True)

    async def index(self, request: Request) -> JSONResponse:
        print(request.body)
        return JSONResponse(
            content={"message": "Bem-vindo ao backend!"}, status_code=200
        )

    async def post(self, request: Request) -> Response:
        data = await request.form()
        print(data)
        return JSONResponse(content={"message": ""}, status_code=200)
