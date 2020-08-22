from fastapi import APIRouter

router = APIRouter()


@router.get("/users/")
async def read_users(name):
    return [{"username": name}, {"username": "Bar"}]
