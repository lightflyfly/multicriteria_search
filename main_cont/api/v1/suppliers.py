from http import HTTPStatus

from fastapi import APIRouter
from fastapi.responses import JSONResponse, Response

# Объект router, в котором регистрируем обработчики
router = APIRouter()


@router.get(path='/')
async def suppliers() -> Response:
    return JSONResponse(
            status_code=HTTPStatus.OK,
            content="ok"
        )
