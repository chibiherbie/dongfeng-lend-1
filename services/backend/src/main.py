from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from tortoise import Tortoise  # NEW

from src.database.register import register_tortoise
from src.database.config import TORTOISE_ORM
from src.routes import cars

from routes import integration

# enable schemas to read relationship between models
Tortoise.init_models(["src.database.models"], "models")  # NEW

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

register_tortoise(app, config=TORTOISE_ORM, generate_schemas=False)

app.include_router(cars.router)
app.include_router(integration.router)


@app.get("/")
def home():
    return "Hello, World!"
