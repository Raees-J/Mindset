"""Business logic for guidance retrieval."""
from sqlalchemy.orm import Session
from typing import Optional

from models.database import QuranAyah, Dua, Hadith
from models.schemas import GuidanceResult
from services.vector_store import VectorStoreService
from core.logging import get_logger
from core.exceptions import DatabaseException

logger = get_logger(__name__)


class GuidanceService:
    """Service for retrieving Islamic guidance based on emotional queries."""
    
    def __init__(self, db: Session, vector_store: VectorStoreService):
        """
        Initialize guidance service.
        
        Args:
            db: Database session
            vector_store: Vector store service instance
        """
        self.db = db
        self.vector_store = vector_store
    
    def get_guidance(
        self,
        query: str,
        top_k_per_type: Optional[int] = None
    ) -> list[GuidanceResult]:
        """
        Get relevant Islamic guidance for an emotional query.
        
        Args:
            query: Natural language emotional query
            top_k_per_type: Number of results per type
            
        Returns:
            List of guidance results
        """
        try:
            # Perform semantic search
            search_results = self.vector_store.search_all(
                query,
                top_k_per_type=top_k_per_type
            )
            
            guidance_results = []
            
            for result in search_results:
                result_type = result['type']
                result_id = int(result['id'])
                distance = result['distance']
                
                # Convert distance to similarity score
                similarity_score = self._distance_to_similarity(distance)
                
                # Fetch full data from database
                item = self._fetch_item(result_type, result_id)
                
                if item:
                    guidance_results.append(GuidanceResult(
                        type=result_type,
                        arabic_text=item.arabic_text,
                        translation=item.translation,
                        citation=item.citation,
                        similarity_score=round(similarity_score, 4)
                    ))
            
            logger.info(f"Retrieved {len(guidance_results)} guidance results for query")
            return guidance_results
        
        except Exception as e:
            logger.error(f"Failed to get guidance: {e}")
            raise DatabaseException(f"Failed to retrieve guidance: {e}")
    
    def _fetch_item(self, item_type: str, item_id: int):
        """Fetch item from database by type and ID."""
        try:
            if item_type == "Quran":
                return self.db.query(QuranAyah).filter(QuranAyah.id == item_id).first()
            elif item_type == "Dua":
                return self.db.query(Dua).filter(Dua.id == item_id).first()
            elif item_type == "Hadith":
                return self.db.query(Hadith).filter(Hadith.id == item_id).first()
            return None
        except Exception as e:
            logger.error(f"Database fetch error: {e}")
            raise DatabaseException(f"Failed to fetch item: {e}")
    
    @staticmethod
    def _distance_to_similarity(distance: float) -> float:
        """
        Convert L2 distance to similarity score.
        
        Args:
            distance: L2 distance from FAISS
            
        Returns:
            Similarity score between 0 and 1
        """
        # Normalize distance to similarity (lower distance = higher similarity)
        return max(0.0, 1.0 - (distance / 2.0))
