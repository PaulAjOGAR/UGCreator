import { useState, useEffect } from 'react'
import { useParams } from 'react-router-dom'

function ProductPage() {
    const { id } = useParams()
    const [product, setProduct] = useState(null)
    const [reviews, setReviews] = useState([])
    const [body, setBody] = useState('')
    const [rating, setRating] = useState(0)

    // your useEffect here — fetch both product and reviews
    useEffect(() => {
        fetch(`http://localhost:8000/products/${id}`)
            .then(res => res.json())
            .then(data => setProduct(data))
        fetch(`http://localhost:8000/reviews/${id}`)
            .then(res => res.json())
            .then(data => setReviews(data))
        },
    []
    )
    const handleReviewSubmit = async (e) => {
    e.preventDefault()
    const token = localStorage.getItem('token')
    const response = await fetch('http://localhost:8000/reviews/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${token}`
        },
        body: JSON.stringify({
            product_id: parseInt(id),
            body,
            rating: parseInt(rating)
        })
    })
    const data = await response.json()
    if (response.ok) {
        alert('Review submitted!')
        setReviews([...reviews, data])
    } else {
        alert(data.detail)
    }
}

    return (
    <div>
        {product && (
            <>
                <h2>{product.name}</h2>
                <p>{product.brand} — {product.category}</p>
                <p>Average Rating: {product.avg_rating} ⭐</p>
                <p>{product.description}</p>
            </>
        )}

        <h3>Write a Review</h3>
        <form onSubmit={handleReviewSubmit}>
            <textarea
                placeholder="Write your review..."
                value={body}
                onChange={(e) => setBody(e.target.value)}
            />
            <input
                type="number"
                min="1"
                max="5"
                value={rating}
                onChange={(e) => setRating(e.target.value)}
            />
            <button type="submit">Submit Review</button>
        </form>

        <h3>Reviews</h3>
        {reviews.map((review) => (
            <div key={review.id}>
                <p>Rating: {review.rating} ⭐</p>
                <p>{review.body}</p>
                <p>Approved: {review.approved ? 'Yes' : 'No'}</p>
            </div>
        ))}
    </div>
)
}

export default ProductPage