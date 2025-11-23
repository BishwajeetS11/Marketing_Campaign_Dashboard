from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import Optional, List
from app.database.dbconnection import get_db
from app.schemas.campaign import Campaign
from app.services.campaign_service import CampaignService

router = APIRouter()

@router.get("/", response_model=List[Campaign])
def get_campaigns(
    status: Optional[str] = Query(None, description="Filter by status: Active or Paused"),
    db: Session = Depends(get_db)
):
    """
    Get all campaigns with optional status filter
    
    Query Parameters:
        - status: Filter by 'Active' or 'Paused' (optional)
    
    Returns:
        List of campaigns
    """
    try:
        # Validate status if provided
        if status and not CampaignService.validate_status(status):
            raise HTTPException(
                status_code=400, 
                detail="Status must be 'Active' or 'Paused'"
            )
        
        # Get campaigns from service layer
        campaigns = CampaignService.get_all_campaigns(db, status)
        return campaigns
    
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=500, 
            detail=f"Database error: {str(e)}"
        )

@router.get("/{campaign_id}", response_model=Campaign)
def get_campaign(campaign_id: int, db: Session = Depends(get_db)):
    """
    Get a specific campaign by ID
    
    Path Parameters:
        - campaign_id: Campaign ID
    
    Returns:
        Campaign object
    """
    campaign = CampaignService.get_campaign_by_id(db, campaign_id)
    
    if not campaign:
        raise HTTPException(
            status_code=404, 
            detail=f"Campaign with id {campaign_id} not found"
        )
    
    return campaign