# Islamic Guidance - AI-Powered Spiritual Support

A modern web application that provides personalized Islamic guidance based on emotional states using semantic search powered by AI.

## 🌟 Features

- **Semantic Search**: AI-powered search through 6,000+ Islamic texts
- **Complete Quran**: All 6,236 ayahs with Arabic text and English translations
- **Authentic Hadiths**: Curated collection from Sahih Bukhari, Sahih Muslim, and more
- **Emotional Categorization**: Texts organized by emotional themes
- **Beautiful UI**: Modern, responsive design with smooth animations
- **Real-time Results**: Fast semantic matching (< 5 seconds)
- **Accessibility**: WCAG 2.1 AA compliant

## 🏗️ Architecture

### Backend (Python/FastAPI)
- **Framework**: FastAPI with async support
- **AI/ML**: Sentence Transformers (all-MiniLM-L6-v2)
- **Vector Search**: FAISS for fast similarity search
- **Database**: Neon PostgreSQL (serverless)
- **Architecture**: Clean architecture with dependency injection

### Frontend (Next.js/React)
- **Framework**: Next.js 14 with App Router
- **UI**: Aceternity UI components + Tailwind CSS
- **Animations**: Framer Motion
- **Type Safety**: Full TypeScript support
- **State Management**: Custom hooks

## 🚀 Quick Start

### Prerequisites
- Python 3.12+
- Node.js 18+
- PostgreSQL (or Neon account)

### Backend Setup

```bash
cd backend

# Install dependencies
pip install -r requirements.txt

# Configure environment
cp .env.example .env
# Edit .env with your Neon database URL

# Import data
python scripts/import_quran.py
python scripts/import_curated_hadith.py

# Start server
uvicorn app:app --reload
```

Backend will be available at http://localhost:8000

### Frontend Setup

```bash
cd frontend

# Install dependencies
npm install

# Start development server
npm run dev
```

Frontend will be available at http://localhost:3000

## 📊 Data Sources

### Quran
- **Source**: api.alquran.cloud
- **Translation**: Sahih International
- **Total**: 6,236 ayahs across 114 surahs

### Hadith
- **Collections**: Sahih Bukhari, Sahih Muslim, Jami' at-Tirmidhi, Sunan Abu Dawud
- **Categorization**: Organized by emotional themes
- **Authenticity**: All from verified authentic sources

## 🎨 UI Components

### Vanishing Input
Beautiful animated search input from Aceternity UI with:
- Rotating placeholder text
- Smooth vanishing animation on submit
- Responsive design

### Guidance Cards
Color-coded result cards showing:
- Arabic text with proper font (Amiri)
- English translation
- Source citation
- Similarity score

## 🔧 Technology Stack

### Backend
- FastAPI 0.104.1
- Sentence Transformers 5.1.2
- FAISS 1.13.0
- SQLAlchemy 2.0.23
- Pydantic 2.5.0
- PostgreSQL (Neon)

### Frontend
- Next.js 14.0.4
- React 18
- TypeScript 5
- Tailwind CSS 3.3
- Framer Motion 10.16
- Axios 1.6.2

## 📁 Project Structure

```
islamic-guidance/
├── backend/
│   ├── api/              # API routes
│   ├── core/             # Core functionality
│   ├── db/               # Database layer
│   ├── models/           # Data models
│   ├── services/         # Business logic
│   ├── scripts/          # Data import scripts
│   └── app.py            # Main application
│
├── frontend/
│   ├── app/              # Next.js pages
│   ├── components/       # React components
│   ├── hooks/            # Custom hooks
│   ├── lib/              # Utilities
│   └── public/           # Static assets
│
└── README.md
```

## 🧪 Testing

### Backend
```bash
cd backend
python test_refactored_api.py
```

### Frontend
```bash
cd frontend
npm run type-check
npm run lint
```

## 📖 API Documentation

### POST /api/v1/guidance
Get Islamic guidance based on emotional query.

**Request:**
```json
{
  "emotion_query": "I feel anxious and need comfort"
}
```

**Response:**
```json
{
  "results": [
    {
      "type": "Quran",
      "arabic_text": "...",
      "translation": "...",
      "citation": "Quran 2:153",
      "similarity_score": 0.8542
    }
  ],
  "query": "I feel anxious and need comfort",
  "total_results": 5
}
```

### GET /api/v1/health
Health check endpoint.

**Response:**
```json
{
  "status": "healthy",
  "version": "1.0.0",
  "database": "healthy",
  "vector_store": "healthy"
}
```

## 🎯 Best Practices

### Backend
- ✅ Clean architecture with separation of concerns
- ✅ Dependency injection
- ✅ Comprehensive error handling
- ✅ Structured logging
- ✅ Type hints throughout
- ✅ Connection pooling
- ✅ Environment-based configuration

### Frontend
- ✅ Component composition
- ✅ Custom hooks for logic
- ✅ Error boundaries
- ✅ TypeScript for type safety
- ✅ Accessibility (ARIA labels, semantic HTML)
- ✅ Performance optimization (memoization)
- ✅ Responsive design

## 🔒 Security

- Input validation on client and server
- SQL injection protection (SQLAlchemy ORM)
- XSS protection (React escaping)
- CORS configuration
- Environment variable protection
- HTTPS ready for production

## 🚀 Deployment

### Backend
- **Recommended**: Railway, Render, or AWS
- **Requirements**: Python 3.12+, PostgreSQL
- **Environment**: Set DATABASE_URL

### Frontend
- **Recommended**: Vercel (Next.js creators)
- **Alternative**: Netlify, AWS Amplify
- **Environment**: Set NEXT_PUBLIC_API_URL

## 📈 Performance

- **API Response Time**: 2-5 seconds
- **Semantic Search**: < 300ms
- **Database Queries**: Optimized with indexes
- **Frontend**: Lighthouse score > 90

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📝 License

This project is for educational and religious purposes.

## 🙏 Acknowledgments

- **Quran Data**: api.alquran.cloud
- **Hadith Data**: Sunnah.com
- **UI Components**: Aceternity UI
- **AI Model**: Sentence Transformers

## 📧 Support

For issues or questions, please open an issue on GitHub.

## 🌙 Islamic Authenticity

All Islamic texts are from verified authentic sources:
- Quran: Sahih International translation
- Hadiths: Sahih Bukhari, Sahih Muslim, and other authentic collections
- Duas: From authentic sources with proper citations

---

**Built with ❤️ to help Muslims find peace through authentic Islamic guidance**
