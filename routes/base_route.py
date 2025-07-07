from auth import JWTToken, validate_token
from fastapi import FastAPI, APIRouter, Request, Depends
from typing import List, Callable, Optional, Any
from inspect import signature


class Route:

    def __init__(
        self,
        app: FastAPI,
        prefix: str = "",
        public: bool = False,
        validate_access: Callable = validate_token,
    ) -> None:
        self.router = APIRouter()
        self.public = public
        self.validate_access = validate_access

        self.register_routes()
        app.include_router(self.router, prefix=prefix)

    def register_routes(self) -> None:
        """Método para ser sobrescrito nas rotas específicas."""
        raise NotImplementedError("Método register_routes deve ser implementado.")

    def add_to_router(
        self,
        path: str,
        function: Callable,
        methods: List[str],
        public: Optional[bool] = None,
    ) -> None:

        if not public:
            public = self.public

        self.router.add_api_route(
            path,
            self._wrap(function, public),
            methods=methods,
        )

    def _wrap(self, handler: Callable, public: bool) -> Any:
        """Wrapper para injetar o token manualmente usando Depends."""
        validate = (
            self.validate_access
            if not public
            else lambda: JWTToken(user_id="public", session_id="")
        )

        async def endpoint(request: Request, token: JWTToken = Depends(validate)):
            if await request.body():
                data = await request.json()
            else:
                data = {}

            return await self._call_handler(
                handler,
                request=request,
                **request.path_params,
                **request.query_params,
                **data,
                **token.__dict__,
            )

        return endpoint

    async def _call_handler(self, handler_func: Callable, **available_args) -> Callable:
        sig = signature(handler_func)
        expected_args = sig.parameters.keys()
        filtered_args = {k: v for k, v in available_args.items() if k in expected_args}
        return await handler_func(**filtered_args)
