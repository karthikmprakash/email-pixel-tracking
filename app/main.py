from fastapi import FastAPI

from . import schemas
from .database import Base, engine
from .routers import tracking

# Create the database tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(tracking.router)
