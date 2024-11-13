class ImageProcessor:
    def __init__(self, cache_dir: str = "data/processed/images"):
        from pathlib import Path
        self.cache_dir = Path(cache_dir)
        self.cache_dir.mkdir(parents=True, exist_ok=True)

    def load_image(self, image_url: str) -> Image.Image:
        from PIL import Image
        import requests
        import io
        response = requests.get(image_url)
        image = Image.open(io.BytesIO(response.content))
        return image.convert('RGB')

    from typing import List
    from PIL import Image

    def process_product_images(self, images: List[str]) -> List[Image.Image]:
        processed_images = []
        for image_url in images:
            image = self.load_image(image_url)
            processed_image = self.preprocess_image(image)
            processed_images.append(processed_image)
        return processed_images

    def preprocess_image(self, image: Image.Image, target_size=(224, 224)) -> Image.Image:
        return image.resize(target_size)
