import sys
import os

# Add backend directory to path
backend_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, backend_dir)

from sqlalchemy.orm import Session
from app.database.dbconnection import SessionLocal, engine
from app.models.campaign import Campaign, Base  # ← Fix this line

# Sample campaign data - 50 campaigns
SAMPLE_CAMPAIGNS = [
    {"name": "Summer Sale", "status": "Active", "clicks": 150, "cost": 45.99, "impressions": 1000},
    {"name": "Black Friday", "status": "Paused", "clicks": 320, "cost": 89.50, "impressions": 2500},
    {"name": "Holiday Special", "status": "Active", "clicks": 275, "cost": 120.75, "impressions": 3200},
    {"name": "Spring Launch", "status": "Active", "clicks": 198, "cost": 67.30, "impressions": 1850},
    {"name": "Back to School", "status": "Paused", "clicks": 410, "cost": 155.20, "impressions": 4100},
    {"name": "Winter Clearance", "status": "Active", "clicks": 89, "cost": 32.15, "impressions": 950},
    {"name": "New Year Promo", "status": "Active", "clicks": 502, "cost": 210.80, "impressions": 5500},
    {"name": "Valentine's Day", "status": "Paused", "clicks": 145, "cost": 58.90, "impressions": 1600},
    {"name": "Easter Campaign", "status": "Active", "clicks": 223, "cost": 95.40, "impressions": 2800},
    {"name": "Cyber Monday", "status": "Paused", "clicks": 678, "cost": 299.99, "impressions": 7200},
    {"name": "Flash Sale Weekend", "status": "Active", "clicks": 432, "cost": 178.45, "impressions": 4800},
    {"name": "Mother's Day Special", "status": "Active", "clicks": 267, "cost": 112.30, "impressions": 3100},
    {"name": "Father's Day Deals", "status": "Paused", "clicks": 189, "cost": 76.50, "impressions": 2200},
    {"name": "Labor Day Sale", "status": "Active", "clicks": 345, "cost": 145.99, "impressions": 3900},
    {"name": "Memorial Day Promo", "status": "Active", "clicks": 298, "cost": 125.40, "impressions": 3400},
    {"name": "Independence Day", "status": "Paused", "clicks": 412, "cost": 167.80, "impressions": 4500},
    {"name": "Thanksgiving Special", "status": "Active", "clicks": 556, "cost": 234.90, "impressions": 6100},
    {"name": "Halloween Campaign", "status": "Active", "clicks": 387, "cost": 156.25, "impressions": 4200},
    {"name": "Fall Collection", "status": "Paused", "clicks": 234, "cost": 98.75, "impressions": 2900},
    {"name": "Winter Collection", "status": "Active", "clicks": 445, "cost": 189.50, "impressions": 5000},
    {"name": "Clearance Blowout", "status": "Active", "clicks": 623, "cost": 265.40, "impressions": 6800},
    {"name": "End of Season Sale", "status": "Paused", "clicks": 178, "cost": 72.15, "impressions": 2100},
    {"name": "Graduation Special", "status": "Active", "clicks": 312, "cost": 128.90, "impressions": 3600},
    {"name": "Teacher Appreciation", "status": "Active", "clicks": 156, "cost": 64.30, "impressions": 1900},
    {"name": "Student Discount", "status": "Paused", "clicks": 289, "cost": 118.45, "impressions": 3300},
    {"name": "Senior Citizen Sale", "status": "Active", "clicks": 201, "cost": 84.60, "impressions": 2400},
    {"name": "Military Discount", "status": "Active", "clicks": 167, "cost": 69.90, "impressions": 2000},
    {"name": "First Responder Deal", "status": "Paused", "clicks": 143, "cost": 58.25, "impressions": 1750},
    {"name": "Healthcare Workers", "status": "Active", "clicks": 198, "cost": 81.40, "impressions": 2350},
    {"name": "Employee Exclusive", "status": "Active", "clicks": 234, "cost": 96.80, "impressions": 2750},
    {"name": "Referral Program", "status": "Active", "clicks": 456, "cost": 192.30, "impressions": 5200},
    {"name": "Loyalty Rewards", "status": "Paused", "clicks": 389, "cost": 159.75, "impressions": 4400},
    {"name": "VIP Member Sale", "status": "Active", "clicks": 523, "cost": 218.90, "impressions": 5800},
    {"name": "Birthday Special", "status": "Active", "clicks": 278, "cost": 115.60, "impressions": 3250},
    {"name": "Anniversary Sale", "status": "Paused", "clicks": 367, "cost": 151.20, "impressions": 4100},
    {"name": "Grand Opening", "status": "Active", "clicks": 612, "cost": 256.70, "impressions": 6700},
    {"name": "Store Relocation", "status": "Active", "clicks": 245, "cost": 102.45, "impressions": 2900},
    {"name": "New Product Launch", "status": "Paused", "clicks": 489, "cost": 204.80, "impressions": 5400},
    {"name": "Limited Edition", "status": "Active", "clicks": 534, "cost": 223.50, "impressions": 5900},
    {"name": "Exclusive Preview", "status": "Active", "clicks": 401, "cost": 167.90, "impressions": 4600},
    {"name": "Weekend Flash Deal", "status": "Paused", "clicks": 298, "cost": 124.30, "impressions": 3400},
    {"name": "Monday Madness", "status": "Active", "clicks": 356, "cost": 148.75, "impressions": 4000},
    {"name": "Midweek Special", "status": "Active", "clicks": 267, "cost": 111.40, "impressions": 3100},
    {"name": "Friday Feature", "status": "Paused", "clicks": 423, "cost": 176.90, "impressions": 4700},
    {"name": "Social Media Exclusive", "status": "Active", "clicks": 589, "cost": 246.20, "impressions": 6400},
    {"name": "Email Subscriber Deal", "status": "Active", "clicks": 445, "cost": 186.50, "impressions": 5100},
    {"name": "Mobile App Promo", "status": "Paused", "clicks": 378, "cost": 157.80, "impressions": 4300},
    {"name": "Online Only Sale", "status": "Active", "clicks": 512, "cost": 214.60, "impressions": 5700},
    {"name": "In-Store Exclusive", "status": "Active", "clicks": 289, "cost": 120.90, "impressions": 3300},
    {"name": "Bundle Deal Special", "status": "Paused", "clicks": 334, "cost": 139.45, "impressions": 3800},
]

def seed_database():
    """Seed the database with sample campaign data"""
    
    # Create tables
    Base.metadata.create_all(bind=engine)  # ← Now this will work
    
    # Create session
    db = SessionLocal()
    
    try:
        # Check if data already exists
        existing_count = db.query(Campaign).count()
        
        if existing_count > 0:
            print(f"⚠️  Database already contains {existing_count} campaigns.")
            response = input("Do you want to clear and re-seed? (y/n): ")
            
            if response.lower() == 'y':
                db.query(Campaign).delete()
                db.commit()
                print("✅ Database cleared!")
            else:
                print("❌ Seeding cancelled.")
                return
        
        # Insert campaigns
        for campaign_data in SAMPLE_CAMPAIGNS:
            campaign = Campaign(**campaign_data)
            db.add(campaign)
        
        db.commit()
        print(f"✅ Successfully seeded {len(SAMPLE_CAMPAIGNS)} campaigns!")
        
        # Show statistics
        active = db.query(Campaign).filter(Campaign.status == "Active").count()
        paused = db.query(Campaign).filter(Campaign.status == "Paused").count()
        print(f"📊 Active: {active} | Paused: {paused}")
        
    except Exception as e:
        print(f"❌ Error seeding database: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    print("🌱 Starting database seeding...")
    seed_database()