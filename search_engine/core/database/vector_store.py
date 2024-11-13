
from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams, PointStruct

class VectorStore:
    def __init__(self, host: str, port: int):
        self.client = QdrantClient(host=host, port=port)
        self.collection_name = "products"
        
    def init_collection(self, vector_size: int):
        self.client.recreate_collection(
            collection_name=self.collection_name,
            vectors_config=VectorParams(size=vector_size, distance=Distance.COSINE)
        )
    
    def insert_vectors(self, vectors, metadata):
        points = [
            PointStruct(
                id=idx,
                vector=vector.tolist(),
                payload=meta
            )
            for idx, (vector, meta) in enumerate(zip(vectors, metadata))
        ]
        self.client.upsert(collection_name=self.collection_name, points=points)
