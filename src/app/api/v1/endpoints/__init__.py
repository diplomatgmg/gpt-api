from fastapi import APIRouter

from app.api.v1.endpoints import prompt


__all__ = ["router"]


router = APIRouter()

router.include_router(prompt.router, prefix="/prompt", tags=["prompt"])
