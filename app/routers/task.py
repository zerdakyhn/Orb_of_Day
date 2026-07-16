from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Task
from app.schemas import TaskCreate, TaskUpdate, TaskResponse  

router = APIRouter(prefix="/tasks", tags=["Tasks"])
@router.post("/", response_model=TaskResponse)


def create_task(task: TaskCreate, db: Session = Depends(get_db)):
    new_task = Task(
        title=task.title,
        description=task.description,
        completed=False,
        owner_id=1  # Replace with the actual user ID from authentication
    )
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task 

@router.put("/{task_id}", response_model=TaskResponse)
def update_task(
    task_id: int,
    task: TaskUpdate,
    db: Session = Depends(get_db),
):
    existing_task = db.query(Task).filter(Task.id == task_id).first()

    if not existing_task:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    existing_task.title = task.title
    existing_task.description = task.description
    existing_task.completed = task.completed

    db.commit()
    db.refresh(existing_task)

    return existing_task
    
@router.delete("/{task_id}")
def dalete_task(task_id: int, db: Session = Depends(get_db)):
    existing_task = db.query(Task).filter(Task.id == task_id).first()

    if not existing_task:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    db.delete(existing_task)
    db.commit()

    return {"detail": "Task deleted successfully"}
