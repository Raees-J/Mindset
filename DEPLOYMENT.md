# Deployment Guide

Complete guide for deploying the Islamic Guidance application to production.

## 📋 Pre-Deployment Checklist

### Backend
- [ ] All tests passing
- [ ] Environment variables configured
- [ ] Database migrations completed
- [ ] Data imported (Quran + Hadiths)
- [ ] API documentation reviewed
- [ ] Error handling tested
- [ ] Logging configured

### Frontend
- [ ] Build successful (`npm run build`)
- [ ] Type checking passed (`npm run type-check`)
- [ ] No console errors
- [ ] Environment variables set
- [ ] API endpoints configured
- [ ] Responsive design tested
- [ ] Accessibility checked

## 🚀 Backend Deployment

### Option 1: Railway (Recommended)

1. **Create Account**: https://railway.app
2. **Create New Project**
3. **Add PostgreSQL**: Railway provides managed PostgreSQL
4. **Deploy Backend**:
   ```bash
   # Install Railway CLI
   npm install -g @railway/cli
   
   # Login
   railway login
   
   # Link project
   railway link
   
   # Deploy
   railway up
   ```

5. **Set Environment Variables**:
   ```
   DATABASE_URL=<railway-postgres-url>
   EMBEDDING_MODEL=all-MiniLM-L6-v2
   VECTOR_STORE_PERSIST_DIR=/app/chroma_db
   ```

6. **Import Data**:
   ```bash
   railway run python scripts/import_quran.py
   railway run python scripts/import_curated_hadith.py
   ```

### Option 2: Render

1. **Create Account**: https://render.com
2. **New Web Service**
3. **Connect Repository**
4. **Configure**:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `uvicorn app:app --host 0.0.0.0 --port $PORT`
   - **Environment**: Python 3.12

5. **Add PostgreSQL**: Render provides managed PostgreSQL
6. **Set Environment Variables**
7. **Deploy**

### Option 3: AWS (Advanced)

1. **EC2 Instance**: Ubuntu 22.04
2. **Install Dependencies**:
   ```bash
   sudo apt update
   sudo apt install python3.12 python3-pip postgresql
   ```

3. **Clone Repository**
4. **Install Requirements**
5. **Configure Nginx** as reverse proxy
6. **Use Supervisor** for process management
7. **Setup SSL** with Let's Encrypt

## 🌐 Frontend Deployment

### Option 1: Vercel (Recommended)

1. **Create Account**: https://vercel.com
2. **Import Project**: Connect GitHub repository
3. **Configure**:
   - **Framework**: Next.js
   - **Root Directory**: `frontend`
   - **Build Command**: `npm run build`
   - **Output Directory**: `.next`

4. **Environment Variables**:
   ```
   NEXT_PUBLIC_API_URL=https://your-backend-url.com
   ```

5. **Deploy**: Automatic on git push

### Option 2: Netlify

1. **Create Account**: https://netlify.com
2. **New Site from Git**
3. **Configure**:
   - **Base Directory**: `frontend`
   - **Build Command**: `npm run build`
   - **Publish Directory**: `.next`

4. **Environment Variables**: Same as Vercel
5. **Deploy**

### Option 3: Docker

```dockerfile
# frontend/Dockerfile
FROM node:18-alpine

WORKDIR /app

COPY package*.json ./
RUN npm ci --only=production

COPY . .
RUN npm run build

EXPOSE 3000

CMD ["npm", "start"]
```

Build and run:
```bash
docker build -t islamic-guidance-frontend .
docker run -p 3000:3000 -e NEXT_PUBLIC_API_URL=https://api.example.com islamic-guidance-frontend
```

## 🗄️ Database Setup

### Neon (Serverless PostgreSQL)

1. **Create Account**: https://neon.tech
2. **Create Project**
3. **Get Connection String**:
   ```
   postgresql://user:pass@ep-xxx.region.aws.neon.tech/dbname?sslmode=require
   ```

4. **Import Data**:
   ```bash
   # Set environment variable
   export DATABASE_URL="your-neon-connection-string"
   
   # Run import scripts
   python scripts/import_quran.py
   python scripts/import_curated_hadith.py
   ```

### Traditional PostgreSQL

1. **Install PostgreSQL 15+**
2. **Create Database**:
   ```sql
   CREATE DATABASE islamic_guidance;
   ```

3. **Configure Connection**:
   ```
   DATABASE_URL=postgresql://user:password@localhost:5432/islamic_guidance
   ```

4. **Import Data**: Same as above

## 🔐 Environment Variables

### Backend (.env)
```env
# Database
DATABASE_URL=postgresql://user:pass@host:5432/dbname

# AI/ML
EMBEDDING_MODEL=all-MiniLM-L6-v2
EMBEDDING_DIMENSION=384

# Vector Store
VECTOR_STORE_PERSIST_DIR=./chroma_db

# API
API_TITLE=Islamic Guidance API
API_VERSION=1.0.0

# CORS
CORS_ORIGINS=["https://your-frontend-domain.com"]
```

### Frontend (.env.local)
```env
NEXT_PUBLIC_API_URL=https://your-backend-api.com
```

## 🔧 Production Optimizations

### Backend

1. **Use Production ASGI Server**:
   ```bash
   pip install gunicorn
   gunicorn app:app -w 4 -k uvicorn.workers.UvicornWorker
   ```

2. **Enable Caching**:
   - Redis for API responses
   - CDN for static assets

3. **Database Optimization**:
   - Connection pooling (already configured)
   - Query optimization
   - Indexes on frequently queried fields

4. **Monitoring**:
   - Sentry for error tracking
   - Prometheus for metrics
   - CloudWatch/DataDog for logs

### Frontend

1. **Build Optimization**:
   ```bash
   npm run build
   ```

2. **Image Optimization**:
   - Use Next.js Image component
   - Serve WebP format

3. **CDN**:
   - Vercel Edge Network (automatic)
   - CloudFlare for custom domains

4. **Analytics**:
   - Google Analytics
   - Vercel Analytics

## 🔒 Security Checklist

- [ ] HTTPS enabled (SSL certificate)
- [ ] Environment variables secured
- [ ] Database credentials rotated
- [ ] CORS properly configured
- [ ] Rate limiting enabled
- [ ] Input validation on all endpoints
- [ ] SQL injection protection (ORM)
- [ ] XSS protection (React escaping)
- [ ] Security headers configured
- [ ] Regular dependency updates

## 📊 Monitoring

### Backend Monitoring

1. **Health Endpoint**: `/api/v1/health`
2. **Uptime Monitoring**: UptimeRobot, Pingdom
3. **Error Tracking**: Sentry
4. **Performance**: New Relic, DataDog

### Frontend Monitoring

1. **Vercel Analytics**: Built-in
2. **Google Analytics**: User behavior
3. **Sentry**: Error tracking
4. **Lighthouse CI**: Performance monitoring

## 🔄 CI/CD Pipeline

### GitHub Actions Example

```yaml
# .github/workflows/deploy.yml
name: Deploy

on:
  push:
    branches: [main]

jobs:
  backend:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Deploy to Railway
        run: railway up
        env:
          RAILWAY_TOKEN: ${{ secrets.RAILWAY_TOKEN }}

  frontend:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Deploy to Vercel
        run: vercel --prod
        env:
          VERCEL_TOKEN: ${{ secrets.VERCEL_TOKEN }}
```

## 🧪 Testing in Production

1. **Smoke Tests**:
   ```bash
   curl https://api.example.com/api/v1/health
   ```

2. **Load Testing**:
   ```bash
   # Using Apache Bench
   ab -n 1000 -c 10 https://api.example.com/api/v1/guidance
   ```

3. **End-to-End Tests**:
   - Playwright or Cypress
   - Test critical user flows

## 📈 Scaling

### Horizontal Scaling

1. **Backend**: Multiple instances behind load balancer
2. **Database**: Read replicas for queries
3. **Vector Store**: Distributed FAISS or Pinecone

### Vertical Scaling

1. **Increase server resources**
2. **Optimize database queries**
3. **Add caching layer**

## 🆘 Troubleshooting

### Backend Issues

**Problem**: Slow API responses
- **Solution**: Check database indexes, add caching

**Problem**: Out of memory
- **Solution**: Increase server RAM, optimize vector store

**Problem**: Database connection errors
- **Solution**: Check connection string, verify SSL settings

### Frontend Issues

**Problem**: Build fails
- **Solution**: Check TypeScript errors, update dependencies

**Problem**: API calls fail
- **Solution**: Verify CORS settings, check API URL

**Problem**: Slow page load
- **Solution**: Optimize images, enable CDN

## 📞 Support

For deployment issues:
1. Check logs first
2. Review error messages
3. Consult documentation
4. Open GitHub issue

## 🎉 Post-Deployment

- [ ] Test all features
- [ ] Monitor error rates
- [ ] Check performance metrics
- [ ] Verify data integrity
- [ ] Test on multiple devices
- [ ] Share with beta users
- [ ] Collect feedback
- [ ] Plan improvements

---

**Your Islamic Guidance application is now ready for production!** 🚀
