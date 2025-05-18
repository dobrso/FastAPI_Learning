from fastapi import FastAPI
from models import Product
from typing import List

app = FastAPI()

sample_product_1 = {
    "product_id": 123,
    "name": "Smartphone",
    "category": "Electronics",
    "price": 599.99
}

sample_product_2 = {
    "product_id": 456,
    "name": "Phone Case",
    "category": "Accessories",
    "price": 19.99
}

sample_product_3 = {
    "product_id": 789,
    "name": "Iphone",
    "category": "Electronics",
    "price": 1299.99
}

sample_product_4 = {
    "product_id": 101,
    "name": "Headphones",
    "category": "Accessories",
    "price": 99.99
}

sample_product_5 = {
    "product_id": 202,
    "name": "Smartwatch",
    "category": "Electronics",
    "price": 299.99
}

sample_products = [sample_product_1, sample_product_2, sample_product_3, sample_product_4, sample_product_5]

@app.get("/product/{product_id}")
async def getProduct(product_id: int) -> Product:
    try:
        for product in sample_products:
            if product["product_id"] == product_id:
                return product
    except Exception as e:
        raise e

@app.get("/products/search")
async def getProducts(keyword: str,
                        category: str = None,
                         limit: int = 10) -> List[Product]:
    try:
        products = list(filter(lambda product: keyword.lower() in product["name"].lower(), sample_products))
        if category:
            products = list(filter(lambda product: product["category"].lower() == category.lower(), products))
        return products[:limit]
    except Exception as e:
        raise e
    