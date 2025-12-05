"""
Import curated hadith collection organized by emotional themes.

This collection focuses on authentic hadiths from major collections
(Sahih Bukhari, Sahih Muslim, etc.) categorized by emotional states
to provide relevant guidance for users.

Categories:
- Anxiety & Worry
- Sadness & Depression  
- Gratitude & Thankfulness
- Hope & Optimism
- Fear & Tawakkul (Trust in Allah)
- Patience & Perseverance
- Comfort & Peace
- Forgiveness & Repentance
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


# Curated authentic hadiths organized by emotional themes
CURATED_HADITHS = [
    # ANXIETY & WORRY
    {
        "book": "Sahih Bukhari",
        "hadith_number": "6369",
        "arabic_text": "اللَّهُمَّ إِنِّي أَعُوذُ بِكَ مِنَ الْهَمِّ وَالْحَزَنِ، وَالْعَجْزِ وَالْكَسَلِ",
        "translation": "O Allah, I seek refuge in You from worry and grief, from helplessness and laziness, from cowardice and miserliness, and from being overcome by debt and from being overpowered by men.",
        "citation": "Sahih Bukhari 6369",
        "themes": ["anxiety", "worry", "dua", "protection"]
    },
    {
        "book": "Sunan Abu Dawud",
        "hadith_number": "1525",
        "arabic_text": "اللَّهُمَّ رَحْمَتَكَ أَرْجُو فَلَا تَكِلْنِي إِلَى نَفْسِي طَرْفَةَ عَيْنٍ",
        "translation": "O Allah, it is Your mercy that I hope for, so do not leave me in charge of my affairs even for a blink of an eye and rectify for me all of my affairs. None has the right to be worshipped except You.",
        "citation": "Sunan Abu Dawud 1525",
        "themes": ["anxiety", "hope", "dua", "trust"]
    },
    {
        "book": "Jami' at-Tirmidhi",
        "hadith_number": "3505",
        "arabic_text": "مَا أَصَابَ عَبْدًا هَمٌّ وَلَا حَزَنٌ فَقَالَ اللَّهُمَّ إِنِّي عَبْدُكَ",
        "translation": "No worries or grief afflict a servant who says: 'O Allah, I am Your servant, son of Your servant, son of Your maidservant; my forelock is in Your hand, Your command over me is forever executed and Your decree over me is just. I ask You by every name belonging to You which You have named Yourself with, or revealed in Your Book, or You taught to any of Your creation, or You have preserved in the knowledge of the Unseen with You, that You make the Quran the life of my heart and the light of my breast, and a departure for my sorrow and a release for my anxiety' - except that Allah will take away his worries and grief, and replace them with joy.",
        "citation": "Jami' at-Tirmidhi 3505",
        "themes": ["anxiety", "worry", "dua", "comfort"]
    },
    
    # SADNESS & DEPRESSION
    {
        "book": "Sahih Bukhari",
        "hadith_number": "5645",
        "arabic_text": "مَا يُصِيبُ الْمُسْلِمَ مِنْ نَصَبٍ وَلَا وَصَبٍ وَلَا هَمٍّ وَلَا حُزْنٍ وَلَا أَذًى وَلَا غَمٍّ",
        "translation": "No fatigue, nor disease, nor sorrow, nor sadness, nor hurt, nor distress befalls a Muslim, even if it were the prick he receives from a thorn, but that Allah expiates some of his sins for that.",
        "citation": "Sahih Bukhari 5645",
        "themes": ["sadness", "patience", "reward", "comfort"]
    },
    {
        "book": "Sahih Muslim",
        "hadith_number": "2999",
        "arabic_text": "عَجَبًا لِأَمْرِ الْمُؤْمِنِ إِنَّ أَمْرَهُ كُلَّهُ خَيْرٌ",
        "translation": "How wonderful is the affair of the believer, for his affairs are all good. If something good happens to him, he is grateful to Allah and that is good for him. If something bad happens to him, he bears it with patience and that is good for him. And this is only for the believer.",
        "citation": "Sahih Muslim 2999",
        "themes": ["sadness", "patience", "gratitude", "optimism"]
    },
    {
        "book": "Sahih Bukhari",
        "hadith_number": "5641",
        "arabic_text": "إِنَّ عِظَمَ الْجَزَاءِ مَعَ عِظَمِ الْبَلَاءِ",
        "translation": "Indeed, the magnitude of the reward goes along with the magnitude of the affliction. When Allah loves a people, He tests them, and whoever is content, then for him is contentment, and whoever is discontent, then for him is discontent.",
        "citation": "Sahih Bukhari 5641",
        "themes": ["sadness", "patience", "test", "reward"]
    },
    
    # GRATITUDE & THANKFULNESS
    {
        "book": "Sahih Muslim",
        "hadith_number": "2625",
        "arabic_text": "مَنْ لَمْ يَشْكُرِ النَّاسَ لَمْ يَشْكُرِ اللَّهَ",
        "translation": "Whoever does not thank people has not thanked Allah.",
        "citation": "Sahih Muslim 2625",
        "themes": ["gratitude", "thankfulness", "manners"]
    },
    {
        "book": "Jami' at-Tirmidhi",
        "hadith_number": "2035",
        "arabic_text": "مَنْ أَصْبَحَ مِنْكُمْ آمِنًا فِي سِرْبِهِ مُعَافًى فِي جَسَدِهِ",
        "translation": "Whoever among you wakes up secure in his property, healthy in his body, and has his food for the day, it is as if the whole world has been gathered for him.",
        "citation": "Jami' at-Tirmidhi 2035",
        "themes": ["gratitude", "contentment", "blessings"]
    },
    
    # HOPE & OPTIMISM
    {
        "book": "Sahih Muslim",
        "hadith_number": "2675",
        "arabic_text": "إِنَّ اللَّهَ يُحِبُّ الْعَبْدَ الْمُحْسِنَ الْخَفِيَّ التَّقِيَّ",
        "translation": "Indeed, Allah loves the servant who is pious, independent of means and unnoticed.",
        "citation": "Sahih Muslim 2675",
        "themes": ["hope", "love", "piety"]
    },
    {
        "book": "Sahih Bukhari",
        "hadith_number": "7405",
        "arabic_text": "يَقُولُ اللَّهُ تَعَالَى أَنَا عِنْدَ ظَنِّ عَبْدِي بِي",
        "translation": "Allah the Almighty said: I am as My servant thinks I am. I am with him when he makes mention of Me.",
        "citation": "Sahih Bukhari 7405",
        "themes": ["hope", "optimism", "trust", "dua"]
    },
    {
        "book": "Sahih Muslim",
        "hadith_number": "2687",
        "arabic_text": "لَا يَزَالُ الْبَلَاءُ بِالْمُؤْمِنِ وَالْمُؤْمِنَةِ",
        "translation": "Trials will continue to befall the believing man and woman, with regard to themselves, their children and their property, until they meet Allah with no sin on them.",
        "citation": "Sahih Muslim 2687",
        "themes": ["hope", "patience", "purification"]
    },
    
    # FEAR & TAWAKKUL (Trust in Allah)
    {
        "book": "Jami' at-Tirmidhi",
        "hadith_number": "2344",
        "arabic_text": "لَوْ أَنَّكُمْ تَوَكَّلْتُمْ عَلَى اللَّهِ حَقَّ تَوَكُّلِهِ",
        "translation": "If you were to rely upon Allah with the reliance He is due, you would be given provision like the birds: they go out hungry in the morning and return full in the evening.",
        "citation": "Jami' at-Tirmidhi 2344",
        "themes": ["trust", "tawakkul", "provision", "fear"]
    },
    {
        "book": "Sahih Bukhari",
        "hadith_number": "6502",
        "arabic_text": "الْمُؤْمِنُ الْقَوِيُّ خَيْرٌ وَأَحَبُّ إِلَى اللَّهِ مِنَ الْمُؤْمِنِ الضَّعِيفِ",
        "translation": "The strong believer is better and more beloved to Allah than the weak believer, while there is good in both. Strive for that which will benefit you, seek the help of Allah, and do not feel helpless.",
        "citation": "Sahih Bukhari 6502",
        "themes": ["strength", "trust", "determination"]
    },
    
    # PATIENCE & PERSEVERANCE
    {
        "book": "Sahih Muslim",
        "hadith_number": "918",
        "arabic_text": "وَمَا أُعْطِيَ أَحَدٌ عَطَاءً خَيْرًا وَأَوْسَعَ مِنَ الصَّبْرِ",
        "translation": "No one is given a gift better and more comprehensive than patience.",
        "citation": "Sahih Muslim 918",
        "themes": ["patience", "perseverance", "gift"]
    },
    {
        "book": "Sahih Bukhari",
        "hadith_number": "1469",
        "arabic_text": "مَنْ يَسْتَعْفِفْ يُعِفَّهُ اللَّهُ وَمَنْ يَسْتَغْنِ يُغْنِهِ اللَّهُ",
        "translation": "Whoever seeks to be chaste, Allah will make him chaste, and whoever seeks to be independent, Allah will make him independent, and whoever is patient, Allah will give him patience.",
        "citation": "Sahih Bukhari 1469",
        "themes": ["patience", "perseverance", "self-control"]
    },
    
    # COMFORT & PEACE
    {
        "book": "Sahih Muslim",
        "hadith_number": "2593",
        "arabic_text": "إِنَّ اللَّهَ رَفِيقٌ يُحِبُّ الرِّفْقَ فِي الْأَمْرِ كُلِّهِ",
        "translation": "Indeed, Allah is gentle and loves gentleness in all matters.",
        "citation": "Sahih Muslim 2593",
        "themes": ["comfort", "peace", "gentleness", "kindness"]
    },
    {
        "book": "Sahih Muslim",
        "hadith_number": "758",
        "arabic_text": "الصَّلَاةُ نُورٌ وَالصَّدَقَةُ بُرْهَانٌ",
        "translation": "Prayer is light, charity is proof, patience is illumination, and the Quran is an argument for or against you.",
        "citation": "Sahih Muslim 758",
        "themes": ["comfort", "peace", "prayer", "guidance"]
    },
    {
        "book": "Sahih Bukhari",
        "hadith_number": "6407",
        "arabic_text": "أَلَا أُخْبِرُكُمْ بِأَهْلِ الْجَنَّةِ كُلُّ ضَعِيفٍ مُتَضَعِّفٍ",
        "translation": "Shall I not inform you about the people of Paradise? They comprise every obscure unimportant humble person, and if he takes Allah's Oath that he will do that thing, Allah will fulfill his oath.",
        "citation": "Sahih Bukhari 6407",
        "themes": ["comfort", "humility", "paradise"]
    },
    
    # FORGIVENESS & REPENTANCE
    {
        "book": "Sahih Bukhari",
        "hadith_number": "6307",
        "arabic_text": "مَنْ سَتَرَ مُسْلِمًا سَتَرَهُ اللَّهُ يَوْمَ الْقِيَامَةِ",
        "translation": "Whoever conceals the faults of a Muslim, Allah will conceal his faults in this world and the Hereafter.",
        "citation": "Sahih Bukhari 6307",
        "themes": ["forgiveness", "mercy", "kindness"]
    },
    {
        "book": "Sahih Muslim",
        "hadith_number": "2702",
        "arabic_text": "إِنَّ اللَّهَ يَبْسُطُ يَدَهُ بِاللَّيْلِ لِيَتُوبَ مُسِيءُ النَّهَارِ",
        "translation": "Indeed, Allah extends His Hand during the night so that the sinners of the day may repent, and He extends His Hand during the day so that the sinners of the night may repent.",
        "citation": "Sahih Muslim 2702",
        "themes": ["forgiveness", "repentance", "mercy"]
    },
    {
        "book": "Jami' at-Tirmidhi",
        "hadith_number": "3540",
        "arabic_text": "التَّائِبُ مِنَ الذَّنْبِ كَمَنْ لَا ذَنْبَ لَهُ",
        "translation": "The one who repents from sin is like one who has no sin.",
        "citation": "Jami' at-Tirmidhi 3540",
        "themes": ["forgiveness", "repentance", "hope"]
    },
    
    # GENERAL WISDOM & GUIDANCE
    {
        "book": "Sahih Bukhari",
        "hadith_number": "1",
        "arabic_text": "إِنَّمَا الْأَعْمَالُ بِالنِّيَّاتِ",
        "translation": "Actions are judged by intentions, so each man will have what he intended.",
        "citation": "Sahih Bukhari 1",
        "themes": ["wisdom", "intention", "guidance"]
    },
    {
        "book": "Sahih Muslim",
        "hadith_number": "2564",
        "arabic_text": "مَنْ نَفَّسَ عَنْ مُؤْمِنٍ كُرْبَةً مِنْ كُرَبِ الدُّنْيَا",
        "translation": "Whoever relieves a believer of distress in this world, Allah will relieve him of distress on the Day of Resurrection.",
        "citation": "Sahih Muslim 2564",
        "themes": ["kindness", "help", "reward"]
    },
    {
        "book": "40 Hadith Nawawi",
        "hadith_number": "13",
        "arabic_text": "لَا يُؤْمِنُ أَحَدُكُمْ حَتَّى يُحِبَّ لِأَخِيهِ مَا يُحِبُّ لِنَفْسِهِ",
        "translation": "None of you truly believes until he loves for his brother what he loves for himself.",
        "citation": "40 Hadith Nawawi 13",
        "themes": ["love", "brotherhood", "faith"]
    },
    {
        "book": "Sahih Muslim",
        "hadith_number": "2699",
        "arabic_text": "الدُّعَاءُ هُوَ الْعِبَادَةُ",
        "translation": "Supplication is worship itself.",
        "citation": "Sahih Muslim 2699",
        "themes": ["dua", "worship", "prayer"]
    },
]


def import_curated_hadiths():
    """Import curated hadith collection with emotional categorization."""
    db = SessionLocal()
    vector_store = get_vector_store()
    
    try:
        logger.info("="*80)
        logger.info("IMPORTING CURATED HADITH COLLECTION")
        logger.info("="*80)
        logger.info(f"\nTotal hadiths to import: {len(CURATED_HADITHS)}")
        logger.info("Organized by emotional themes for semantic search\n")
        
        # Clear existing hadith data
        logger.info("Clearing existing hadith data...")
        db.query(Hadith).delete()
        db.commit()
        logger.info("✓ Cleared existing data\n")
        
        batch_texts = []
        batch_ids = []
        batch_size = 50
        total_imported = 0
        
        for hadith_data in CURATED_HADITHS:
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
            
            # Add to embedding batch
            # Include themes in the text for better semantic matching
            themes_text = " ".join(hadith_data.get("themes", []))
            searchable_text = f"{hadith_data['translation']} {themes_text}"
            
            batch_texts.append(searchable_text)
            batch_ids.append(str(hadith.id))
            total_imported += 1
            
            # Process batch
            if len(batch_texts) >= batch_size:
                logger.info(f"Creating embeddings... (total: {total_imported})")
                vector_store.add_texts(batch_texts, batch_ids, "hadith")
                db.commit()
                batch_texts = []
                batch_ids = []
        
        # Process remaining batch
        if batch_texts:
            logger.info(f"Creating final embeddings...")
            vector_store.add_texts(batch_texts, batch_ids, "hadith")
            db.commit()
        
        logger.info("\n" + "="*80)
        logger.info("IMPORT COMPLETED SUCCESSFULLY!")
        logger.info("="*80)
        logger.info(f"\nTotal hadiths imported: {total_imported}")
        logger.info("\nEmotional categories covered:")
        logger.info("  ✓ Anxiety & Worry")
        logger.info("  ✓ Sadness & Depression")
        logger.info("  ✓ Gratitude & Thankfulness")
        logger.info("  ✓ Hope & Optimism")
        logger.info("  ✓ Fear & Trust (Tawakkul)")
        logger.info("  ✓ Patience & Perseverance")
        logger.info("  ✓ Comfort & Peace")
        logger.info("  ✓ Forgiveness & Repentance")
        logger.info("\nAll hadiths are from authentic sources:")
        logger.info("  - Sahih Bukhari")
        logger.info("  - Sahih Muslim")
        logger.info("  - Jami' at-Tirmidhi")
        logger.info("  - Sunan Abu Dawud")
        logger.info("  - 40 Hadith Nawawi")
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
    logger.info("Starting curated hadith import...\n")
    import_curated_hadiths()
    logger.info("\n✓ Curated hadith collection imported successfully!")
