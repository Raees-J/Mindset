# Islamic Guidance API - Backend

Production-ready FastAPI backend with semantic search for Islamic texts using Sentence Transformers and FAISS.

## Architecture

```
backend/
├── api/              # API routes and endpoints
├── core/             # Core functionality (config, logging, exceptions)
├── db/               # Database session management
├── models/           # Data models (SQLAlchemy & Pydantic)
├── services/         # Business logic layer
├── scripts/          # Utility scripts (seeding, etc.)
└── app.py            # Main application entry point
```

## Features

- ✅ Clean architecture with separation of concerns
- ✅ Dependency injection pattern
- ✅ Comprehensive error handling
- ✅ Structured logging
- ✅ Type hints throughout
- ✅ Pydantic validation
- ✅ Health check endpoint
- ✅ CORS support
- ✅ Connection pooling
- ✅ Async/await support

## Setup

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Configure Environment

```bash
cp .env.example .env
# Edit .env with your Neon connection string
```

### 3. Seed Database

```bash
python scripts/seed_database.py
```

### 4. Run Server

```bash
uvicorn app:app --reload --host 0.0.0.0 --port 8000
```

## API Endpoints

### POST /api/v1/guidance

Get Islamic guidance based on emotional state.

**Request:**
```json
{
  "emotion_query": "I feel anxious and need comfort"
}
```

**Response:**
```json
{
  "results": [
    {
      "type": "Quran",
      "arabic_text": "...",
      "translation": "...",
      "citation": "Quran 2:153",
      "similarity_score": 0.8542
    }
  ],
  "query": "I feel anxious and need comfort",
  "total_results": 5
}
```

### GET /api/v1/health

Health check endpoint.

**Response:**
```json
{
  "status": "healthy",
  "version": "1.0.0",
  "database": "healthy",
  "vector_store": "healthy"
}
```

## Technology Stack

- **FastAPI**: Modern async web framework
- **SQLAlchemy**: ORM for database operations
- **Pydantic**: Data validation
- **Sentence Transformers**: Generate embeddings (all-MiniLM-L6-v2)
- **FAISS**: Vector database for semantic search
- **PostgreSQL/Neon**: Relational database
- **Python 3.12+**: Programming language

## Best Practices Implemented

1. **Separation of Concerns**: Clear separation between API, business logic, and data layers
2. **Dependency Injection**: Services injected via FastAPI dependencies
3. **Error Handling**: Custom exceptions with proper HTTP status codes
4. **Logging**: Structured logging throughout the application
5. **Type Safety**: Full type hints for better IDE support and error detection
6. **Validation**: Pydantic models for request/response validation
7. **Database Management**: Connection pooling and session management
8. **Configuration**: Environment-based configuration with Pydantic Settings
9. **Code Organization**: Modular structure for maintainability
10. **Documentation**: OpenAPI/Swagger docs auto-generated

## Performance

- Target response time: < 300ms
- Connection pooling enabled
- Vector search optimized with FAISS
- Async request handling

## Development

```bash
# Run with auto-reload
uvicorn app:app --reload

# Access API docs
http://localhost:8000/docs

# Access alternative docs
http://localhost:8000/redoc
```
