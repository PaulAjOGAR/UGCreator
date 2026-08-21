# UGCreator

A Python-based User-Generated Content (UGC) platform for managing products and reviews with content moderation capabilities.

## 🚀 Overview

UGCreator is a FastAPI-based web application designed to handle user-generated content creation and management. It provides a comprehensive platform for users to create accounts, post products, and submit reviews with built-in moderation features.

## ✨ Features (In Development)

- **User Management**: User registration and authentication with credibility scoring
- **Product Management**: Create and manage products with brand categorization
- **Review System**: Submit and manage reviews with rating system
- **Content Moderation**: Automated review moderation with guideline compliance scoring
- **Trust Scoring**: User credibility and trust level tracking
- **RESTful API**: Clean, well-documented API endpoints

## 🛠️ Tech Stack

### Backend Framework
- **FastAPI** (0.137.1) - Modern async web framework
- **Uvicorn** (0.49.0) - ASGI server
- **Starlette** (1.3.1) - Lightweight web components

### Database & ORM
- **PostgreSQL** - Primary data store
- **SQLAlchemy** (2.0.51) - SQL toolkit and ORM
- **Psycopg2** - PostgreSQL adapter
- **Alembic** (1.18.4) - Database migrations

### Task Queue & Caching
- **Celery** (5.6.3) - Distributed task queue (planned)
- **Redis** (8.0.0) - Caching and message broker (planned)
- **Kombu** (5.6.2) - Message transport

### Security & Authentication
- **Passlib** (1.7.4) - Password hashing
- **Bcrypt** (4.0.1) - Cryptographic hashing
- **python-jose** (3.5.0) - JWT token handling
- **python-multipart** (0.0.32) - Form data parsing

### Data Processing & NLP
- **Pydantic** (2.13.4) - Data validation and serialization
- **Spacy** - Natural language processing for content moderation
- **python-dateutil** (2.9.0) - Date/time utilities

### Utilities
- **python-dotenv** - Environment variable management
- **Click** (8.4.1) - CLI framework (for future features)

## 📁 Project Structure

```
UGCreator/
├── app/
│   ├── __init__.py
│   ├── main.py                 # FastAPI application entry point
│   ├── core/
│   │   └── database.py         # Database configuration and setup
│   ├── models/                 # SQLAlchemy database models
│   │   ├── user.py             # User model with credibility scoring
│   │   ├── product.py          # Product model
│   │   └── review.py           # Review model with moderation fields
│   ├── schemas/                # Pydantic request/response schemas
│   │   ├── user.py
│   │   ├── product.py
│   │   └── review.py
│   ├── routers/                # API route handlers
│   │   ├── users.py
│   │   ├── products.py
│   │   └── reviews.py
│   └── services/               # Business logic services
│       └── moderation.py       # Content moderation using Spacy
├── requirements.txt            # Python dependencies
├── .env                        # Environment variables (not in version control)
├── .gitignore
└── README.md
```

## 🗄️ Data Models

### User
- Email, username, name
- Hashed password (bcrypt)
- Credibility score (default: 50)
- Trust level (0-based)
- Account status tracking
- Timestamps (created_at, updated_at)

### Product
- Name, description, brand, category
- Owner ID (Foreign key to User)
- Average rating and review count
- Timestamps

### Review
- User ID and Product ID (Foreign keys)
- Rating and review body
- Guideline compliance score
- Approval status
- Timestamps

## 📋 Prerequisites

- Python 3.8 or higher
- PostgreSQL database
- Redis (for task queue and caching - planned)
- pip package manager

## 🔧 Installation

1. **Clone the repository**
```bash
git clone https://github.com/PaulAjOGAR/UGCreator.git
cd UGCreator
```

2. **Create a virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Download Spacy model** (for NLP features)
```bash
python -m spacy download en_core_web_sm
```

5. **Configure environment variables**
```bash
# Create .env file based on .env template
cp .env .env.local
```

Edit `.env.local` with your settings:
```
DATABASE_URL=postgresql://user:password@localhost:5432/ugcreator
REDIS_URL=redis://localhost:6379
SECRET_KEY=your-secret-key-here
```

6. **Initialize the database**
```bash
# Create tables
python -c "from app.main import app; from app.core.database import Base, engine; Base.metadata.create_all(bind=engine)"
```

## 🚀 Running the Application

### Development Server
```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

The API will be available at `http://localhost:8000`

### API Documentation
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## 📚 API Endpoints (In Development)

### Users
- `POST /users/register` - Register new user
- `POST /users/login` - User login
- `GET /users/{user_id}` - Get user details
- `PUT /users/{user_id}` - Update user profile

### Products
- `POST /products` - Create product
- `GET /products` - List all products
- `GET /products/{product_id}` - Get product details
- `PUT /products/{product_id}` - Update product
- `DELETE /products/{product_id}` - Delete product

### Reviews
- `POST /reviews` - Create review
- `GET /reviews` - List reviews
- `GET /reviews/{review_id}` - Get review details
- `PUT /reviews/{review_id}` - Update review
- `DELETE /reviews/{review_id}` - Delete review

## 🔒 Security Features (Planned)

- JWT-based authentication
- Password hashing with bcrypt
- Review moderation with guideline scoring
- User credibility tracking
- Content validation with Pydantic

## 🚧 Current Status

⚠️ **This project is actively under development.** 

### Completed:
- Project structure and initialization
- Database models (User, Product, Review)
- Basic FastAPI setup with routers

### In Progress:
- Route implementations
- Pydantic schemas and validation
- Content moderation logic
- Authentication and authorization

### Planned:
- Background task processing (Celery)
- Redis caching
- Unit and integration tests
- Admin moderation panel
- User reputation system enhancements
- Email notifications

## 📝 Development

### Project Layout
- Models define the database schema
- Routers handle HTTP endpoints
- Schemas provide request/response validation
- Services contain business logic (e.g., moderation)

### Code Style
- PEP 8 compliant
- Type hints recommended
- Async/await for FastAPI handlers

## 🤝 Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📖 License

This project is not yet under a specific license. 

## 📞 Support & Contact

For issues, questions, or suggestions, please:
- Open an issue on GitHub: [UGCreator Issues](https://github.com/PaulAjOGAR/UGCreator/issues)
- Contact the author: [@PaulAjOGAR](https://github.com/PaulAjOGAR)

## 👤 Author

**PaulAjOGAR**  
GitHub: [@PaulAjOGAR](https://github.com/PaulAjOGAR)

---

**Created**: June 16, 2026  
**Last Updated**: August 21, 2026
