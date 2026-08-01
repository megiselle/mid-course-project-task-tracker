# Personal AI Playbook

## When I Reach for AI First

- When I need help debugging failing tests and error messages.

- When I need help understanding existing code before changing it.

- When I need help creating documentation, planning tasks, or reviewing requirements.

- When I need help generating a structured starting point for CI, Docker, or testing work.

## When I Do Not Reach for AI First

- When handling credentials, secrets, tokens, or personal data.

- When I have not yet read the relevant project files.

- When I do not understand the requirement well enough to evaluate the AI output.

- When a change affects ownership, grading, or business decisions that require my judgment.

## My Non-Negotiables

- Never paste passwords, API keys, tokens, .env values, or personal data into AI tools.

- Never accept code I cannot explain.

- Always verify AI-generated changes before committing them.

- Keep responsibility for the final result instead of assuming the AI is correct.

## My Review Rules

- Read every proposed file change before accepting it.

- Run tests whenever code changes are introduced.

- Verify endpoints manually when API behavior changes.

- Check documentation claims against the running application.

- Grade AI suggestions as Useful, Noise, Wrong, Valid, False Positive, or Needs Verification instead of accepting them automatically.

## What I Am Still Figuring Out

- When to use a coding assistant versus solving a problem independently.

- The best workflow for balancing speed and verification.

- How different AI tools fit different software development tasks.

- How to perform larger security reviews efficiently while maintaining confidence in the results.

## Decision Card

- For a new feature I reach for: Codex or Cursor to help plan implementation after I understand the requirement.

- For a code review I reach for: Codex because it helps evaluate repository-grounded changes and documentation.

- For debugging I reach for: Copilot or Codex after collecting the exact failing test, logs, and error output.

- For infrastructure I reach for: Codex to help review Docker, CI, and configuration files, followed by manual verification.

- I will never paste passwords, tokens, API keys, .env values, or personal customer data into an AI tool.

- My one rule is: If I cannot explain a change and verify it myself, I do not accept it.

## 30-Day Re-Read Commitment

I will revisit this playbook within 30 days and evaluate whether I am still following these rules and whether any of them need refinement based on future projects.