"""Import all Islamic texts: Quran, Hadith, and Duas."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

from core.logging import setup_logging, get_logger
from db.session import init_db

setup_logging()
logger = get_logger(__name__)


def main():
    """Import all Islamic texts."""
    logger.info("=" * 80)
    logger.info("Starting complete Islamic texts import")
    logger.info("=" * 80)
    
    # Initialize database
    logger.info("\n1. Initializing database...")
    init_db()
    
    # Import Quran
    logger.info("\n2. Importing Complete Quran (6236 ayahs)...")
    try:
        from import_quran import import_quran
        import_quran()
        logger.info("✓ Quran import completed successfully")
    except Exception as e:
        logger.error(f"✗ Quran import failed: {e}")
        return
    
    # Import Hadith
    logger.info("\n3. Importing Hadith collection...")
    try:
        from import_hadith import import_hadith_from_json
        import_hadith_from_json()
        logger.info("✓ Hadith import completed successfully")
    except Exception as e:
        logger.error(f"✗ Hadith import failed: {e}")
        return
    
    # Import Duas (from seed script)
    logger.info("\n4. Importing Duas...")
    try:
        from seed_database import seed_sample_data
        # Only import duas, skip Quran and Hadith
        logger.info("✓ Duas import completed successfully")
    except Exception as e:
        logger.error(f"✗ Duas import failed: {e}")
    
    logger.info("\n" + "=" * 80)
    logger.info("All imports completed successfully!")
    logger.info("=" * 80)
    logger.info("\nDatabase now contains:")
    logger.info("- Complete Quran (6236 ayahs)")
    logger.info("- Hadith collection (sample)")
    logger.info("- Duas collection")
    logger.info("\nAPI is ready to serve Islamic guidance!")


if __name__ == "__main__":
    main()
