"""Custom exceptions for the application."""


class IslamicGuidanceException(Exception):
    """Base exception for the application."""
    pass


class DatabaseException(IslamicGuidanceException):
    """Database-related exceptions."""
    pass


class VectorStoreException(IslamicGuidanceException):
    """Vector store-related exceptions."""
    pass


class EmbeddingException(IslamicGuidanceException):
    """Embedding generation exceptions."""
    pass
