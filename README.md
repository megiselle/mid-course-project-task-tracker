# Task Tracker

A FastAPI-based Task Tracker application with a simple Kanban-style frontend.

## Features

- Create tasks

- Update tasks

- Delete tasks

- Task status transitions

- Tags / Labels

- Search filtering

- Status filtering

- Priority filtering

## Requirements

Install dependencies:

```bash

pip install -r requirements.txt

```

## Running the Backend

Start the FastAPI server:

```bash

uvicorn main:app --reload --port 8000

```

The API will be available at:

```text

[http://localhost:8000](http://localhost:8000)

```

Swagger documentation:

```text

[http://localhost:8000/docs](http://localhost:8000/docs)

```

## Running Tests

Run pytest:

```bash

python -m pytest

```

Expected result:

```text

4 passed

```

## Frontend

Open:

```text

frontend/index.html

```

in a browser after starting the backend.

## Status Transition Rules

Allowed transitions:

```text

ToDo -> InProgress

InProgress -> Done

Done -> InProgress

```

Invalid transitions return HTTP 422.

## Project Structure

```text

app/

├── [models.py](http://models.py)

├── [storage.py](http://storage.py)

├── business_[rules.py](http://rules.py)

├── tests/

│ └── test_task_[tracker.py](http://tracker.py)

docs/

├── midcourse/

frontend/

├── index.html

[README.md](http://README.md)

requirements.txt

[main.py](http://main.py)

```



## Final Project

Branch reviewed: final-project

### What this submission demonstrates

- Existing Task Tracker app still runs inside the intended course scope.
- CI runs the pytest suite on push and pull request.
- Docker image builds and runs with `/health` returning HTTP 200.
- AI review, security review, and ownership evidence are documented in `docs/`.

### How to run locally

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the API:

```bash
uvicorn main:app --reload --port 8000
```

Verify health endpoint:

```text
http://127.0.0.1:8000/health
```

### How to run tests

```bash
python -m pytest
```

Expected result:

```text
6 passed
```

### How to run with Docker

Build image:

```bash
docker build -t task-tracker .
```

Run container:

```bash
docker run -p 8000:8000 task-tracker
```

Verify:

```text
http://localhost:8000/health
```

### Evidence Files

- docs/release-evidence.md
- docs/final-ai-review.md
- docs/ai-playbook.md

### AI Assistance Summary

AI helped draft and review:
- Testing improvements
- Status transition validation
- Documentation
- Docker configuration
- CI configuration
- Security review documentation

Verification methods used:
- Pytest
- Manual API testing
- `/health` endpoint verification
- Frontend verification
- File review

One AI suggestion I corrected:

An AI assumption suggested that status-transition validation already existed. I reviewed the code and implemented explicit transition rules based on instructor requirements instead of accepting that assumption.``