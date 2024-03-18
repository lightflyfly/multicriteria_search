import uvicorn
from elasticsearch import AsyncElasticsearch
from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

from api.v1 import suppliers
from core.config import settings
from es import elastic

app = FastAPI(
    title=settings.project_name,
    docs_url='/api/openapi',
    openapi_url='/api/openapi.json',
    default_response_class=ORJSONResponse
)


@app.on_event('startup')
async def startup():
    elastic.es = AsyncElasticsearch(hosts=[f'http://{settings.elastic_host}:{settings.elastic_port}'])


@app.on_event('shutdown')
async def shutdown():
    await elastic.es.close()

app.include_router(suppliers.router, prefix='/api/v1/suppliers', tags=['Suppliers'])

if __name__ == '__main__':
    uvicorn.run(
        'main:app',
        host=settings.main_host,
        port=settings.main_port
    )
