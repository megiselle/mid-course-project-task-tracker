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

# Break Test Evidence



## Break Test 1: Blank Title Validation

Purpose:

Verify that blank task titles are rejected.

Change made:

```python

if not 1 <= len(v) <= 200:

```

temporarily changed to:

```python

if not 0 <= len(v) <= 200:

```

Result:

- test_blank_title_rejected failed.

- API returned HTTP 201 instead of HTTP 422.

Evidence:

```text

FAILED test_blank_title_rejected

assert 201 == 422

```

Fix:

Restored the original validation rule.

Verification:

```text

4 passed

```

Status:

PASS

---

## Break Test 2: Status Transition Validation



Purpose:

Verify that invalid status transitions are rejected.

Change made:

```python

return (current, new) in VALID_TRANSITIONS

```

temporarily changed to:

```python

return True

```

Result:

- test_invalid_status_transition failed.

- API returned HTTP 200 instead of HTTP 422.

Evidence:

```text

FAILED test_invalid_status_transition

assert 200 == 422

```

Fix:

Restored the original validation rule.

Verification:

```text

4 passed

```

Status:

PASS