from .token_variables import SECRET_KEY, ALGORITHM, OAUTH2_SCHEME
from .token_model import JWTToken
from jose import JWTError, jwt
from fastapi import Depends, HTTPException


def validate_token(token: str = Depends(OAUTH2_SCHEME)) -> JWTToken:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return JWTToken(**payload)
    except JWTError as e:
        raise HTTPException(status_code=401, detail="Invalid token") from e
