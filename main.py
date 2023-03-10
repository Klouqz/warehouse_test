from fastapi import FastAPI
from pydantic import BaseModel
from models import Warehouse, Product
from datetime import datetime
from db_connector import DBConnector

app = FastAPI()
db_helper = DBConnector()


class WarehouseModel(BaseModel):
    name: str
    description: str
    address: str


class ProductModel(BaseModel):
    name: str
    description: str
    category: str
    price: float
    supplier: str


@app.post("/warehouse")
async def create_warehouse(warehouse: WarehouseModel):
    created_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    db_helper.insert_warehouse(Warehouse(**warehouse.dict(), created_at=created_at))
    return {"message": "Warehouse created successfully"}


@app.post("/product")
async def create_product(product: ProductModel):
    created_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    db_helper.insert_product(Product(**product.dict(), created_at=created_at))
    return {"message": "Product created successfully"}


@app.get("/warehouses")
async def get_all_warehouses():
    warehouses = db_helper.get_warehouses()
    return {"warehouses": [warehouse.__dict__ for warehouse in warehouses]}


@app.get("/products")
async def get_all_products():
    products = db_helper.get_products()
    return {"products": [product.__dict__ for product in products]}


@app.get("/warehouse/{id}")
async def get_warehouse_by_id(id: int):
    warehouse = db_helper.get_warehouse_by_id(id)
    return {"warehouse": warehouse.__dict__}


@app.get("/product/{id}")
async def get_product_by_id(id: int):
    product = db_helper.get_product_by_id(id)
    return {"product": product.__dict__}