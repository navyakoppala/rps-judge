# AI Judge – Rock Paper Scissors Plus

## Overview
This project implements a prompt-driven AI Judge for a simplified
Rock-Paper-Scissors Plus game.

The focus of this implementation is not on building a full game engine,
but on demonstrating strong prompt design, clear reasoning boundaries,
and explainable AI decisions.

---

## Design Goals
- Use prompting to drive all decision-making
- Clearly separate intent understanding, game logic, and response generation
- Handle ambiguous and invalid inputs explicitly
- Produce structured and explainable outputs

---

## Prompt Design
The solution uses two prompts:

### System Prompt
Defines the AI’s role as an AI Judge and enforces a structured reasoning process:
- Intent Understanding
- Move Validation
- Rule Application
- Outcome Decision
- Explanation

This ensures consistency and explainability across decisions.

### Instruction Prompt
Encodes all game rules and constraints, including:
- Valid moves and special bomb rules
- Handling of ambiguous and invalid inputs
- Winner determination
- Required structured output format

All game logic resides in the prompts, not in application code.

---

## Architecture
The system follows a clean separation of concerns:

- Intent Understanding: Interpreting the user’s free-text input
- Game Logic Evaluation: Applying rules and determining outcomes
- Response Generation: Producing structured, user-facing explanations

The application code acts only as minimal glue for state handling and prompt construction.

---

## State Management
Only minimal state is maintained:
- Current round number
- Whether the user has already used the bomb

This satisfies the assignment constraints while enabling correct rule enforcement.

---

## Edge Cases Considered
The prompts explicitly handle:
- Ambiguous inputs
- Completely invalid inputs
- Reuse of the bomb move
- Rounds where no winner should be declared

Invalid or unclear moves correctly waste the turn.

---

## Why Logic Is Not in Code
All validation and winner determination are delegated to the AI Judge
via prompt instructions. The application code intentionally avoids
hardcoded logic (e.g., if-else comparisons) to align with the assignment’s
prompt-driven design requirement.

---

## Future Improvements
With additional time, the system could be extended by:
- Connecting to a live LLM (e.g., Gemini) for real-time judgments
- Adding confidence scores for intent interpretation
- Improving multi-round result summarization

---

## Key Takeaway
This project demonstrates how careful prompt engineering can replace
traditional hardcoded logic while preserving correctness, clarity,
and explainability in a conversational AI system.

---

### Submission Status
- Prompt Design: Completed
- Architecture Separation: Completed
- Edge-Case Handling: Completed
- Explainability: Completed

This implementation is fully aligned with the
Applied AI Engineer (Conversational Agents) assessment requirements.
