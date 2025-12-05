"""API route handlers."""
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
import time

from models.schemas import EmotionQuery, GuidanceResponse, HealthResponse
from services.guidance import GuidanceService
from services.vector_store import get_vector_store, VectorStoreService
from db.session import get_db
from core.logging import get_logger
from core.exceptions import IslamicGuidanceException

logger = get_logger(__name__)
router = APIRouter()


@router.post(
    "/guidance",
    response_model=GuidanceResponse,
    status_code=status.HTTP_200_OK,
    summary="Get Islamic guidance based on emotional state",
    description="Returns relevant Quran verses, Duas, and Hadiths based on semantic similarity"
)
async def get_guidance(
    query: EmotionQuery,
    db: Session = Depends(get_db),
    vector_store: VectorStoreService = Depends(get_vector_store)
) -> GuidanceResponse:
    """
    Main endpoint for retrieving Islamic guidance.
    
    Args:
        query: Emotion query from user
        db: Database session
        vector_store: Vector store service
        
    Returns:
        Guidance response with relevant Islamic texts
    """
    start_time = time.time()
    
    try:
        # Create guidance service
        guidance_service = GuidanceService(db, vector_store)
        
        # Get guidance results
        results = guidance_service.get_guidance(query.emotion_query)
        
        elapsed_time = (time.time() - start_time) * 1000
        logger.info(f"Query processed in {elapsed_time:.2f}ms")
        
        return GuidanceResponse(
            results=results,
            query=query.emotion_query,
            total_results=len(results)
        )
    
    except IslamicGuidanceException as e:
        logger.error(f"Application error: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An unexpected error occurred"
        )


@router.get(
    "/health",
    response_model=HealthResponse,
    status_code=status.HTTP_200_OK,
    summary="Health check endpoint"
)
async def health_check(
    db: Session = Depends(get_db),
    vector_store: VectorStoreService = Depends(get_vector_store)
) -> HealthResponse:
    """
    Check the health status of the API and its dependencies.
    
    Returns:
        Health status information
    """
    try:
        # Test database connection
        from sqlalchemy import text
        db.execute(text("SELECT 1"))
        db_status = "healthy"
    except Exception as e:
        logger.error(f"Database health check failed: {e}")
        db_status = "unhealthy"
    
    try:
        # Test vector store
        vector_store_status = "healthy" if vector_store else "unhealthy"
    except Exception as e:
        logger.error(f"Vector store health check failed: {e}")
        vector_store_status = "unhealthy"
    
    overall_status = "healthy" if db_status == "healthy" and vector_store_status == "healthy" else "degraded"
    
    return HealthResponse(
        status=overall_status,
        version="1.0.0",
        database=db_status,
        vector_store=vector_store_status
    )
