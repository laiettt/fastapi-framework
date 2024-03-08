from fastapi import Body
from pydantic import BaseModel
from typing import Optional


class LoginRequest(BaseModel):
    account: str = Body(...)
    password: str = Body(...)
    member_id: Optional[int] = None
    gender: Optional[str] = None
