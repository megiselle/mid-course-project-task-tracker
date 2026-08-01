# [AGENTS.md](http://AGENTS.md)

## Project Summary

This repository contains a FastAPI-based Task Tracker application with a simple Kanban-style frontend.

The project uses:

- FastAPI backend

- In-memory storage

- Pytest for testing

- HTML/CSS/JavaScript frontend

- GitHub Actions for CI (if present)

- Docker for local container execution (if present)

## Run Commands

Install dependencies:

```bash

pip install -r requirements.txt

```

Run backend:

```bash

uvicorn main:app --reload --port 8000

```

Run tests:

```bash

python -m pytest

```

Health endpoint:

```text

GET /health

```

Expected response:

```json

{"status":"ok"}

```

Frontend:

```text

frontend/index.html

```

## Business Rules

- Task titles cannot be blank.

- Status transitions are validated.

- Status filtering is supported.

- Priority filtering is supported.

- Tag filtering is supported.

- Search filtering is supported.

- Invalid status transitions return HTTP 422.

- Missing tasks return HTTP 404.

## Important Project Structure

```text

app/

frontend/

docs/

[main.py](http://main.py)

[README.md](http://README.md)

requirements.txt

```

## Module 5 and Final Project Guardrails

- Read first before proposing changes.

- Prefer documentation updates before code changes.

- Create evidence in docs/.

- Do not invent repository structure.

- Cite real files when making claims.

- If information is not visible in the repository, mark it as not confirmed.

## AI Review Expectations

- Explain proposed changes before applying them.

- Reference actual files.

- Avoid assumptions.

- Do not suggest unrelated feature work.

- Respect final-project scope.

## Security and Governance

Never paste:

- API keys

- Tokens

- Passwords

- .env values

- Credentials

- Real customer data

- Personal information

Always verify:

- Test results

- File changes

- Status codes

- Documentation claims

All AI-assisted changes must be reviewed before acceptance.