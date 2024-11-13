from pydantic import BaseModel, HttpUrl
from typing import List, Optional
from datetime import datetime

class Product(BaseModel):
    id: int
    name: str
    description: Optional[str]
    material: Optional[str]
    rating: Optional[float]
    images: List[str]
    code: str
    brand_id: Optional[int]
    brand_name: Optional[str]
    category_id: Optional[int]
    category_name: Optional[str]
    gender_id: Optional[int]
    gender_name: Optional[str]
    shop_id: int
    shop_name: str
    link: str
    status: str
    colors: List[str]
    sizes: List[str]
    region: str
    currency: str
    current_price: float
    old_price: Optional[float]
    off_percent: Optional[int]
    update_date: datetime

    class Config:
        orm_mode = True

class SearchResponse(BaseModel):
    results: List[Product]
    total: int
    page: int
    page_size: int
