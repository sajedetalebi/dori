from typing import Dict, List, Any
from datetime import datetime

class ProductProcessor:
    @staticmethod
    def clean_data(data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        cleaned_data = []
        for item in data:
            if all(key in item for key in ['id', 'name', 'images']):
                cleaned_item = {
                    'id': int(item['id']),
                    'name': str(item['name']).strip(),
                    'description': str(item.get('description', '')).strip(),
                    'images': item['images'],
                    'current_price': float(item['current_price']),
                    'shop_name': str(item['shop_name']),
                    'status': str(item['status']),
                    'update_date': datetime.strptime(item['update_date'], '%Y-%m-%d %H:%M:%S.%f')
                }
                cleaned_data.append(cleaned_item)
        return cleaned_data

    @staticmethod
    def format_metadata(product: Dict[str, Any]) -> Dict[str, Any]:
        return {
            'id': int(product['id']),
            'name': str(product['name']),
            'description': str(product.get('description', '')),
            'image_url': product['images'][0] if product['images'] else None,
            'additional_images': product['images'][1:] if len(product['images']) > 1 else [],
            'current_price': float(product['current_price']),
            'shop_name': str(product['shop_name']),
            'status': str(product['status']),
            'colors': product.get('colors', []),
            'sizes': product.get('sizes', []),
            'currency': str(product['currency']),
            'link': str(product['link'])
        }

    @staticmethod
    def validate_product(product: Dict[str, Any]) -> bool:
        required_fields = ['id', 'name', 'images', 'current_price', 'shop_name']
        return all(field in product for field in required_fields)
