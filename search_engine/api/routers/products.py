from fastapi import APIRouter, HTTPException, Depends
from typing import List
from data.schemas.models import Product
from core.search.service import SearchService

router = APIRouter()

@router.get("/", response_model=List[Product])
async def get_products(
    category: str = None,
    limit: int = 10,
    search_service: SearchService = Depends()
):
    products = await search_service.get_products(category=category, limit=limit)
    return products

@router.get("/{product_id}", response_model=Product)
async def get_product(
    product_id: int,
    search_service: SearchService = Depends()
):
    product = await search_service.get_product_by_id(product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product
