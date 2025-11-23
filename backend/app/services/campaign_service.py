from sqlalchemy.orm import Session
from typing import List, Optional
from app.models.campaign import Campaign

class CampaignService:
    """
    Service layer for campaign business logic
    """
    
    @staticmethod
    def get_all_campaigns(db: Session, status: Optional[str] = None) -> List[Campaign]:
        """
        Get all campaigns with optional status filter
        
        Args:
            db: Database session
            status: Optional status filter ('Active' or 'Paused')
            
        Returns:
            List of Campaign objects
        """
        query = db.query(Campaign)
        
        if status:
            query = query.filter(Campaign.status == status)
        
        return query.all()
    
    @staticmethod
    def get_campaign_by_id(db: Session, campaign_id: int) -> Optional[Campaign]:
        """
        Get a specific campaign by ID
        
        Args:
            db: Database session
            campaign_id: Campaign ID
            
        Returns:
            Campaign object or None if not found
        """
        return db.query(Campaign).filter(Campaign.id == campaign_id).first()
    
    @staticmethod
    def validate_status(status: str) -> bool:
        """
        Validate campaign status
        
        Args:
            status: Status string to validate
            
        Returns:
            True if valid, False otherwise
        """
        return status in ["Active", "Paused"]