import base64

from fastapi import APIRouter
import qrcode
from starlette import responses
from api.v1 import Utility
from os import path
from io import BytesIO

router = APIRouter()


@router.get("/code2d_file/")
async def code2d_file(string):
    img = qrcode.make(string)
    img_path = path.join(Utility.static_path, '/static/2d_code.png')
    with open(img_path, "wb") as file:
        img.save(file)
    return responses.FileResponse(img_path, filename='2d_code.png')


@router.get("/code2d/")
async def code2d(string):
    img = qrcode.make(string)
    img_byte = BytesIO()
    img.save(img_byte, format="PNG")  # format: PNG or JPEG
    # write写入的数据，文件指针在末位，如果不重新定义文件指针位置，将无法获取到数据
    # 另，也可以使用BytesIO(b'')在创建实例时便将数据置入，文件指针便在初始位置
    # 将文件指针指向0
    img_byte.seek(0)
    return responses.StreamingResponse(img_byte, media_type="image/png")
