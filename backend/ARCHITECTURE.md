# Backend Architecture

## Overview

The backend follows **Clean Architecture** principles with clear separation of concerns and dependency injection.

## Directory Structure

```
backend/
├── api/                    # API Layer
│   ├── __init__.py
│   └── routes.py          # FastAPI route handlers
│
├── core/                   # Core Functionality
│   ├── __init__.py
│   ├── config.py          # Application settings
│   ├── exceptions.py      # Custom exceptions
│   └── logging.py         # Logging configuration
│
├── db/                     # Database Layer
│   ├── __init__.py
│   └── session.py         # Session management & connection pooling
│
├── models/                 # Data Models
│   ├── __init__.py
│   ├── database.py        # SQLAlchemy ORM models
│   └── schemas.py         # Pydantic validation schemas
│
├── services/               # Business Logic Layer
│   ├── __init__.py
│   ├── guidance.py        # Guidance retrieval service
│   └── vector_store.py    # Vector store service (FAISS)
│
├── scripts/                # Utility Scripts
│   └── seed_database.py   # Database seeding script
│
├── app.py                  # Main application entry point
├── requirements.txt        # Python dependencies
└── .env                    # Environment variables
```

## Layers

### 1. API Layer (`api/`)
- **Responsibility**: HTTP request/response handling
- **Components**:
  - Route handlers
  - Request validation
  - Response formatting
  - HTTP status codes
- **Dependencies**: Services, Database session

### 2. Service Layer (`services/`)
- **Responsibility**: Business logic
- **Components**:
  - `GuidanceService`: Orchestrates guidance retrieval
  - `VectorStoreService`: Manages embeddings and similarity search
- **Dependencies**: Database models, Configuration

### 3. Data Layer (`models/`, `db/`)
- **Responsibility**: Data persistence and validation
- **Components**:
  - SQLAlchemy models (database.py)
  - Pydantic schemas (schemas.py)
  - Session management (session.py)
- **Dependencies**: Configuration

### 4. Core Layer (`core/`)
- **Responsibility**: Cross-cutting concerns
- **Components**:
  - Configuration management
  - Logging
  - Custom exceptions
- **Dependencies**: None (foundation layer)

## Design Patterns

### 1. Dependency Injection
```python
# Services are injected via FastAPI dependencies
async def get_guidance(
    query: EmotionQuery,
    db: Session = Depends(get_db),
    vector_store: VectorStoreService = Depends(get_vector_store)
):
    guidance_service = GuidanceService(db, vector_store)
    return guidance_service.get_guidance(query.emotion_query)
```

### 2. Repository Pattern
- Database access is abstracted through SQLAlchemy ORM
- Services interact with models, not raw SQL

### 3. Singleton Pattern
- Vector store service is a singleton (expensive to initialize)
- Configuration settings are cached

### 4. Factory Pattern
- Database sessions created via factory function
- Settings loaded via factory function

## Data Flow

```
1. HTTP Request
   ↓
2. API Route Handler (routes.py)
   ↓
3. Request Validation (Pydantic schemas)
   ↓
4. Service Layer (guidance.py)
   ↓
5. Vector Store Search (vector_store.py)
   ↓
6. Database Query (SQLAlchemy)
   ↓
7. Response Formatting (Pydantic schemas)
   ↓
8. HTTP Response
```

## Error Handling

### Custom Exception Hierarchy
```
IslamicGuidanceException (base)
├── DatabaseException
├── VectorStoreException
└── EmbeddingException
```

### Error Flow
1. Service layer raises custom exceptions
2. API layer catches exceptions
3. Converts to appropriate HTTP status codes
4. Returns formatted error response

## Configuration Management

- Environment-based configuration using Pydantic Settings
- Type-safe configuration with validation
- Cached settings for performance
- Supports `.env` files

## Logging Strategy

- Structured logging throughout application
- Log levels: INFO, WARNING, ERROR
- Includes timestamps and module names
- Separate loggers per module

## Database Management

### Connection Pooling
```python
engine = create_engine(
    settings.database_url,
    pool_pre_ping=True,    # Verify connections
    pool_size=5,           # Connection pool size
    max_overflow=10        # Max overflow connections
)
```

### Session Management
- Session per request pattern
- Automatic rollback on errors
- Proper cleanup in finally block

## Vector Store Architecture

### FAISS Implementation
- Separate indexes for each collection type
- L2 distance metric for similarity
- Persistent storage to disk
- Lazy loading on startup

### Embedding Pipeline
1. Text → Sentence Transformer
2. Generate 384-dimensional vector
3. Store in FAISS index
4. Save to disk

### Search Pipeline
1. Query → Embedding
2. FAISS similarity search
3. Retrieve top-k per collection
4. Merge and sort results
5. Fetch full data from database

## Best Practices Implemented

1. **Type Hints**: Full type annotations for IDE support
2. **Validation**: Pydantic models for data validation
3. **Error Handling**: Comprehensive exception handling
4. **Logging**: Structured logging throughout
5. **Documentation**: Docstrings for all functions
6. **Separation of Concerns**: Clear layer boundaries
7. **Dependency Injection**: Loose coupling between components
8. **Configuration**: Environment-based settings
9. **Testing**: Testable architecture with DI
10. **Performance**: Connection pooling, caching, async support

## Performance Optimizations

1. **Connection Pooling**: Reuse database connections
2. **Vector Store Caching**: Load indexes once on startup
3. **Settings Caching**: LRU cache for configuration
4. **Async/Await**: Non-blocking I/O operations
5. **Batch Processing**: Efficient embedding generation

## Security Considerations

1. **Environment Variables**: Sensitive data in .env
2. **SQL Injection**: Protected by SQLAlchemy ORM
3. **Input Validation**: Pydantic validation on all inputs
4. **CORS**: Configurable CORS policy
5. **Error Messages**: No sensitive data in error responses

## Scalability

### Horizontal Scaling
- Stateless API design
- Shared database (Neon PostgreSQL)
- Vector store can be moved to dedicated service

### Vertical Scaling
- Connection pooling handles more concurrent requests
- FAISS is CPU-optimized
- Can upgrade to GPU-accelerated FAISS

## Future Enhancements

1. **Caching Layer**: Redis for frequently accessed data
2. **Rate Limiting**: Protect against abuse
3. **Authentication**: JWT-based auth
4. **Monitoring**: Prometheus metrics
5. **Testing**: Unit and integration tests
6. **CI/CD**: Automated deployment pipeline
7. **API Versioning**: Support multiple API versions
8. **Pagination**: For large result sets
