"""Import complete Quran from API."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

import requests
from sqlalchemy.orm import Session
from db.session import SessionLocal, init_db
from models.database import QuranAyah
from services.vector_store import get_vector_store
from core.logging import setup_logging, get_logger

setup_logging()
logger = get_logger(__name__)

# API endpoints for Quran data
QURAN_API_BASE = "https://api.alquran.cloud/v1"


def fetch_quran_data():
    """Fetch complete Quran with Arabic and English translation."""
    logger.info("Fetching Quran data from API...")
    
    # Fetch Arabic text
    arabic_response = requests.get(f"{QURAN_API_BASE}/quran/quran-uthmani")
    arabic_data = arabic_response.json()
    
    # Fetch English translation (Sahih International)
    english_response = requests.get(f"{QURAN_API_BASE}/quran/en.sahih")
    english_data = english_response.json()
    
    if arabic_data['code'] != 200 or english_data['code'] != 200:
        raise Exception("Failed to fetch Quran data")
    
    logger.info("Successfully fetched Quran data")
    return arabic_data['data']['surahs'], english_data['data']['surahs']


def import_quran():
    """Import complete Quran into database."""
    db = SessionLocal()
    vector_store = get_vector_store()
    
    try:
        logger.info("Starting Quran import...")
        
        # Fetch data
        arabic_surahs, english_surahs = fetch_quran_data()
        
        # Clear existing Quran data
        db.query(QuranAyah).delete()
        db.commit()
        logger.info("Cleared existing Quran data")
        
        total_ayahs = 0
        batch_texts = []
        batch_ids = []
        batch_size = 100
        
        # Process each surah
        for arabic_surah, english_surah in zip(arabic_surahs, english_surahs):
            surah_number = arabic_surah['number']
            logger.info(f"Processing Surah {surah_number}: {english_surah['englishName']}")
            
            # Process each ayah
            for arabic_ayah, english_ayah in zip(arabic_surah['ayahs'], english_surah['ayahs']):
                ayah_number = arabic_ayah['numberInSurah']
                
                # Create database record
                ayah = QuranAyah(
                    surah_number=surah_number,
                    ayah_number=ayah_number,
                    arabic_text=arabic_ayah['text'],
                    translation=english_ayah['text'],
                    citation=f"Quran {surah_number}:{ayah_number}"
                )
                db.add(ayah)
                db.flush()
                
                # Add to batch for embeddings
                batch_texts.append(english_ayah['text'])
                batch_ids.append(str(ayah.id))
                total_ayahs += 1
                
                # Process batch when it reaches batch_size
                if len(batch_texts) >= batch_size:
                    logger.info(f"Creating embeddings for batch (total: {total_ayahs} ayahs)")
                    vector_store.add_texts(batch_texts, batch_ids, "quran")
                    batch_texts = []
                    batch_ids = []
        
        # Process remaining batch
        if batch_texts:
            logger.info(f"Creating embeddings for final batch")
            vector_store.add_texts(batch_texts, batch_ids, "quran")
        
        db.commit()
        logger.info(f"Successfully imported {total_ayahs} Quran ayahs!")
        
    except Exception as e:
        logger.error(f"Import failed: {e}")
        db.rollback()
        raise
    finally:
        db.close()


if __name__ == "__main__":
    logger.info("Initializing database...")
    init_db()
    logger.info("Starting Quran import...")
    import_quran()
    logger.info("Quran import completed!")
