import uvicorn
from fastapi import FastAPI
from api import v1

app = FastAPI(
    title="GearAPI",
    version="1.0",
)


app.include_router(
    v1.router,
    prefix="/api/v1",
)


if __name__ == '__main__':
    uvicorn.run(app='Main:app', host="127.0.0.1", port=8000, reload=True, debug=True)