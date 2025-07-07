from pydantic import BaseModel
from datetime import datetime


class JWTToken(BaseModel):
    user_id: str
    session_id: str
    expire: datetime = datetime.now()
