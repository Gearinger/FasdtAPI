import dbHelper
from fastapi import APIRouter
import uuid

router = APIRouter()


@router.post("/register/")
async def read_item(user_name):
    if not dbHelper.exist_table("USER"):
        dbHelper.logger.error("注册用户时，不存在USER表！")
    key = uuid.uuid1().__str__()
    dbHelper.execute_sql(f"insert into USER (NAME, KEY) values (\'{user_name}\',\'{key[:16]}\')")
    return {"item_id": "item_id"}
