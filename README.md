# Генерация swagger-документа

Помощник по генерации swagger-документа.
В сигнатуре метода `Func` указываем поля запроса, в файле `response.json` сохраняем (например из Postman) ответ сервера.

Далее в корневой директории появятся два файла: `openapi_schemas.yaml` в котором расположены схемы для `$ref`.
В файле `openapi_paths.yaml` будет код, который нужно вставить в swagger-документ.

При внесении изменений в сигнатуру или `response.json` изменения применятся автоматически и "пересоберут" нужные нам файлы.

Пример функции с необходимой сигнатурой:
```python
async def Func(
        brand: str = Query(example='adidas', description='Бренд'),
        sku_scheme: List[SkuSchemes] = Query(example='FBO', description='SKU-схема', alias='sku_schema[]', default=None),
        start_date=Query(example='2023-03-11', description='Данные с', default=None),
        end_date=Query(example='2023-04-09', description='Данные по', default=None),
):
    pass
```

## Установка
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Запуск
```bash
uvicorn main:app --reload
```

### Документация по FastAPI
***Документация по [FastAPI](https://fastapi.tiangolo.com/tutorial/query-params/) Query parameters.***

***Документация по [FastAPI](https://fastapi.tiangolo.com/tutorial/path-params/) Path parameters.***