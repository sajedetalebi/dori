import json
from pathlib import Path
from data.processors.product_processor import ProductProcessor
from data.processors.image_processor import ImageProcessor
from core.clip.encoder import ClipEncoder
from core.database.vector_store import VectorStore
from config.settings import settings
import logging

logger = logging.getLogger(__name__)

class DataInitializer:
    def __init__(self):
        self.product_processor = ProductProcessor()
        self.image_processor = ImageProcessor()
        self.clip_encoder = ClipEncoder()
        self.vector_store = VectorStore(
            host=settings.VECTOR_DB_HOST,
            port=settings.VECTOR_DB_PORT
        )

    def initialize_database(self):
        # Create vector collection if not exists
        self.vector_store.init_collection(vector_size=512)
        logger.info("Vector collection initialized")

    def load_products(self, file_path: str):
        with open(file_path, 'r') as f:
            products = json.load(f)
        return products

    def process_and_store_products(self, products):
        for product in products:
            if self.product_processor.validate_product(product):
                # Process product metadata
                metadata = self.product_processor.format_metadata(product)
                
                # Process main product image
                main_image = self.image_processor.load_image(product['images'][0])
                processed_image = self.image_processor.preprocess_image(main_image)
                
                # Generate vector embedding
                vector = self.clip_encoder.encode_image(processed_image)
                
                # Store in vector database
                self.vector_store.insert_vectors([vector], [metadata])
                
                logger.info(f"Processed and stored product: {metadata['id']}")

def run_initialization():
    initializer = DataInitializer()
    
    # Initialize database
    initializer.initialize_database()
    
    # Load and process products
    products = initializer.load_products('data/raw/products.json')
    initializer.process_and_store_products(products)
    
    logger.info("Data initialization completed successfully")

if __name__ == "__main__":
    run_initialization()
