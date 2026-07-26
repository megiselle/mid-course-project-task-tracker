# Reflection

## Project Summary

For the mid-course project, I implemented two scoped features:

1. Tags / Labels
2. Search Filtering

Both features were integrated into the Task Tracker application and made visible in the frontend Kanban board.

---

## AI-Assisted Workflow

I used AI assistance to plan, implement, debug, verify, and refine the features.

The work was completed in small steps:

- Updating models
- Updating storage logic
- Testing API endpoints
- Building a frontend Kanban board
- Connecting frontend and backend
- Displaying task data
- Displaying tags
- Adding search functionality

I reviewed the generated code at each step rather than accepting it blindly.

---

## Challenges Encountered

Several issues occurred during development:

### Backend Errors

After adding tags, task creation began returning a 500 Internal Server Error.

Investigation showed that the tags field had been added to the response model but was not being supplied by the storage layer.

Adding:

```python
tags=payload.tags
```

resolved the issue.

### Frontend Issues

While building the frontend:

- JavaScript was accidentally placed inside the CSS section.
- Some HTML was accidentally placed inside JavaScript.
- Changes were not always visible immediately because the page had not been refreshed.

These issues were resolved through incremental debugging and testing.

---

## What I Learned

The most valuable lesson was the importance of verifying each small change before moving to the next one.

I also learned:

- How FastAPI models, storage, and routes work together.
- How to connect a frontend to a backend using fetch.
- How CORS allows browser communication with APIs.
- How dynamic rendering works in JavaScript.
- How AI assistance is most effective when changes are made and verified incrementally.

---

## Future Improvements

If additional time were available, I would consider:

- Filtering by tags.
- Status-based Kanban columns.
- Search by tags as well as title.
- Improved UI styling.
- Persistent database storage instead of in-memory storage.

---

## Conclusion

The project successfully implemented two complete features, both of which were verified in the backend and frontend. The AI-assisted workflow helped accelerate development while still requiring careful review, debugging, and testing of all generated changes.