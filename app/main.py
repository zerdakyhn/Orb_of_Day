from fastapi import FastAPI

from app.database import engine
from app.models import Base
from app.routers import user, task

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Orb of Day API",
    version="1.0.0",
    description="Task and Productivity Management System"
)
app.include_router(user.router)
app.include_router(task.router)


@app.get("/")
def root():
    return {
        "message": "Welcome to Orb of Day API!"
    }