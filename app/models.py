from datetime import datetime

from sqlalchemy import Column, DateTime, Integer, String

from .database import Base


class TrackingEvent(Base):
    __tablename__ = "tracking_events"

    id = Column(Integer, primary_key=True, index=True)
    email_id = Column(String, index=True)
    timestamp = Column(DateTime, default=datetime.utcnow)
    user_agent = Column(String)
    ip_address = Column(String)
