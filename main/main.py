import logging

import uvicorn
from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

from api.v1 import suppliers
from core.config import settings
from core.logger import LOGGING

app = FastAPI(
    # Конфигурируем название проекта. Оно будет отображаться в документации
    title=settings.project_name,
    # Адрес документации в красивом интерфейсе
    docs_url='/api/openapi',
    # Адрес документации в формате OpenAPI
    openapi_url='/api/openapi.json',
    # Можно сразу сделать небольшую оптимизацию сервиса
    # и заменить стандартный JSON-сереализатор на более шуструю версию, написанную на Rust
    default_response_class=ORJSONResponse,
)

app.include_router(suppliers.router, prefix='/suppliers', tags=['Suppliers'])

if __name__ == '__main__':
    uvicorn.run(
        'main:app',
        host=settings.main_host,
        port=settings.main_port,
        log_config=LOGGING,
        log_level=logging.DEBUG
    )
