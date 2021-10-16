# pylint: disable=E0611,E0401
import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from tortoise.contrib.fastapi import register_tortoise
from .routers import auth as auth_router, user, video


app = FastAPI(title="Subme API")

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(auth_router.router)
app.include_router(user.router)
app.include_router(video.router)


@app.get("/")
async def hello():
    return {"message": "Subme Backend service"}


register_tortoise(
    app,
    db_url=os.environ['DB_CONN'],
    modules={"models": ["app.models"]},
    generate_schemas=True,
    add_exception_handlers=True
)
