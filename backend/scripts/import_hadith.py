"""Import Hadith collections from API."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

import requests
import time
from sqlalchemy.orm import Session
from db.session import SessionLocal, init_db
from models.database import Hadith
from services.vector_store import get_vector_store
from core.logging import setup_logging, get_logger

setup_logging()
logger = get_logger(__name__)

# Hadith API
HADITH_API_BASE = "https://api.sunnah.com/v1"

# Major Hadith collections to import
HADITH_COLLECTIONS = [
    {"name": "bukhari", "display": "Sahih Bukhari"},
    {"name": "muslim", "display": "Sahih Muslim"},
    {"name": "abudawud", "display": "Sunan Abu Dawud"},
    {"name": "tirmidhi", "display": "Jami' at-Tirmidhi"},
    {"name": "nasai", "display": "Sunan an-Nasa'i"},
    {"name": "ibnmajah", "display": "Sunan Ibn Majah"},
]


def fetch_hadith_collection(collection_name: str):
    """Fetch hadiths from a specific collection."""
    logger.info(f"Fetching {collection_name} collection...")
    
    # Note: This is a placeholder. You'll need an API key from sunnah.com
    # Alternative: Use hadith datasets from GitHub or other sources
    
    # For now, we'll use a public API endpoint
    url = f"https://random-hadith-generator.vercel.app/{collection_name}"
    
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            return response.json()
    except Exception as e:
        logger.warning(f"Could not fetch from API: {e}")
    
    return None


def import_hadith_from_json():
    """Import hadiths from local JSON files (recommended approach)."""
    db = SessionLocal()
    vector_store = get_vector_store()
    
    try:
        logger.info("Starting Hadith import from sample data...")
        
        # Clear existing hadith data
        db.query(Hadith).delete()
        db.commit()
        logger.info("Cleared existing Hadith data")
        
        # Sample comprehensive hadith collection
        # In production, you would load this from JSON files
        sample_hadiths = [
            # Sahih Bukhari
            {
                "book": "Sahih Bukhari",
                "hadith_number": "1",
                "arabic_text": "إِنَّمَا الأَعْمَالُ بِالنِّيَّاتِ",
                "translation": "Actions are judged by intentions, and every person will be rewarded according to their intention.",
                "citation": "Sahih Bukhari 1"
            },
            {
                "book": "Sahih Bukhari",
                "hadith_number": "6410",
                "arabic_text": "مَا يُصِيبُ الْمُسْلِمَ مِنْ نَصَبٍ وَلَا وَصَبٍ وَلَا هَمٍّ وَلَا حُزْنٍ وَلَا أَذًى وَلَا غَمٍّ",
                "translation": "No fatigue, disease, sorrow, sadness, hurt, or distress befalls a Muslim, even if it were the prick he receives from a thorn, but that Allah expiates some of his sins for that.",
                "citation": "Sahih Bukhari 6410"
            },
            {
                "book": "Sahih Bukhari",
                "hadith_number": "6502",
                "arabic_text": "الْمُؤْمِنُ الْقَوِيُّ خَيْرٌ وَأَحَبُّ إِلَى اللَّهِ مِنَ الْمُؤْمِنِ الضَّعِيفِ",
                "translation": "The strong believer is better and more beloved to Allah than the weak believer, while there is good in both.",
                "citation": "Sahih Bukhari 6502"
            },
            # Sahih Muslim
            {
                "book": "Sahih Muslim",
                "hadith_number": "2999",
                "arabic_text": "عَجَبًا لِأَمْرِ الْمُؤْمِنِ إِنَّ أَمْرَهُ كُلَّهُ خَيْرٌ",
                "translation": "How wonderful is the affair of the believer, for his affairs are all good. If something good happens to him, he is grateful, and that is good for him. If something bad happens to him, he bears it with patience, and that is good for him.",
                "citation": "Sahih Muslim 2999"
            },
            {
                "book": "Sahih Muslim",
                "hadith_number": "2564",
                "arabic_text": "مَنْ نَفَّسَ عَنْ مُؤْمِنٍ كُرْبَةً مِنْ كُرَبِ الدُّنْيَا",
                "translation": "Whoever relieves a believer of distress in this world, Allah will relieve him of distress on the Day of Resurrection.",
                "citation": "Sahih Muslim 2564"
            },
            {
                "book": "Sahih Muslim",
                "hadith_number": "2699",
                "arabic_text": "الدُّعَاءُ هُوَ الْعِبَادَةُ",
                "translation": "Supplication is worship itself.",
                "citation": "Sahih Muslim 2699"
            },
        ]
        
        # Add more comprehensive hadiths
        additional_hadiths = [
            # About patience and hardship
            {
                "book": "Sahih Bukhari",
                "hadith_number": "5645",
                "arabic_text": "مَا أَصَابَ الْمُسْلِمَ مِنْ هَمٍّ وَلَا حَزَنٍ",
                "translation": "No Muslim is afflicted with harm because of sickness or other matters, but that Allah will remove his sins as a tree sheds its leaves.",
                "citation": "Sahih Bukhari 5645"
            },
            # About gratitude
            {
                "book": "Sahih Muslim",
                "hadith_number": "2625",
                "arabic_text": "مَنْ لَمْ يَشْكُرِ النَّاسَ لَمْ يَشْكُرِ اللَّهَ",
                "translation": "Whoever does not thank people has not thanked Allah.",
                "citation": "Sahih Muslim 2625"
            },
            # About hope
            {
                "book": "Sunan Ibn Majah",
                "hadith_number": "4168",
                "arabic_text": "إِنَّ اللَّهَ يُحِبُّ الْعَبْدَ الْمُحْسِنَ",
                "translation": "Indeed, Allah loves the servant who does good.",
                "citation": "Sunan Ibn Majah 4168"
            },
            # About fear and anxiety
            {
                "book": "Sunan Abu Dawud",
                "hadith_number": "1525",
                "arabic_text": "اللَّهُمَّ إِنِّي أَعُوذُ بِكَ مِنَ الْهَمِّ وَالْحَزَنِ",
                "translation": "O Allah, I seek refuge in You from worry and grief, from incapacity and laziness.",
                "citation": "Sunan Abu Dawud 1525"
            },
            # About trust in Allah
            {
                "book": "Jami' at-Tirmidhi",
                "hadith_number": "2344",
                "arabic_text": "لَوْ أَنَّكُمْ تَوَكَّلْتُمْ عَلَى اللَّهِ حَقَّ تَوَكُّلِهِ",
                "translation": "If you were to rely upon Allah with the reliance He is due, you would be given provision like the birds: they go out hungry in the morning and return full in the evening.",
                "citation": "Jami' at-Tirmidhi 2344"
            },
            # About kindness
            {
                "book": "Sahih Muslim",
                "hadith_number": "2593",
                "arabic_text": "إِنَّ اللَّهَ رَفِيقٌ يُحِبُّ الرِّفْقَ",
                "translation": "Indeed, Allah is gentle and loves gentleness in all matters.",
                "citation": "Sahih Muslim 2593"
            },
            # About forgiveness
            {
                "book": "Sahih Bukhari",
                "hadith_number": "6307",
                "arabic_text": "مَنْ سَتَرَ مُسْلِمًا سَتَرَهُ اللَّهُ",
                "translation": "Whoever conceals the faults of a Muslim, Allah will conceal his faults in this world and the Hereafter.",
                "citation": "Sahih Bukhari 6307"
            },
            # About prayer
            {
                "book": "Sahih Muslim",
                "hadith_number": "758",
                "arabic_text": "الصَّلَاةُ نُورٌ",
                "translation": "Prayer is light, charity is proof, patience is illumination, and the Quran is an argument for or against you.",
                "citation": "Sahih Muslim 758"
            },
        ]
        
        all_hadiths = sample_hadiths + additional_hadiths
        
        batch_texts = []
        batch_ids = []
        batch_size = 50
        total_hadiths = 0
        
        for hadith_data in all_hadiths:
            hadith = Hadith(**hadith_data)
            db.add(hadith)
            db.flush()
            
            batch_texts.append(hadith_data["translation"])
            batch_ids.append(str(hadith.id))
            total_hadiths += 1
            
            if len(batch_texts) >= batch_size:
                logger.info(f"Creating embeddings for batch (total: {total_hadiths} hadiths)")
                vector_store.add_texts(batch_texts, batch_ids, "hadith")
                batch_texts = []
                batch_ids = []
        
        # Process remaining batch
        if batch_texts:
            logger.info(f"Creating embeddings for final batch")
            vector_store.add_texts(batch_texts, batch_ids, "hadith")
        
        db.commit()
        logger.info(f"Successfully imported {total_hadiths} hadiths!")
        logger.info("Note: This is a sample collection. For complete hadith collections (6000+),")
        logger.info("please download hadith datasets from sources like:")
        logger.info("- https://github.com/sunnah-com/hadith")
        logger.info("- https://ahadith.co.uk/")
        
    except Exception as e:
        logger.error(f"Import failed: {e}")
        db.rollback()
        raise
    finally:
        db.close()


if __name__ == "__main__":
    logger.info("Initializing database...")
    init_db()
    logger.info("Starting Hadith import...")
    import_hadith_from_json()
    logger.info("Hadith import completed!")
