import json
import os
from datetime import timedelta

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordRequestForm
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig
from tortoise.contrib.fastapi import HTTPNotFoundError
from pydantic import BaseModel  # Импортируем BaseModel


router = APIRouter()

conf = ConnectionConfig(
    MAIL_USERNAME="hyperpe4nka@yandex.ru",
    MAIL_PASSWORD="jrajgfmvgrgqinve",
    MAIL_FROM="hyperpe4nka@yandex.ru",
    MAIL_PORT=465,
    MAIL_SERVER="smtp.yandex.ru",
    MAIL_STARTTLS=True,
    MAIL_SSL_TLS=False,
)


html = """
<p>Привет, тебе пришло письмо от {{ email }} с сообщением:</p>
<p>asdasdasdasd</p>
"""


class EmailData(BaseModel):
    email: str


@router.post(
    "/send_email"
)
async def send_email(email_data: EmailData):
    message = MessageSchema(
        subject="Новое сообщение",
        recipients=['bekkerrdm@gmail.com'],
        body=html,
        subtype="html",
        params={"email": email_data.email}
    )

    try:
        fm = FastMail(conf)
        await fm.send_message(message)
        return {"message": "Письмо успешно отправлено"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Ошибка при отправке письма: {str(e)}")
