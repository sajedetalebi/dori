from core.search.service import SearchService
from core.database.vector_store import VectorStore
from core.clip.encoder import ClipEncoder
from config.settings import settings

def get_vector_store():
    return VectorStore(
        host=settings.VECTOR_DB_HOST,
        port=settings.VECTOR_DB_PORT
    )

def get_clip_encoder():
    return ClipEncoder()

def get_search_service():
    vector_store = get_vector_store()
    encoder = get_clip_encoder()
    return SearchService(vector_store=vector_store, encoder=encoder)
