from docxtpl import DocxTemplate
from tempfile import NamedTemporaryFile
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse, FileResponse
from fastapi.security import OAuth2PasswordRequestForm
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig
from tortoise.contrib.fastapi import HTTPNotFoundError
from pydantic import BaseModel
from datetime import datetime

router = APIRouter()


class DataGenerate(BaseModel):
    email: str
    phone: str
    position: str
    car: str
    vin: str
    company: str
    name: str


@router.post(
    "/generate"
)
async def generate_docx(data: DataGenerate):
    try:
        required_fields = ['name', 'email', 'phone', 'position', 'car', 'vin', 'company']
        for field in required_fields:
            if not getattr(data, field, None):
                print(f"Ошибка: Поле {field} не заполнено.")
                raise HTTPException(status_code=500, detail=f"Нет поля {field}")

        file_name = f'src/files/{data.car}.docx'
        output_path = await generate(file_name, data)

        return FileResponse(
            output_path,
            media_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document'
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Ошибка при создание файла: {str(e)}")


async def generate(file_name: str, data: DataGenerate) -> str:
    template = DocxTemplate(file_name)

    context = {
        'email': data.email,
        'position': data.position,
        'car': data.car,
        'vin': data.vin,
        'company': data.company,
        'name': data.name,
        'phone': data.phone,
        'date': datetime.today().date()
    }

    template.render(context)

    temp_file = NamedTemporaryFile(delete=False)
    temp_file.close()

    output_path = temp_file.name
    template.save(output_path)

    return output_path
