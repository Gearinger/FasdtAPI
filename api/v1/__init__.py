from fastapi import APIRouter
from .Tools import create_2d_code
from .TestControlers import register_user
from .TestControlers import add_name_password

router = APIRouter()

router.include_router(create_2d_code.router, tags=["tool"], prefix='/tool')
router.include_router(register_user.router, tags=["user"], prefix='/user')
router.include_router(add_name_password.router, tags=["name_pswd"], prefix='/user')
