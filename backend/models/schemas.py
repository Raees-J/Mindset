"""Pydantic schemas for API request/response validation."""
from pydantic import BaseModel, Field
from typing import Literal


class EmotionQuery(BaseModel):
    """Request schema for emotion-based guidance query."""
    
    emotion_query: str = Field(
        ...,
        min_length=3,
        max_length=500,
        description="Natural language description of emotional state",
        examples=["I feel anxious and need comfort"]
    )


class GuidanceResult(BaseModel):
    """Schema for a single guidance result."""
    
    type: Literal["Quran", "Dua", "Hadith"] = Field(
        ...,
        description="Type of Islamic text"
    )
    arabic_text: str = Field(
        ...,
        description="Original Arabic text"
    )
    translation: str = Field(
        ...,
        description="English translation"
    )
    citation: str = Field(
        ...,
        description="Source reference (e.g., 'Quran 2:153')"
    )
    similarity_score: float = Field(
        ...,
        ge=0.0,
        le=1.0,
        description="Semantic similarity score (0-1)"
    )


class GuidanceResponse(BaseModel):
    """Response schema for guidance query."""
    
    results: list[GuidanceResult] = Field(
        ...,
        description="List of relevant Islamic texts"
    )
    query: str = Field(
        ...,
        description="Original query"
    )
    total_results: int = Field(
        ...,
        description="Number of results returned"
    )


class HealthResponse(BaseModel):
    """Health check response schema."""
    
    status: str
    version: str
    database: str
    vector_store: str
