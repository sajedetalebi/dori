const API_BASE_URL = process.env.REACT_APP_API_BASE_URL || 'http://localhost:8000/api';

export const searchProducts = async (query, filters) => {
    const response = await fetch(`${API_BASE_URL}/search?query=${query}`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(filters),
    });
    return response.json();
};

export const getProduct = async (productId) => {
    const response = await fetch(`${API_BASE_URL}/products/${productId}`);
    return response.json();
};
