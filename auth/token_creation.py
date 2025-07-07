from .token_variables import SECRET_KEY, ALGORITHM, EXPIRE_MINUTES
from .token_model import JWTToken
from datetime import datetime, timedelta
from pytz import timezone
from jose import jwt


def create_access_token(data: JWTToken, delta: float = EXPIRE_MINUTES) -> str:

    expire = datetime.now(timezone("America/Sao_Paulo")) + (timedelta(minutes=delta))
    data.expire = expire
    return jwt.encode(data.__dict__, SECRET_KEY, algorithm=ALGORITHM)
