from core.database.vector_store import VectorStore
from config.settings import settings
import logging

logger = logging.getLogger(__name__)

def setup_vector_database():
    try:
        vector_store = VectorStore(
            host=settings.VECTOR_DB_HOST,
            port=settings.VECTOR_DB_PORT
        )
        
        # Initialize collection with CLIP embedding dimension (512)
        vector_store.init_collection(vector_size=512)
        logger.info("Vector database initialized successfully")
        
    except Exception as e:
        logger.error(f"Failed to initialize vector database: {str(e)}")
        raise

if __name__ == "__main__":
    setup_vector_database()
