# Prompt Log

## Prompt 1

Goal: Add a Tags feature to the Task Tracker.

Prompt:

"Add support for tags to tasks. Update the models, storage layer, and API responses while keeping the change small and easy to verify."

Result:

- Added a tags field to TaskCreate.
- Added a tags field to TaskUpdate.
- Added a tags field to TaskResponse.

Review:

The generated code was mostly correct, but additional changes were needed in the storage layer.

Decision:

Accepted with modifications.

---

## Prompt 2

Goal: Fix the task creation error after adding tags.

Prompt:

"Help diagnose a 500 Internal Server Error that occurs after adding tags."

Result:

The issue was traced to TaskResponse requiring tags while storage.py was not providing them.

Review:

The analysis correctly identified the missing field.

Decision:

Accepted.

Fix applied:

```python
tags=payload.tags,
```

Verification:

POST /tasks returned 201 successfully after the fix.

---

## Prompt 3

Goal: Connect the frontend Kanban board to the backend API.

Prompt:

"Help the frontend load tasks from GET /tasks."

Result:

Implemented a fetch request:

```javascript
fetch("http://127.0.0.1:8000/tasks")
```

Review:

The frontend successfully retrieved task data.

Decision:

Accepted.

Verification:

The board displayed tasks from the backend.

---

## Prompt 4

Goal: Display tags on task cards.

Prompt:

"Show task tags on the Kanban board cards."

Result:

Updated card rendering logic to display:

```javascript
Tags: ${task.tags.join(", ")}
```

Review:

Worked correctly.

Decision:

Accepted.

Verification:

Tasks displayed tags such as:

school, urgent

---

## Prompt 5

Goal: Add search functionality.

Prompt:

"Add a search box that filters tasks by title."

Result:

Implemented:

- Search box UI
- Frontend filtering logic
- Real-time filtering using an input event listener

Review:

The feature worked as expected.

Decision:

Accepted.

Verification:

Typing "project" displayed only matching task cards.