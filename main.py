from fastapi import FastAPI, status, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from app import storage
from app.business_rules import validate_status_transition
from app.models import (
    TaskCreate,
    TaskResponse,
    TaskStatus,
    TaskPriority,
    TaskUpdate,
)

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.get("/health")

def health_check():
    return {"status": "ok"}

@app.post(
    "/tasks",
    response_model=TaskResponse,
    status_code=status.HTTP_201_CREATED,
    tags=["tasks"],
)
def create_task(payload: TaskCreate) -> TaskResponse:
    return storage.add_task(payload)


@app.get("/tasks", response_model=list[TaskResponse], tags=["tasks"])
def list_tasks(
    status: TaskStatus | None = None,
    priority: TaskPriority | None = None,
    tag: str | None = None,
    search: str | None = None,
):

    return storage.get_all_tasks(
        status=status,
        priority=priority,
        tag=tag,
        search=search,
    )

@app.get("/tasks/{task_id}", response_model=TaskResponse, tags=["tasks"])
def get_task(task_id: str) -> TaskResponse:
    task = storage.get_task_by_id(task_id)

    if task is None:
        raise HTTPException(
            status_code=404,
            detail=f"Task with id {task_id} not found",
        )

    return task



@app.patch("/tasks/{task_id}", response_model=TaskResponse, tags=["tasks"])
def update_task(task_id: str, payload: TaskUpdate) -> TaskResponse:

    existing = storage.get_task_by_id(task_id)

    if existing is None:
        raise HTTPException(
            status_code=404,
            detail=f"Task with id {task_id} not found",
        )

    if payload.status is not None:

        if payload.status == existing.status:
            raise HTTPException(
                status_code=422,
                detail="Status cannot remain unchanged",
            )

        if not validate_status_transition(
            existing.status,
            payload.status,
        ):
            raise HTTPException(
                status_code=422,
                detail="Invalid status transition",
            )

    updated_task = storage.update_task(task_id, payload)

    return updated_task

@app.delete("/tasks/{task_id}", tags=["tasks"])
def delete_task(task_id: str):
    deleted = storage.delete_task(task_id)

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail=f"Task with id {task_id} not found",
        )

    return {"message": f"Task {task_id} deleted"}
