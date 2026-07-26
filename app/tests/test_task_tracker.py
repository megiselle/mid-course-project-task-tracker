from app.models import TaskCreate
from app import storage

def setup_function():
    storage._reset()


def test_create_task():
    task = storage.add_task(
        TaskCreate(title="Test Task")
    )

    assert task.title == "Test Task"


def test_create_task_with_tags():
    task = storage.add_task(
        TaskCreate(
            title="Tagged Task",
            tags=["school", "urgent"]
        )
    )

    assert task.tags == ["school", "urgent"]


def test_get_all_tasks():
    storage.add_task(
        TaskCreate(title="Task 1")
    )

    storage.add_task(
        TaskCreate(title="Task 2")
    )

    tasks = storage.get_all_tasks()

    assert len(tasks) == 2


def test_delete_task():
    task = storage.add_task(
        TaskCreate(title="Delete Me")
    )

    deleted = storage.delete_task(task.id)

    assert deleted is True