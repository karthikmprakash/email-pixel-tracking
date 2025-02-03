from fastapi import APIRouter, HTTPException, Request, Response
from loguru import logger
from sqlalchemy import func
from sqlalchemy.orm import Session

from app.config import settings
from app.database import SessionLocal
from app.models import TrackingEvent
from app.utils import get_image_bytes

router = APIRouter()


@router.get("/track/{email_id}")
async def track_email(email_id: str, request: Request):
    db: Session = SessionLocal()
    try:
        tracking_event = TrackingEvent(
            email_id=email_id,
            user_agent=request.headers.get("User-Agent"),
            ip_address=request.client.host,
        )
        db.add(tracking_event)
        db.commit()
        db.refresh(tracking_event)

        # Return a 1x1 transparent pixel
        icon = get_image_bytes("../assets/icon.png")
        return Response(content=icon, media_type="image/gif")
    except Exception as e:
        logger.error(f"Error tracking email: {e}")
        logger.exception(e)
        db.rollback()
        raise HTTPException(status_code=500, detail="Internal Server Error")
    finally:
        db.close()


@router.get("/track_counts")
async def get_track_counts():
    db: Session = SessionLocal()
    try:
        track_counts = (
            db.query(
                TrackingEvent.email_id,
                func.count(TrackingEvent.email_id).label("count"),
            )
            .group_by(TrackingEvent.email_id)
            .all()
        )
        return track_counts
    except Exception as e:
        logger.error(f"Error getting track counts: {e}")
        logger.exception(e)
        raise HTTPException(status_code=500, detail="Internal Server Error")
    finally:
        db.close()
