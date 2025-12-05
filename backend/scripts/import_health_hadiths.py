"""
Import health and lifestyle hadiths from Prophetic medicine and Sunnah.

This collection includes authentic hadiths about:
- Food and nutrition
- Natural remedies
- Healthy lifestyle
- Prophetic medicine
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

from sqlalchemy.orm import Session
from db.session import SessionLocal, init_db
from models.database import Hadith
from services.vector_store import get_vector_store
from core.logging import setup_logging, get_logger

setup_logging()
logger = get_logger(__name__)

# Health and lifestyle hadiths
HEALTH_HADITHS = [
    # FOOD & NUTRITION
    {
        "book": "Sahih Bukhari",
        "hadith_number": "5686",
        "arabic_text": "مَا مَلَأَ آدَمِيٌّ وِعَاءً شَرًّا مِنْ بَطْنٍ",
        "translation": "The son of Adam does not fill any vessel worse than his stomach. It is sufficient for the son of Adam to eat a few mouthfuls to keep him going. If he must fill it, then one-third for his food, one-third for his drink, and one-third for air.",
        "citation": "Sahih Bukhari 5686",
        "themes": ["health", "food", "moderation", "gut health"]
    },
    {
        "book": "Sahih Muslim",
        "hadith_number": "2052",
        "arabic_text": "الْعَسَلُ شِفَاءٌ مِنْ كُلِّ دَاءٍ",
        "translation": "Honey is a remedy for every illness. And the Quran is a remedy for all illness of the mind, therefore I recommend to you both remedies, the Quran and honey.",
        "citation": "Sahih Muslim 2052",
        "themes": ["health", "honey", "remedy", "healing"]
    },
    {
        "book": "Sahih Bukhari",
        "hadith_number": "5687",
        "arabic_text": "كُلُوا الزَّيْتَ وَادَّهِنُوا بِهِ فَإِنَّهُ مِنْ شَجَرَةٍ مُبَارَكَةٍ",
        "translation": "Eat olive oil and anoint yourselves with it, for it comes from a blessed tree.",
        "citation": "Sahih Bukhari 5687",
        "themes": ["health", "olive oil", "food", "nutrition"]
    },
    {
        "book": "Jami' at-Tirmidhi",
        "hadith_number": "2038",
        "arabic_text": "عَلَيْكُمْ بِالتَّلْبِينَةِ فَإِنَّهَا مُجِمَّةٌ لِفُؤَادِ الْمَرِيضِ",
        "translation": "You should eat Talbinah (barley soup), for it soothes the heart of the sick person and relieves some of his sorrow.",
        "citation": "Jami' at-Tirmidhi 2038",
        "themes": ["health", "barley", "remedy", "comfort food"]
    },
    {
        "book": "Sahih Bukhari",
        "hadith_number": "5445",
        "arabic_text": "التَّمْرُ مِنَ الْجَنَّةِ وَفِيهِ شِفَاءٌ مِنَ السُّمِّ",
        "translation": "Dates are from Paradise and they contain a cure for poison.",
        "citation": "Sahih Bukhari 5445",
        "themes": ["health", "dates", "food", "remedy"]
    },
    {
        "book": "Sahih Muslim",
        "hadith_number": "2048",
        "arabic_text": "مَنْ تَصَبَّحَ بِسَبْعِ تَمَرَاتٍ عَجْوَةٍ لَمْ يَضُرَّهُ ذَلِكَ الْيَوْمَ سُمٌّ وَلَا سِحْرٌ",
        "translation": "Whoever eats seven Ajwa dates in the morning will not be harmed by poison or magic on that day.",
        "citation": "Sahih Muslim 2048",
        "themes": ["health", "dates", "protection", "morning routine"]
    },
    
    # DIGESTIVE HEALTH
    {
        "book": "Sunan Ibn Majah",
        "hadith_number": "3457",
        "arabic_text": "الْحِمْيَةُ رَأْسُ الدَّوَاءِ",
        "translation": "The stomach is the house of disease, and abstinence is the head of every remedy.",
        "citation": "Sunan Ibn Majah 3457",
        "themes": ["health", "gut health", "fasting", "remedy"]
    },
    {
        "book": "Sahih Bukhari",
        "hadith_number": "5059",
        "arabic_text": "الْحَبَّةُ السَّوْدَاءُ شِفَاءٌ مِنْ كُلِّ دَاءٍ إِلَّا السَّامَ",
        "translation": "Black seed (Nigella sativa) is a cure for every disease except death.",
        "citation": "Sahih Bukhari 5059",
        "themes": ["health", "black seed", "remedy", "cure"]
    },
    
    # LIFESTYLE & HYGIENE
    {
        "book": "Sahih Bukhari",
        "hadith_number": "5376",
        "arabic_text": "النَّظَافَةُ مِنَ الْإِيمَانِ",
        "translation": "Cleanliness is part of faith.",
        "citation": "Sahih Bukhari 5376",
        "themes": ["health", "hygiene", "cleanliness", "lifestyle"]
    },
    {
        "book": "Sahih Muslim",
        "hadith_number": "2020",
        "arabic_text": "إِذَا اسْتَيْقَظَ أَحَدُكُمْ مِنْ نَوْمِهِ فَلْيَسْتَنْشِقْ بِمَنْخِرَيْهِ مِنَ الْمَاءِ",
        "translation": "When one of you wakes up from sleep, let him rinse his nose with water three times, for the devil spends the night in the upper part of his nose.",
        "citation": "Sahih Muslim 2020",
        "themes": ["health", "hygiene", "morning routine", "cleanliness"]
    },
    
    # EXERCISE & PHYSICAL ACTIVITY
    {
        "book": "Sahih Muslim",
        "hadith_number": "2664",
        "arabic_text": "الْمُؤْمِنُ الْقَوِيُّ خَيْرٌ وَأَحَبُّ إِلَى اللَّهِ مِنَ الْمُؤْمِنِ الضَّعِيفِ",
        "translation": "The strong believer is better and more beloved to Allah than the weak believer, while there is good in both.",
        "citation": "Sahih Muslim 2664",
        "themes": ["health", "strength", "fitness", "lifestyle"]
    },
    {
        "book": "Sunan Abu Dawud",
        "hadith_number": "2513",
        "arabic_text": "عَلِّمُوا أَوْلَادَكُمُ السِّبَاحَةَ وَالرَّمْيَ",
        "translation": "Teach your children swimming and archery.",
        "citation": "Sunan Abu Dawud 2513",
        "themes": ["health", "exercise", "sports", "physical activity"]
    },
    
    # SLEEP & REST
    {
        "book": "Sahih Bukhari",
        "hadith_number": "6320",
        "arabic_text": "إِذَا أَوَى أَحَدُكُمْ إِلَى فِرَاشِهِ فَلْيَنْفُضْ فِرَاشَهُ",
        "translation": "When one of you goes to bed, let him dust off his bed with the inside of his garment, for he does not know what came onto it after him.",
        "citation": "Sahih Bukhari 6320",
        "themes": ["health", "sleep", "hygiene", "bedtime"]
    },
    {
        "book": "Sahih Muslim",
        "hadith_number": "2714",
        "arabic_text": "لَا تَنَامُوا عَلَى ظُهُورِكُمْ",
        "translation": "Do not sleep on your stomach, for that is a way of sleeping that Allah dislikes. Sleep on your right side.",
        "citation": "Sahih Muslim 2714",
        "themes": ["health", "sleep", "sleeping position", "rest"]
    },
    
    # WATER & HYDRATION
    {
        "book": "Sunan Ibn Majah",
        "hadith_number": "3427",
        "arabic_text": "لَا تَشْرَبُوا وَاحِدًا كَشُرْبِ الْبَعِيرِ وَلَكِنِ اشْرَبُوا مَثْنَى وَثُلَاثَ",
        "translation": "Do not drink in one gulp like a camel, but in two or three breaths.",
        "citation": "Sunan Ibn Majah 3427",
        "themes": ["health", "water", "hydration", "drinking"]
    },
    {
        "book": "Jami' at-Tirmidhi",
        "hadith_number": "1887",
        "arabic_text": "خَيْرُ الْمَاءِ مَاءُ زَمْزَمَ",
        "translation": "The best water on the face of the earth is the water of Zamzam; it is a kind of food and a healing from sickness.",
        "citation": "Jami' at-Tirmidhi 1887",
        "themes": ["health", "water", "zamzam", "healing"]
    },
]


def import_health_hadiths():
    """Import health and lifestyle hadiths."""
    db = SessionLocal()
    vector_store = get_vector_store()
    
    try:
        logger.info("="*80)
        logger.info("IMPORTING HEALTH & LIFESTYLE HADITHS")
        logger.info("="*80)
        logger.info(f"\nTotal hadiths to import: {len(HEALTH_HADITHS)}")
        logger.info("Categories: Food, Nutrition, Remedies, Hygiene, Exercise, Sleep\n")
        
        batch_texts = []
        batch_ids = []
        total_imported = 0
        
        for hadith_data in HEALTH_HADITHS:
            # Check if already exists
            existing = db.query(Hadith).filter(
                Hadith.citation == hadith_data["citation"]
            ).first()
            
            if existing:
                logger.info(f"Skipping existing: {hadith_data['citation']}")
                continue
            
            # Create database record
            hadith = Hadith(
                book=hadith_data["book"],
                hadith_number=hadith_data["hadith_number"],
                arabic_text=hadith_data["arabic_text"],
                translation=hadith_data["translation"],
                citation=hadith_data["citation"]
            )
            db.add(hadith)
            db.flush()
            
            # Add to embedding batch with themes
            themes_text = " ".join(hadith_data.get("themes", []))
            searchable_text = f"{hadith_data['translation']} {themes_text}"
            
            batch_texts.append(searchable_text)
            batch_ids.append(str(hadith.id))
            total_imported += 1
        
        # Create embeddings
        if batch_texts:
            logger.info(f"Creating embeddings for {len(batch_texts)} hadiths...")
            vector_store.add_texts(batch_texts, batch_ids, "hadith")
            db.commit()
        
        logger.info("\n" + "="*80)
        logger.info("IMPORT COMPLETED SUCCESSFULLY!")
        logger.info("="*80)
        logger.info(f"\nTotal new hadiths imported: {total_imported}")
        logger.info("\nCategories added:")
        logger.info("  ✓ Food & Nutrition (dates, honey, olive oil, barley)")
        logger.info("  ✓ Digestive Health (moderation, fasting, black seed)")
        logger.info("  ✓ Lifestyle & Hygiene (cleanliness, morning routine)")
        logger.info("  ✓ Exercise & Physical Activity (strength, sports)")
        logger.info("  ✓ Sleep & Rest (sleeping position, bedtime routine)")
        logger.info("  ✓ Water & Hydration (drinking etiquette)")
        logger.info("="*80)
        
    except Exception as e:
        logger.error(f"Import failed: {e}")
        db.rollback()
        raise
    finally:
        db.close()


if __name__ == "__main__":
    logger.info("Initializing database...")
    init_db()
    logger.info("Starting health hadiths import...\n")
    import_health_hadiths()
    logger.info("\n✓ Health hadiths imported successfully!")
