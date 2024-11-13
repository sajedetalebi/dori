from core.clip.encoder import ClipEncoder
from core.database.vector_store import VectorStore

class SearchService:
    def __init__(self):
        self.encoder = ClipEncoder()
        self.vector_store = VectorStore(host="vector_db", port=6333)
    
    async def search_products(self, query: str, category: str = None, 
                            price_min: float = None, price_max: float = None):
        query_vector = self.encoder.encode_text(query)
        filters = self._build_filters(category, price_min, price_max)
        results = self.vector_store.search(query_vector, filters)
        return results
    
    def _build_filters(self, category, price_min, price_max):
        filters = {}
        if category:
            filters["category"] = category
        if price_min or price_max:
            filters["price"] = {"$gte": price_min, "$lte": price_max}
        return filters
