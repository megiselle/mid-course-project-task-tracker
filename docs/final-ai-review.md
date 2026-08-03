# Final AI Review and Ownership Evidence

## `AGENTS.md`Guardrails

- Repo-specific stack and commands included: Yes

- Docs-first/read-first guardrail included: Yes

- Unexpected app/frontend edits rule included: Yes

---

## AI Code Review Mini-Log

| AI Comment | Grade | Reason | Verification or Decision |

|------------|--------|---------|--------------------------|

| Add FastAPI TestClient tests instead of testing storage functions directly. | Useful | Better matches API behavior and instructor requirements. | Implemented and verified with 6 passing tests. |

| Add status-transition validation in business rules. | Useful | The instructor specifically required explicit transition rules. | Added and verified through passing tests. |

| Add a frontend tag filter. | Noise | The backend filtering requirement was more urgent, and the existing rubric emphasized filtering support rather than major frontend changes. | Backend filtering was implemented and tested. |

---

## AI Security Mini-Review

| Finding | File Evidence | Grade | Reason | Next Action |

|----------|--------------|--------|--------|------------|

| No authentication or authorization on task endpoints. | `main.py` | Valid | Acceptable for course scope, but would be a production risk. | Document scope limitation. |

| In-memory storage is not persistent. | app/`storage.py` | Noise | True, but this is an intentional learning-project decision. | No action required. |

| Task title validation prevents blank titles. | app/`models.py` | Valid | Input validation exists and protects data quality. | Continue testing validation behavior. |

---

## Manual Security Check

I manually reviewed the application startup behavior, task validation rules, status transition handling, and API responses.

Manual observations:

- Blank titles are rejected with HTTP 422.

- Invalid status transitions are rejected with HTTP 422.

- Missing tasks return HTTP 404.

- No secrets, tokens, credentials, or environment values are stored in the repository.

These checks were verified using pytest and manual API testing.

---

## One AI Output I Rejected or Corrected

One AI suggestion incorrectly assumed that status-transition validation was already implemented.

After reviewing the repository and instructor feedback, I verified that transition validation was missing and implemented explicit business rules instead of accepting the assumption.

This reinforced the Module 5 principle of grading AI output rather than accepting it blindly.

---

## Three AI Usage Rules

1. Never paste:
   - API keys
   - Passwords
   - Tokens

2. Always verify:
   - AI-generated code before committing changes.
   - Test results before recording evidence.
   - Documentation claims against the actual repository contents.

3. Record AI contributions by:
   - Documenting significant AI-assisted changes.
   - Reviewing and adapting AI suggestions before use.
   - Maintaining ownership of all final decisions and submitted work.

   ## Ownership Statement

I confirm that I understand the architecture, implementation, testing, and documentation included in this repository and am comfortable submitting it as my own work. AI tools were used to assist with planning, code suggestions, debugging, and documentation, but all outputs were reviewed, tested, and adapted before inclusion. I made the final decisions regarding the design and implementation of the Task Tracker application. I can explain how the API endpoints, validation rules, tests, CI workflow, and Docker configuration work. For these reasons, I consider this repository to accurately represent my own learning and effort.

 
