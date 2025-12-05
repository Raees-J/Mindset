"""SQLAlchemy database models."""
from sqlalchemy import Column, Integer, String, Text, Index
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class QuranAyah(Base):
    """Quran verse model."""
    
    __tablename__ = "quran_ayahs"
    
    id = Column(Integer, primary_key=True, index=True)
    surah_number = Column(Integer, nullable=False)
    ayah_number = Column(Integer, nullable=False)
    arabic_text = Column(Text, nullable=False)
    translation = Column(Text, nullable=False)
    citation = Column(String(100), nullable=False, unique=True)
    
    __table_args__ = (
        Index('idx_surah_ayah', 'surah_number', 'ayah_number'),
    )


class Dua(Base):
    """Islamic supplication model."""
    
    __tablename__ = "duas"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False)
    arabic_text = Column(Text, nullable=False)
    translation = Column(Text, nullable=False)
    citation = Column(String(200), nullable=False)


class Hadith(Base):
    """Hadith (Prophet's saying) model."""
    
    __tablename__ = "hadiths"
    
    id = Column(Integer, primary_key=True, index=True)
    book = Column(String(100), nullable=False)
    hadith_number = Column(String(50), nullable=False)
    arabic_text = Column(Text, nullable=False)
    translation = Column(Text, nullable=False)
    citation = Column(String(200), nullable=False, unique=True)
    
    __table_args__ = (
        Index('idx_book_number', 'book', 'hadith_number'),
    )
