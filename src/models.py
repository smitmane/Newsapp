from sqlalchemy import Column, Integer, String,JSON, DateTime
from database import Base
from datetime import datetime
import pytz
# Convert UTC to IST
def utcnow_ist():
    utc_now = datetime.utcnow()
    ist = pytz.timezone("Asia/Kolkata")
    return utc_now.replace(tzinfo=pytz.utc).astimezone(ist)

class News(Base):
    __tablename__ = "news"

    id = Column(Integer, primary_key=True, index=True)
    result = Column(JSON, nullable=True)
    created_at = Column(DateTime, default=utcnow_ist) 
    
