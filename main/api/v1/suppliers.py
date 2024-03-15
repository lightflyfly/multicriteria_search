from fastapi import APIRouter

from api.v1.models.supplier_api_model import Supplier

# Объект router, в котором регистрируем обработчики
router = APIRouter()


@router.get('/{supplier_id}', response_model=Supplier)
async def supplier_details(sup_id: str) -> Supplier:
    return Supplier(id='some_id', title='some_title')
