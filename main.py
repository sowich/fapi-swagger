from fastapi import FastAPI
from fastapi.params import Query
from typing import List
from common import SkuSchemes, responses
import yaml

app = FastAPI(
    servers=[
        {"url": "http://localhost:85", "description": "Local environment"},
    ],
)


@app.get(
    path="/api/v2/oz/statistic/brands/categories",
    tags=["analytics"],
    summary="Метод получения статистики категорий по брендам",
    responses=responses
)
async def Func(
        brand: str = Query(example='adidas', description='Бренд'),
        sku_scheme: List[SkuSchemes] = Query(example='FBO', description='SKU-схема', alias='sku_schema[]', default=None),
        start_date=Query(example='2023-03-11', description='Данные с', default=None),
        end_date=Query(example='2023-04-09', description='Данные по', default=None),
):
    pass


@app.on_event("startup")
def save_openapi_yaml():
    data = app.openapi()

    with open("openapi_paths.yaml", "w") as file:
        yaml.dump(data["paths"], file, allow_unicode=True)

    with open("openapi_schemas.yaml", "w") as file:
        yaml.dump(data["components"]["schemas"], file, allow_unicode=True)
