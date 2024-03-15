import asyncio
import logging

from django.apps import AppConfig
from elasticsearch import NotFoundError

from suppliers.es.elastic_provider import ElasticProvider
from suppliers.es.schemas.supplier import SUPPLIER_INDEX_SCHEMA


class SuppliersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'suppliers'

    def ready(self):
        asyncio.run(self.create_index())

    async def create_index(self):
        provider = ElasticProvider()
        async with await provider.get_elastic() as es:
            index_name = 'supplier'
            try:
                await es.indices.get(index=index_name)
                logging.warning(f"Index '{index_name}' already exists")
            except NotFoundError:
                await es.indices.create(index=index_name, body=SUPPLIER_INDEX_SCHEMA)
