from fastapi.security import OAuth2PasswordBearer
from os import getenv

SECRET_KEY = getenv("SECRET_KEY", "")
ALGORITHM = getenv("ACCES_TOKEN_ALGORITHM", "HS256")
EXPIRE_MINUTES = int(getenv("ACCES_TOKEN_EXPIRE_MINUTES", 10))
OAUTH2_SCHEME = OAuth2PasswordBearer(tokenUrl="token")
