from .token_validation import validate_token
from .token_creation import create_access_token
from .token_model import JWTToken
from fastapi import HTTPException, Request


def get_refresh_token(request: Request) -> JWTToken:
    refresh_token = str(request.cookies.get("refresh_token"))
    if not refresh_token:
        raise HTTPException(status_code=401, detail="Refresh token ausente")

    token = validate_token(refresh_token)
    _validate_refresh(token)
    return {"token": create_access_token(token)}


def _validate_refresh(refresh_token: JWTToken) -> None:
    # Placeholder for any additional validation logic for the refresh token
    pass
