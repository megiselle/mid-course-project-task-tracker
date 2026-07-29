import datetime
import uuid
from typing import Optional

from app.models import TaskCreate, TaskPriority, TaskResponse, TaskStatus, TaskUpdate

_tasks: dict[str, TaskResponse] = {}


def _reset() -> None:
    _tasks.clear()


def add_task(payload: TaskCreate) -> TaskResponse:
    now = datetime.datetime.now(datetime.timezone.utc)
    task_id = str(uuid.uuid4())
    task = TaskResponse(
        id=task_id,
        title=payload.title,
        description=payload.description or "",
        status=payload.status,
        priority=payload.priority, 
        assignee=payload.assignee,
        tags=payload.tags,
        created_at=now,
        updated_at=now,
    )
    _tasks[task_id] = task
    return task

def get_all_tasks(
    status: Optional[TaskStatus] = None,
    priority: Optional[TaskPriority] = None,
    tag: Optional[str] = None,
    search: Optional[str] = None,
    ) -> list[TaskResponse]:
    tasks = list(_tasks.values())

    if status is not None:
        tasks = [task for task in tasks if task.status == status]

    if priority is not None:
        tasks = [task for task in tasks if task.priority == priority]

    if tag is not None:
        tasks = [task for task in tasks if tag in task.tags]

    if search is not None:
        search = search.lower()
        tasks = [
            task
            for task in tasks
            if search in task.title.lower()
        ]

    return tasks


def get_task_by_id(task_id: str) -> Optional[TaskResponse]:
    return _tasks.get(task_id)


def update_task(task_id: str, payload: TaskUpdate) -> Optional[TaskResponse]:
    existing = _tasks.get(task_id)
    if existing is None:
        return None
    updates = payload.model_dump(exclude_unset=True)
    if not updates:
        return existing
    updates["updated_at"] = datetime.datetime.now(datetime.timezone.utc)
    updated = existing.model_copy(update=updates)
    _tasks[task_id] = updated
    return updated


def delete_task(task_id: str) -> bool:
    if task_id not in _tasks:
        return False
    del _tasks[task_id]
    return True
