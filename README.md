# 📊 Campaign Analytics Dashboard

> A full-stack web application for monitoring and analyzing marketing campaign performance.

[![FastAPI](https://img.shields.io/badge/FastAPI-0.104.1-009688.svg?style=flat&logo=FastAPI)](https://fastapi.tiangolo.com)
[![Next.js](https://img.shields.io/badge/Next.js-14.2.0-black?style=flat&logo=next.js)](https://nextjs.org/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15-316192.svg?style=flat&logo=postgresql)](https://www.postgresql.org/)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

## 🚀 Live Demo

- **Frontend:** [https://your-app.vercel.app](https://your-app.vercel.app)
- **Backend API:** [https://your-api.railway.app](https://your-api.railway.app)
- **API Docs:** [https://your-api.railway.app/docs](https://your-api.railway.app/docs)

## 📋 Overview

A modern, production-ready application built for Grippi's Junior Full-Stack Developer assignment. Monitor marketing campaigns with real-time filtering, view detailed metrics, and analyze performance across 50+ active campaigns.

### Key Features

✨ **Backend (FastAPI)**
- RESTful API with OpenAPI documentation
- MVC architecture for scalability
- PostgreSQL database with SQLAlchemy ORM
- Status filtering (Active/Paused)
- CORS-enabled for cross-origin requests
- Production deployment on Railway

✨ **Frontend (Next.js)**
- Server-side rendering with App Router
- TypeScript for type safety
- Tailwind CSS for responsive design
- Real-time campaign filtering
- Loading states and error handling
- Deployed on Vercel

✨ **Database**
- 50 sample marketing campaigns
- Indexed queries for performance
- PostgreSQL with validation constraints
- Automatic seeding script

## 🛠️ Tech Stack

**Backend:**
- FastAPI 0.104.1
- SQLAlchemy 2.0.23
- PostgreSQL / SQLite
- Pydantic for validation
- Uvicorn ASGI server

**Frontend:**
- Next.js 14.2.0
- React 18
- TypeScript 5
- Tailwind CSS 3.4
- Fetch API for data fetching

**Deployment:**
- Railway (Backend + Database)
- Vercel (Frontend)

## 📸 Screenshots


## 🚀 Quick Start

### Backend
```bash
cd backend
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
python scripts/seed_data.py
uvicorn app.main:app --reload
```

### Frontend
```bash
cd frontend
npm install
npm run dev
```

Visit `http://localhost:3000` to see the dashboard!

## 📚 API Documentation

Interactive API docs available at `/docs` endpoint:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## 🏗️ Project Structure
```
├── backend/               # FastAPI backend
│   ├── app/
│   │   ├── models/       # SQLAlchemy models
│   │   ├── schemas/      # Pydantic schemas
│   │   ├── routes/       # API endpoints
│   │   ├── services/     # Business logic
│   │   └── database/     # DB configuration
│   └── scripts/          # Utility scripts
└── frontend/             # Next.js frontend
    ├── app/              # App router pages
    ├── components/       # React components
    └── lib/              # Utilities
```

## 🎯 Assignment Requirements

✅ Frontend (Next.js/React) - Campaign table with filtering  
✅ Backend (FastAPI) - RESTful API with mock data  
✅ Database (PostgreSQL) - SQL schema and sample data  
✅ Deployment - Vercel (frontend) + Railway (backend)  
✅ Git - Clean commit history with meaningful messages  

## 👨‍💻 Development

Built following industry best practices:
- MVC architecture for separation of concerns
- Type-safe code with TypeScript/Pydantic
- RESTful API design principles
- Responsive UI with mobile support
- Error handling and loading states
- Environment-based configuration

## 📝 License

MIT License - feel free to use for learning purposes

## 🤝 Contact

Your Name - [bishwajeetsahoo11@gmail.com](mailto:bishwajeetsahoo11@gmail.com)

Project Link: [https://github.com/BishwajeetS11/Marketing_Campaign_Dashboard](https://github.com/BishwajeetS11/Marketing_Campaign_Dashboard)
```

## 🏷️ GitHub Topics/Tags

Add these topics to your repo for discoverability:
```
fastapi
nextjs
postgresql
typescript
tailwindcss
react
python
fullstack
rest-api
mvc-architecture
sqlalchemy
vercel
railway
internship-project
campaign-analytics
marketing-dashboard
