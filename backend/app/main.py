from dotenv import load_dotenv
load_dotenv()

import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database.dbconnection import engine
from app.models.campaign import Base
from app.routes import campaign_routes

# Create database tables
Base.metadata.create_all(bind=engine)

# Initialize FastAPI app
app = FastAPI(
    title="Campaign Analytics API",
    description="API for managing marketing campaigns",
    version="1.0.0"
)

# CORS configuration
frontend_url = os.getenv("FRONTEND_URL", "http://localhost:3000")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[frontend_url],  # Allowing frontend URL only
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(
    campaign_routes.router, 
    prefix="/campaigns", 
    tags=["Campaigns"]
)

@app.get("/")
def read_root():
    """Root endpoint"""
    return {
        "message": "Campaign Analytics API",
        "statuscode": 200,
        "status": "running",
        "version": "1.0.0"
    }

@app.get("/health")
def health_check():
    """Health check endpoint for Railway"""
    return {
        "statuscode": 200,
        "status": "healthy & running"
    }