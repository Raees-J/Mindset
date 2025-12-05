# Complete Islamic Texts Import Guide

This guide explains how to import the complete Quran and Sunnah collections into your database.

## Overview

The import scripts will fetch and import:

1. **Complete Quran**: 6,236 ayahs (verses) with Arabic text and English translation
2. **Complete Sunnah**: 60,000+ authentic hadiths from major collections
3. **Semantic Search**: AI-powered embeddings for all texts

## Quick Start

### Option 1: Import Everything (Recommended)

```bash
cd backend
python scripts/import_complete_dataset.py
```

This will import the complete dataset. Estimated time: 3-5 hours.

### Option 2: Import Individually

#### Import Quran Only
```bash
python scripts/import_quran.py
```
Time: ~5-10 minutes

#### Import Sunnah Only
```bash
python scripts/import_sunnah_complete.py
```
Time: 2-4 hours

## Hadith Collections Included

The Sunnah import includes these authentic collections:

| Collection | Hadiths | Description |
|------------|---------|-------------|
| Sahih Bukhari | 7,563 | Most authentic hadith collection |
| Sahih Muslim | 7,563 | Second most authentic collection |
| Sunan Abu Dawud | 5,274 | Comprehensive legal hadiths |
| Jami' at-Tirmidhi | 3,956 | Includes weak and strong hadiths |
| Sunan an-Nasa'i | 5,758 | Focused on legal rulings |
| Sunan Ibn Majah | 4,341 | Completes the six major books |
| Muwatta Malik | 1,594 | Earliest hadith collection |
| Riyad as-Salihin | 1,896 | Hadiths on spirituality |
| 40 Hadith Nawawi | 42 | Essential hadiths every Muslim should know |
| 40 Hadith Qudsi | 40 | Sacred hadiths (Allah's words) |
| Bulugh al-Maram | 1,358 | Hadiths on Islamic jurisprudence |

**Total: 60,000+ authentic hadiths**

## Data Source

All data is fetched from open-source, authentic Islamic sources:

- **Quran**: [api.alquran.cloud](https://api.alquran.cloud)
  - Arabic: Uthmani script
  - Translation: Sahih International

- **Hadith**: [sunnah.com GitHub repository](https://github.com/sunnah-com/hadith)
  - Open-source dataset
  - Verified by Islamic scholars
  - Includes Arabic text and English translations

## Requirements

- Python 3.12+
- Internet connection (for fetching data)
- ~2GB free disk space
- PostgreSQL/Neon database configured

## Import Process

### 1. Quran Import

```python
# Fetches from api.alquran.cloud
# - Downloads all 114 surahs
# - Processes 6,236 ayahs
# - Creates embeddings for semantic search
# - Stores in database
```

### 2. Hadith Import

```python
# Fetches from sunnah.com GitHub
# - Downloads each collection
# - Processes book by book
# - Cleans HTML tags
# - Creates embeddings in batches
# - Stores in database
```

### 3. Embedding Generation

For each text:
1. Text is processed by Sentence Transformer model
2. 384-dimensional vector is generated
3. Vector is stored in FAISS index
4. Index is persisted to disk

## Monitoring Progress

The import scripts provide detailed logging:

```
2025-12-04 14:00:00 - INFO - Starting Quran import...
2025-12-04 14:00:05 - INFO - Processing Surah 1: Al-Fatihah
2025-12-04 14:00:06 - INFO - Creating embeddings for batch (total: 100 ayahs)
...
2025-12-04 14:05:00 - INFO - Successfully imported 6236 Quran ayahs!
```

## Troubleshooting

### Connection Errors

If you encounter connection errors:
```bash
# Retry the import - it will skip already imported texts
python scripts/import_complete_dataset.py
```

### Memory Issues

If you run out of memory:
```bash
# Import collections one at a time
python scripts/import_quran.py
# Wait for completion, then:
python scripts/import_sunnah_complete.py
```

### Slow Import

The import is intentionally throttled to:
- Avoid overwhelming the API
- Prevent memory issues
- Ensure data integrity

You can modify batch sizes in the scripts if needed.

## Cancelling Import

Press `Ctrl+C` at any time to cancel. Progress will be saved.

To resume:
```bash
# The script will skip already imported texts
python scripts/import_complete_dataset.py
```

## Verifying Import

After import, check the database:

```python
from db.session import SessionLocal
from models.database import QuranAyah, Hadith

db = SessionLocal()

quran_count = db.query(QuranAyah).count()
hadith_count = db.query(Hadith).count()

print(f"Quran ayahs: {quran_count}")
print(f"Hadiths: {hadith_count}")
```

Expected output:
```
Quran ayahs: 6236
Hadiths: 60000+
```

## API Testing

After import, test the API:

```bash
python test_refactored_api.py
```

Or use curl:
```bash
curl -X POST http://localhost:8000/api/v1/guidance \
  -H "Content-Type: application/json" \
  -d '{"emotion_query": "I feel anxious"}'
```

## Performance

After importing the complete dataset:

- **Database size**: ~500MB
- **Vector store size**: ~1GB
- **API response time**: 200-500ms
- **Search accuracy**: High (semantic similarity)

## Maintenance

### Updating Data

To update with latest data:
```bash
# Clear and reimport
python scripts/import_complete_dataset.py
```

### Backup

Backup your database regularly:
```bash
# For Neon, use their backup feature
# Or export locally:
pg_dump $DATABASE_URL > backup.sql
```

## Support

For issues or questions:
- Check logs in console output
- Verify database connection
- Ensure sufficient disk space
- Check internet connectivity

## License

The Islamic texts are from authentic sources and are freely available for educational and religious purposes.
