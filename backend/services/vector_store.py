"""Vector store service using FAISS."""
import faiss
import numpy as np
import pickle
import os
from typing import Optional
from sentence_transformers import SentenceTransformer

from core.config import get_settings
from core.logging import get_logger
from core.exceptions import VectorStoreException, EmbeddingException

logger = get_logger(__name__)
settings = get_settings()


class VectorStoreService:
    """Service for managing vector embeddings and similarity search."""
    
    def __init__(self):
        """Initialize vector store service."""
        try:
            self.model = SentenceTransformer(settings.embedding_model)
            self.dimension = settings.embedding_dimension
            
            # Initialize FAISS indexes
            self.quran_index = faiss.IndexFlatL2(self.dimension)
            self.dua_index = faiss.IndexFlatL2(self.dimension)
            self.hadith_index = faiss.IndexFlatL2(self.dimension)
            
            # Store metadata
            self.quran_ids: list[str] = []
            self.dua_ids: list[str] = []
            self.hadith_ids: list[str] = []
            
            # Setup persistence
            self.persist_dir = settings.vector_store_persist_dir
            os.makedirs(self.persist_dir, exist_ok=True)
            
            # Load existing indexes
            self._load_indexes()
            
            logger.info("Vector store service initialized successfully")
        except Exception as e:
            logger.error(f"Failed to initialize vector store: {e}")
            raise VectorStoreException(f"Vector store initialization failed: {e}")
    
    def _load_indexes(self) -> None:
        """Load indexes from disk if they exist."""
        try:
            collections = [
                ("quran", self.quran_index, self.quran_ids),
                ("dua", self.dua_index, self.dua_ids),
                ("hadith", self.hadith_index, self.hadith_ids)
            ]
            
            for name, index_attr, ids_list in collections:
                index_path = f"{self.persist_dir}/{name}.index"
                ids_path = f"{self.persist_dir}/{name}_ids.pkl"
                
                if os.path.exists(index_path) and os.path.exists(ids_path):
                    setattr(self, f"{name}_index", faiss.read_index(index_path))
                    with open(ids_path, 'rb') as f:
                        loaded_ids = pickle.load(f)
                        ids_list.clear()
                        ids_list.extend(loaded_ids)
                    logger.info(f"Loaded {name} index with {len(loaded_ids)} entries")
        except Exception as e:
            logger.warning(f"Could not load indexes: {e}")
    
    def _save_indexes(self) -> None:
        """Save indexes to disk."""
        try:
            collections = [
                ("quran", self.quran_index, self.quran_ids),
                ("dua", self.dua_index, self.dua_ids),
                ("hadith", self.hadith_index, self.hadith_ids)
            ]
            
            for name, index, ids in collections:
                faiss.write_index(index, f"{self.persist_dir}/{name}.index")
                with open(f"{self.persist_dir}/{name}_ids.pkl", 'wb') as f:
                    pickle.dump(ids, f)
            
            logger.info("Indexes saved successfully")
        except Exception as e:
            logger.error(f"Failed to save indexes: {e}")
            raise VectorStoreException(f"Failed to save indexes: {e}")
    
    def add_texts(
        self,
        texts: list[str],
        ids: list[str],
        collection_name: str
    ) -> None:
        """
        Add texts to the specified collection.
        
        Args:
            texts: List of text strings to embed
            ids: List of corresponding IDs
            collection_name: Name of collection (quran, dua, hadith)
        """
        try:
            if len(texts) != len(ids):
                raise ValueError("Texts and IDs must have the same length")
            
            embeddings = self.model.encode(texts)
            embeddings = np.array(embeddings).astype('float32')
            
            if collection_name == "quran":
                self.quran_index.add(embeddings)
                self.quran_ids.extend(ids)
            elif collection_name == "dua":
                self.dua_index.add(embeddings)
                self.dua_ids.extend(ids)
            elif collection_name == "hadith":
                self.hadith_index.add(embeddings)
                self.hadith_ids.extend(ids)
            else:
                raise ValueError(f"Invalid collection name: {collection_name}")
            
            self._save_indexes()
            logger.info(f"Added {len(texts)} texts to {collection_name} collection")
        except Exception as e:
            logger.error(f"Failed to add texts: {e}")
            raise EmbeddingException(f"Failed to add texts: {e}")
    
    def search_all(
        self,
        query: str,
        top_k_per_type: Optional[int] = None
    ) -> list[dict]:
        """
        Search across all collections.
        
        Args:
            query: Search query text
            top_k_per_type: Number of results per collection type
            
        Returns:
            List of search results with type, id, and distance
        """
        try:
            if top_k_per_type is None:
                top_k_per_type = settings.default_top_k_per_type
            
            query_embedding = self.model.encode([query])
            query_embedding = np.array(query_embedding).astype('float32')
            
            all_results = []
            
            # Search each collection
            collections = [
                ("Quran", self.quran_index, self.quran_ids),
                ("Dua", self.dua_index, self.dua_ids),
                ("Hadith", self.hadith_index, self.hadith_ids)
            ]
            
            for type_name, index, ids in collections:
                if index.ntotal > 0:
                    k = min(top_k_per_type, index.ntotal)
                    distances, indices = index.search(query_embedding, k)
                    
                    for i, idx in enumerate(indices[0]):
                        all_results.append({
                            'type': type_name,
                            'id': ids[idx],
                            'distance': float(distances[0][i])
                        })
            
            # Sort by distance and limit results
            all_results.sort(key=lambda x: x['distance'])
            return all_results[:settings.max_results]
        
        except Exception as e:
            logger.error(f"Search failed: {e}")
            raise VectorStoreException(f"Search failed: {e}")


# Global instance
_vector_store: Optional[VectorStoreService] = None


def get_vector_store() -> VectorStoreService:
    """Get or create vector store instance."""
    global _vector_store
    if _vector_store is None:
        _vector_store = VectorStoreService()
    return _vector_store
