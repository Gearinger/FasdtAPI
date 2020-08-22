from fastapi import APIRouter

router = APIRouter()


@router.get("/items/")
async def read_item():
    return {"item_id": "item_id"}
