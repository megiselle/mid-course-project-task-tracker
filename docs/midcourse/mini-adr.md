# Mini Architecture Decision Record (ADR)

## Context

The mid-course project required two scoped features to be implemented using an AI-assisted workflow. The features needed to be achievable within the available time, verifiable through testing, and visible in the application.

## Decision

The selected features were:

1. Tags / Labels
2. Search Filtering

## Rationale

### Tags / Labels

Tags provide a simple way to categorize tasks and improve organization. The feature required manageable backend changes and a visible frontend enhancement.

Advantages:

- Small implementation scope
- Easy to test
- Easy to verify
- Visible on task cards

### Search Filtering

Search improves usability by allowing users to quickly find tasks.

Advantages:

- Visible frontend feature
- Builds on existing task data
- Easy to demonstrate
- Simple verification process

## Alternatives Considered

### Comments

Rejected because it would require additional models, storage logic, and UI components.

### Activity Log

Rejected because it would introduce additional complexity for tracking and displaying historical task actions.

## Consequences

The selected features were completed end-to-end and fully verified in both the backend API and frontend Kanban board.