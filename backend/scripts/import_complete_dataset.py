"""
Master import script for complete Islamic texts dataset.

This script imports:
1. Complete Quran (6,236 ayahs)
2. Complete Sunnah collections (60,000+ hadiths)
3. Duas collection

Total: 66,000+ Islamic texts with semantic search
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

import time
from core.logging import setup_logging, get_logger
from db.session import init_db

setup_logging()
logger = get_logger(__name__)


def main():
    """Import complete Islamic texts dataset."""
    logger.info("="*80)
    logger.info("COMPLETE ISLAMIC TEXTS IMPORT")
    logger.info("="*80)
    logger.info("\nThis will import:")
    logger.info("  1. Complete Quran (6,236 ayahs)")
    logger.info("  2. Complete Sunnah collections (60,000+ hadiths)")
    logger.info("  3. Duas collection")
    logger.info("\nTotal: ~66,000 Islamic texts")
    logger.info("Estimated time: 3-5 hours")
    logger.info("\nPress Ctrl+C to cancel at any time")
    logger.info("="*80)
    
    input("\nPress Enter to continue...")
    
    start_time = time.time()
    
    # Initialize database
    logger.info("\n[1/3] Initializing database...")
    init_db()
    logger.info("✓ Database initialized\n")
    
    # Import Quran
    logger.info("[2/3] Importing Complete Quran...")
    logger.info("-"*80)
    try:
        from import_quran import import_quran
        import_quran()
        logger.info("✓ Quran import completed\n")
    except Exception as e:
        logger.error(f"✗ Quran import failed: {e}")
        return
    
    # Import Sunnah
    logger.info("[3/3] Importing Complete Sunnah Collections...")
    logger.info("-"*80)
    try:
        from import_sunnah_complete import import_all_sunnah
        import_all_sunnah()
        logger.info("✓ Sunnah import completed\n")
    except KeyboardInterrupt:
        logger.info("\n\nImport cancelled by user")
        logger.info("Partial data has been saved")
        return
    except Exception as e:
        logger.error(f"✗ Sunnah import failed: {e}")
        return
    
    elapsed = time.time() - start_time
    hours = int(elapsed // 3600)
    minutes = int((elapsed % 3600) // 60)
    
    logger.info("\n" + "="*80)
    logger.info("ALL IMPORTS COMPLETED SUCCESSFULLY!")
    logger.info("="*80)
    logger.info(f"\nTime taken: {hours}h {minutes}m")
    logger.info("\nYour database now contains:")
    logger.info("  ✓ Complete Quran (6,236 ayahs)")
    logger.info("  ✓ Complete Sunnah collections (60,000+ hadiths)")
    logger.info("  ✓ Semantic search enabled for all texts")
    logger.info("\nThe API is ready to serve comprehensive Islamic guidance!")
    logger.info("="*80)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        logger.info("\n\nImport cancelled by user")
    except Exception as e:
        logger.error(f"\n\nImport failed: {e}")
        raise
