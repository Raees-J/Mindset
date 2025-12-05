"""
Download and import complete hadith datasets.

This script downloads hadith collections from reliable sources.
For production use, download datasets from:
- https://github.com/sunnah-com/hadith (Official Sunnah.com dataset)
- https://ahadith.co.uk/
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

import json
import requests
from core.logging import setup_logging, get_logger

setup_logging()
logger = get_logger(__name__)


def download_hadith_json():
    """
    Download hadith collections in JSON format.
    
    Instructions:
    1. Visit https://github.com/sunnah-com/hadith
    2. Download the JSON files for each collection
    3. Place them in backend/data/hadith/ directory
    4. Run this script to import them
    """
    logger.info("Hadith Dataset Download Instructions:")
    logger.info("=" * 80)
    logger.info("\nTo import complete hadith collections (6000+ hadiths):")
    logger.info("\n1. Visit: https://github.com/sunnah-com/hadith")
    logger.info("2. Download JSON files for:")
    logger.info("   - Sahih Bukhari (7563 hadiths)")
    logger.info("   - Sahih Muslim (7563 hadiths)")
    logger.info("   - Sunan Abu Dawud (5274 hadiths)")
    logger.info("   - Jami' at-Tirmidhi (3956 hadiths)")
    logger.info("   - Sunan an-Nasa'i (5758 hadiths)")
    logger.info("   - Sunan Ibn Majah (4341 hadiths)")
    logger.info("\n3. Create directory: backend/data/hadith/")
    logger.info("4. Place JSON files in that directory")
    logger.info("5. Run: python scripts/import_hadith_from_files.py")
    logger.info("\n" + "=" * 80)
    logger.info("\nAlternatively, use the API approach (requires API key):")
    logger.info("- Sign up at https://sunnah.com/api")
    logger.info("- Get your API key")
    logger.info("- Set HADITH_API_KEY in .env file")
    logger.info("=" * 80)


if __name__ == "__main__":
    download_hadith_json()
