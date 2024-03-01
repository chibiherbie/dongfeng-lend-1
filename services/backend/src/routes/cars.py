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
    return {'cars':
        [
            {"img": "C80", "total": 0},
            {"img": "C100"},
            {"img": "C120"},
            {"img": "C180"},
            {"img": "Z55"},
            {"img": "Z80"},
        ]
    }
