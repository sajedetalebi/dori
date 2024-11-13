import React, { useState } from 'react';
import { SearchBox } from '../components/SearchBox';
import { ProductGrid } from '../components/ProductGrid';
import { Filters } from '../components/Filters';

export const SearchPage = () => {
    const [products, setProducts] = useState([]);
    const [loading, setLoading] = useState(false);

    const handleSearch = async (query, filters) => {
        setLoading(true);
        try {
            const response = await fetch(`/api/search?query=${query}`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(filters),
            });
            const data = await response.json();
            setProducts(data.results);
        } catch (error) {
            console.error('Search failed:', error);
        }
        setLoading(false);
    };

    return (
        <div className="search-page">
            <SearchBox onSearch={handleSearch} />
            <Filters onFilterChange={handleSearch} />
            {loading ? (
                <div>Loading...</div>
            ) : (
                <ProductGrid products={products} />
            )}
        </div>
    );
};
