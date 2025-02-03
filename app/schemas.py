from datetime import datetime

from pydantic import BaseModel


class TrackingEventBase(BaseModel):
    email_id: str
    user_agent: str
    ip_address: str


class TrackingEventCreate(TrackingEventBase):
    pass


class TrackingEvent(TrackingEventBase):
    id: int
    timestamp: datetime

    class Config:
        orm_mode: True


class TrackingEventCount(BaseModel):
    email_id: str
    count: int
