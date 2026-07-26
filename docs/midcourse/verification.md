# Verification

## Feature 1: Tags / Labels

### Test 1: Create task with tags

Request:

```json
{
  "title": "Project Report",
  "tags": ["school", "urgent"]
}
```

Expected Result:

- Task is created successfully.
- Tags are stored.

Actual Result:

- POST /tasks returned HTTP 201.
- Tags were returned in the API response.

Status:

PASS

---

### Test 2: Display tags on frontend

Expected Result:

- Tags appear on task cards.

Actual Result:

- The task "Project Report" displayed:
  - Tags: school, urgent

Status:

PASS

---

## Feature 2: Search Tasks

### Test 1: Search for "project"

Expected Result:

- Only matching tasks remain visible.

Actual Result:

- Only "Project Report" remained visible.

Status:

PASS

---

### Test 2: Clear search

Expected Result:

- All tasks become visible again.

Actual Result:

- All task cards reappeared.

Status:

PASS

---

## CRUD Verification

Verified:

- POST /tasks
- GET /tasks
- GET /tasks/{task_id}
- PATCH /tasks/{task_id}
- DELETE /tasks/{task_id}

Result:

All endpoints functioned correctly.

Status:

PASS