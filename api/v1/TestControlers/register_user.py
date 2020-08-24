from api.v1.Utility import dbHelper
from fastapi import APIRouter
import uuid
from api.v1.Utility import crypto

router = APIRouter()


@router.post("/register/")
async def read_item(user_name):
    if not dbHelper.exist_table("USER"):
        dbHelper.logger.error("注册用户时，不存在USER表！")

    # 计算私钥和公钥
    rsa_key = crypto.get_rsa_keys()

    conn = dbHelper.db.connect(dbHelper.db_file)
    cur = conn.cursor()
    query = 'insert into USER (NAME, PRIVATEKEY, PUBLICKEY) values (?,?,?)'
    result = cur.execute(query, (user_name, rsa_key.private_pem, rsa_key.public_pem)).fetchall()
    conn.commit()
    cur.close()
    conn.close()

    return rsa_key.public_pem
