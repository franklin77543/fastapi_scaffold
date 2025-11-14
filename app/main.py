from fastapi import FastAPI
from app.db.database import Base, engine
from app.api.v1.endpoints import users
from app.core.config import settings

# Create all database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title=settings.app_name, debug=settings.debug)

# Include routers
app.include_router(users.router, prefix="/api/v1")


@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI Scaffold"}


@app.get("/health")
def health_check():
    return {"status": "ok"}
