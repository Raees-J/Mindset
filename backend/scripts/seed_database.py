"""Script to seed the database with sample Islamic texts."""
import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from sqlalchemy.orm import Session
from db.session import SessionLocal, init_db
from models.database import QuranAyah, Dua, Hadith
from services.vector_store import get_vector_store
from core.logging import setup_logging, get_logger

setup_logging()
logger = get_logger(__name__)


def seed_sample_data():
    """Seed database with sample Quran ayahs, duas, and hadiths."""
    db = SessionLocal()
    vector_store = get_vector_store()
    
    try:
        logger.info("Starting database seeding...")
        
        # Sample Quran Ayahs
        sample_ayahs = [
            {
                "surah_number": 2,
                "ayah_number": 153,
                "arabic_text": "يَا أَيُّهَا الَّذِينَ آمَنُوا اسْتَعِينُوا بِالصَّبْرِ وَالصَّلَاةِ ۚ إِنَّ اللَّهَ مَعَ الصَّابِرِينَ",
                "translation": "O you who have believed, seek help through patience and prayer. Indeed, Allah is with the patient.",
                "citation": "Quran 2:153"
            },
            {
                "surah_number": 94,
                "ayah_number": 5,
                "arabic_text": "فَإِنَّ مَعَ الْعُسْرِ يُسْرًا",
                "translation": "For indeed, with hardship [will be] ease.",
                "citation": "Quran 94:5"
            },
            {
                "surah_number": 13,
                "ayah_number": 28,
                "arabic_text": "الَّذِينَ آمَنُوا وَتَطْمَئِنُّ قُلُوبُهُم بِذِكْرِ اللَّهِ ۗ أَلَا بِذِكْرِ اللَّهِ تَطْمَئِنُّ الْقُلُوبُ",
                "translation": "Those who have believed and whose hearts are assured by the remembrance of Allah. Unquestionably, by the remembrance of Allah hearts are assured.",
                "citation": "Quran 13:28"
            },
            {
                "surah_number": 3,
                "ayah_number": 139,
                "arabic_text": "وَلَا تَهِنُوا وَلَا تَحْزَنُوا وَأَنتُمُ الْأَعْلَوْنَ إِن كُنتُم مُّؤْمِنِينَ",
                "translation": "So do not weaken and do not grieve, and you will be superior if you are [true] believers.",
                "citation": "Quran 3:139"
            }
        ]
        
        # Sample Duas
        sample_duas = [
            {
                "title": "Dua for Anxiety",
                "arabic_text": "اللَّهُمَّ إِنِّي أَعُوذُ بِكَ مِنَ الْهَمِّ وَالْحَزَنِ",
                "translation": "O Allah, I seek refuge in You from anxiety and grief.",
                "citation": "Sahih Bukhari 6369"
            },
            {
                "title": "Dua for Relief",
                "arabic_text": "لَا إِلَهَ إِلَّا أَنْتَ سُبْحَانَكَ إِنِّي كُنْتُ مِنَ الظَّالِمِينَ",
                "translation": "There is no deity except You; exalted are You. Indeed, I have been of the wrongdoers.",
                "citation": "Quran 21:87"
            },
            {
                "title": "Dua for Comfort",
                "arabic_text": "حَسْبُنَا اللَّهُ وَنِعْمَ الْوَكِيلُ",
                "translation": "Sufficient for us is Allah, and [He is] the best Disposer of affairs.",
                "citation": "Quran 3:173"
            }
        ]
        
        # Sample Hadiths
        sample_hadiths = [
            {
                "book": "Sahih Muslim",
                "hadith_number": "2999",
                "arabic_text": "عَجَبًا لِأَمْرِ الْمُؤْمِنِ إِنَّ أَمْرَهُ كُلَّهُ خَيْرٌ",
                "translation": "How wonderful is the affair of the believer, for his affairs are all good.",
                "citation": "Sahih Muslim 2999"
            },
            {
                "book": "Sahih Bukhari",
                "hadith_number": "6410",
                "arabic_text": "مَا يُصِيبُ الْمُسْلِمَ مِنْ نَصَبٍ وَلَا وَصَبٍ وَلَا هَمٍّ وَلَا حُزْنٍ وَلَا أَذًى وَلَا غَمٍّ",
                "translation": "No fatigue, nor disease, nor sorrow, nor sadness, nor hurt, nor distress befalls a Muslim.",
                "citation": "Sahih Bukhari 6410"
            }
        ]
        
        # Clear existing data
        db.query(QuranAyah).delete()
        db.query(Dua).delete()
        db.query(Hadith).delete()
        db.commit()
        logger.info("Cleared existing data")
        
        # Add Quran Ayahs
        quran_texts = []
        quran_ids = []
        for ayah_data in sample_ayahs:
            ayah = QuranAyah(**ayah_data)
            db.add(ayah)
            db.flush()
            quran_texts.append(ayah_data["translation"])
            quran_ids.append(str(ayah.id))
        
        # Add Duas
        dua_texts = []
        dua_ids = []
        for dua_data in sample_duas:
            dua = Dua(**dua_data)
            db.add(dua)
            db.flush()
            dua_texts.append(dua_data["translation"])
            dua_ids.append(str(dua.id))
        
        # Add Hadiths
        hadith_texts = []
        hadith_ids = []
        for hadith_data in sample_hadiths:
            hadith = Hadith(**hadith_data)
            db.add(hadith)
            db.flush()
            hadith_texts.append(hadith_data["translation"])
            hadith_ids.append(str(hadith.id))
        
        db.commit()
        logger.info("Database records created")
        
        # Create embeddings in vector store
        logger.info("Creating embeddings for Quran ayahs...")
        vector_store.add_texts(quran_texts, quran_ids, "quran")
        
        logger.info("Creating embeddings for Duas...")
        vector_store.add_texts(dua_texts, dua_ids, "dua")
        
        logger.info("Creating embeddings for Hadiths...")
        vector_store.add_texts(hadith_texts, hadith_ids, "hadith")
        
        logger.info("Database seeded successfully!")
        
    except Exception as e:
        logger.error(f"Seeding failed: {e}")
        db.rollback()
        raise
    finally:
        db.close()


if __name__ == "__main__":
    logger.info("Initializing database...")
    init_db()
    logger.info("Seeding data...")
    seed_sample_data()
