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

``