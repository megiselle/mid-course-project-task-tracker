# User Stories

## Feature 1: Tags / Labels

### User Story 1

As a user, I want to assign tags to tasks so that I can organize related work items.

#### Acceptance Criteria

- A task can be created with one or more tags.
- Tags are stored by the backend.
- Tags are returned by the API.

---

### User Story 2

As a user, I want to view tags on task cards so that I can quickly identify task categories.

#### Acceptance Criteria

- Tags are displayed on Kanban task cards.
- Multiple tags are displayed correctly.
- Tasks without tags still display correctly.

---

### User Story 3

As a user, I want to use tags to identify urgent or important tasks so that I can prioritize my work.

#### Acceptance Criteria

- Users can assign tags such as "urgent".
- Tags remain attached to tasks after retrieval.
- Tags are visible in the frontend.

---

### User Story 4

As a user, I want tags to remain attached to tasks when tasks are viewed again so that important information is not lost.

#### Acceptance Criteria

- Tags persist after task creation.
- Tags are returned in GET requests.
- Tags are consistently displayed in the frontend.

---

## Feature 2: Search Filtering

### User Story 1

As a user, I want to search tasks by title so that I can quickly find a specific task.

#### Acceptance Criteria

- A search box is available on the Kanban board.
- Search filters tasks by title.
- Matching tasks remain visible.

---

### User Story 2

As a user, I want search results to update while typing so that I receive immediate feedback.

#### Acceptance Criteria

- Search updates dynamically.
- No page refresh is required.
- Results update after each keystroke.

---

### User Story 3

As a user, I want non-matching tasks to be hidden so that I only see relevant results.

#### Acceptance Criteria

- Matching tasks remain visible.
- Non-matching tasks are hidden.
- Filtering works correctly with multiple tasks.

---

### User Story 4

As a user, I want all tasks to return when the search box is cleared so that I can return to the full board view.

#### Acceptance Criteria

- Clearing the search box restores all tasks.
- Previously hidden tasks become visible again.
- The board remains functional after clearing the search field.
