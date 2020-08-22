import base64

from fastapi import APIRouter
import qrcode
from starlette import responses
from v1 import Utility
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
    return responses.StreamingResponse(img_byte)
