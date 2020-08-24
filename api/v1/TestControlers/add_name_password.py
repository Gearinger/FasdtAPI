from api.v1.Utility import dbHelper
from fastapi import APIRouter
import uuid
from api.v1.Utility import crypto
from api.v1.models.name_password import NamePassword
from datetime import datetime

router = APIRouter()


@router.post("/name_password/")
async def name_passwd(item: NamePassword):
    table_name = 'NAME_PASSWORD'
    if not dbHelper.exist_table(table_name):
        dbHelper.logger.error(f"注册用户时，不存在 {table_name} 表！")

    create_time = datetime.now().isoformat()
    update_time = datetime.now().isoformat()

    conn = dbHelper.db.connect(dbHelper.db_file)
    cur = conn.cursor()
    if not dbHelper.exist_row(table_name, 'TITLE', item.title):
        query = f'insert into {table_name} ' \
                f'(TITLE, NAME, PASSWORD, URL, BZ, CREATETIME, UPDATETIME) values (?,?,?,?,?,?,?)'
        result = cur.execute(query, (item.title, item.name, item.password,
                                     item.url, item.bz, create_time, update_time)).fetchall()
    else:
        sql = f"UPDATE {table_name} SET NAME = ?, PASSWORD = ?, URL = ?, BZ = ?, UPDATETIME = ? WHERE TITLE = ?"
        result = cur.execute(sql, (item.name, item.password, item.url, item.bz, update_time, item.title)).fetchall()

    conn.commit()
    cur.close()
    conn.close()

    return True
