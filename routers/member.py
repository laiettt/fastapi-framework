from fastapi import APIRouter, HTTPException
from model.member.login import LoginRequest
from common.enum import Gender

router = APIRouter(
    prefix="/qa/api",
    tags=["Member"],
)


@router.post(path="/member")
async def login(request: LoginRequest) -> dict:
    if request.gender:
        if request.gender != Gender.Male.value and request.gender != Gender.Female.value:
            raise HTTPException(status_code=422, detail="Unprocessable Entity")
    return {"code": "0000", "message": "success"}
