import pandas as pd
from core.clip.encoder import ClipEncoder
from core.database.vector_store import VectorStore
from PIL import Image
import requests

def load_and_process_products(file_path: str):
    df = pd.read_csv(file_path)
    encoder = ClipEncoder()
    vector_store = VectorStore(host="vector_db", port=6333)
    
    for _, row in df.iterrows():
        image = Image.open(requests.get(row['image_url'], stream=True).raw)
        vector = encoder.encode_image(image)
        metadata = {
            'title': row['title'],
            'price': row['price'],
            'category': row['category'],
            'image_url': row['image_url']
        }
        vector_store.insert_vectors([vector], [metadata])

if __name__ == "__main__":
    load_and_process_products("data/products.csv")
