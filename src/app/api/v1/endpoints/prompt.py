from fastapi import APIRouter


__all__ = ["router"]


router = APIRouter()


@router.get("")
async def prompt() -> dict[str, str]:
    return {"result": "ok"}
