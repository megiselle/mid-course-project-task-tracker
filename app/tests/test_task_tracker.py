from fastapi.testclient import TestClient

from main import app
from app import storage

client = TestClient(app)


def setup_function():
    storage._reset()


def test_blank_title_rejected():
    response = client.post(
        "/tasks",
        json={
            "title": "   "
        }
    )

    assert response.status_code == 422


def test_get_missing_task_returns_404():
    response = client.get(
        "/tasks/not-found"
    )

    assert response.status_code == 404


def test_valid_status_transition():
    create_response = client.post(
        "/tasks",
        json={
            "title": "Task A"
        }
    )

    task_id = create_response.json()["id"]

    response = client.patch(
        f"/tasks/{task_id}",
        json={
            "status": "InProgress"
        }
    )

    assert response.status_code == 200


def test_invalid_status_transition():
    create_response = client.post(
        "/tasks",
        json={
            "title": "Task B"
        }
    )

    task_id = create_response.json()["id"]

    response = client.patch(
        f"/tasks/{task_id}",
        json={
            "status": "Done"
        }
    )

    assert response.status_code == 422
    
    
def test_filter_by_tag():
    client.post(
        "/tasks",
        json={
            "title": "Task A",
            "tags": ["urgent"]
        }
    )

    client.post(
        "/tasks",
        json={
            "title": "Task B",
            "tags": ["school"]
        }
    )

    response = client.get("/tasks?tag=urgent")

    assert response.status_code == 200
    data = response.json()

    assert len(data) == 1
    assert data[0]["title"] == "Task A"


def test_search_filter():
    client.post(
        "/tasks",
        json={
            "title": "Project Report"
        }
    )

    client.post(
        "/tasks",
        json={
            "title": "Buy Groceries"
        }
    )

    response = client.get("/tasks?search=project")

    assert response.status_code == 200
    data = response.json()

    assert len(data) == 1
    assert data[0]["title"] == "Project Report"