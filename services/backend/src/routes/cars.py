import json
import os
from datetime import timedelta

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordRequestForm

from tortoise.contrib.fastapi import HTTPNotFoundError


router = APIRouter()


@router.get(
    "/cars"
)
async def get_cars():
    with open(os.path.abspath('src/files/cars_data.json'), mode='r') as file:
        analytics_json = json.load(file)

    return analytics_json

