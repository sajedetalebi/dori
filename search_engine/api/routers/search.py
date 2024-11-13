from fastapi import APIRouter, Query, Depends
from core.search.service import SearchService
from data.schemas.models import SearchResponse

router = APIRouter()

@router.get("/", response_model=SearchResponse)
async def search_products(
    query: str = Query(..., min_length=1),
    category: str = None,
    price_min: float = None,
    price_max: float = None,
    search_service: SearchService = Depends()
):
    results = await search_service.search_products(
        query, category, price_min, price_max
    )
    return SearchResponse(results=results)
