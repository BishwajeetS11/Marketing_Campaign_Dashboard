from pydantic import BaseModel, Field

class CampaignBase(BaseModel):
    name: str = Field(..., description="Campaign name")
    status: str = Field(..., description="Campaign status: Active or Paused")
    clicks: int = Field(ge=0, description="Number of clicks")
    cost: float = Field(ge=0, description="Campaign cost")
    impressions: int = Field(ge=0, description="Number of impressions")

class Campaign(CampaignBase):
    id: int
    
    class Config:
        from_attributes = True  # It enables compatibility with SQLAlchemy models