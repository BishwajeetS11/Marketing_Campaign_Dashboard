from sqlalchemy import Column, Integer, String, Float
from app.database.dbconnection import Base

class Campaign(Base):
    """Campaign model representing marketing campaigns"""
    __tablename__ = "campaigns"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, index=True)
    status = Column(String, nullable=False)  # Active or Paused
    clicks = Column(Integer, nullable=False, default=0)
    cost = Column(Float, nullable=False, default=0.0)
    impressions = Column(Integer, nullable=False, default=0)