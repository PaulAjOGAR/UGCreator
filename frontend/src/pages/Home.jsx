import { useState, useEffect } from 'react'
import { Link } from 'react-router-dom'

function Home() {
    const [products, setProducts] = useState([])

    useEffect(() => {
        fetch('http://127.0.0.1:8000/products/')
            .then(res => res.json())
            .then(data => setProducts(data))
    }, [])

    return (
        <div>
            <h2>HypeCheck — Product Feed</h2>
            {products.map((product) => (
                <div key={product.id}>
                    <Link to={`/products/${product.id}`}>
                        <h3>{product.name}</h3>
                    </Link>
                    <p>{product.brand}</p>
                    <p>Rating: {product.avg_rating} ⭐</p>
                    <p>Reviews: {product.review_count}</p>
                </div>
            ))}
        </div>
    )
}

export default Home