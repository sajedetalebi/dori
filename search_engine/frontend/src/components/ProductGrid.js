import React from 'react';

export const ProductGrid = ({ products }) => {
    return (
        <div className="product-grid">
            {products.map(product => (
                <div key={product.id} className="product-card">
                    <img src={product.image_url} alt={product.title} />
                    <h3>{product.title}</h3>
                    <p>${product.price}</p>
                </div>
            ))}
        </div>
    );
};
