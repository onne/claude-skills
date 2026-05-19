# Gemini CLI - Claude Skills & Agent Plugins Library

This repository is a production-ready, platform-agnostic library of 313+ agent skills and 400+ automation tools. It is designed using a **Domain-Driven Architecture** to provide AI agents with specialized expertise through a "write once, deploy anywhere" framework.

## Repository Architecture

### 1. Domain Clusters (The Core)
The repository is organized by business and technical functions:
*   **Engineering & DevOps:** `/engineering`, `/engineering-team` (Architecture, SecOps, QA).
*   **Leadership & Strategy:** `/c-level-advisor` (Founder-mode C-suite personas).
*   **Operations & Growth:** `/business-growth`, `/business-operations`, `/commercial`.
*   **Specialized Functions:** `/marketing-skill`, `/ra-qm-team`, `/research`, `/finance`.

### 2. Hierarchical Modules
*   **Skills:** Modular instruction sets (`SKILL.md`) that define *how* to execute tasks.
*   **Agents:** Curated personas (`agents/`) with distinct voices and skill loadouts.
*   **Commands:** Markdown-based "slash commands" (`/commands`) for direct workflows.
*   **Reference Assets:** Deep knowledge bases (`references/`) and templates (`assets/`).

## Operational Standards ("The Rules of the Game")

All interactions and contributions MUST adhere to these foundational principles:

### 1. Skill Authoring Patterns (The 10 Patterns)
*   **Context-First:** Always check for domain context files (e.g., `project-context.md`) before asking questions.
*   **Practitioner Voice:** Act as a senior expert (opinionated, direct) rather than a neutral textbook.
*   **Multi-Mode:** Design for multiple entry points (Build from scratch vs. Optimize existing).
*   **Related Skills:** Always provide "When to use / When NOT to use" disambiguation for related skills.
*   **Proactive Triggers:** Surface risks and issues without being asked when patterns are detected.

### 2. Communication Standard
All output should follow the **Bottom Line First** protocol:
1.  **BOTTOM LINE:** One-sentence answer.
2.  **WHAT:** Categorized findings with confidence tags (🟢 verified, 🟡 medium, 🔴 assumed).
3.  **WHY THIS MATTERS:** Business impact/consequence.
4.  **HOW TO ACT:** Concrete actions with owners and deadlines.

### 3. Technical Constraints
*   **Python Scripts:** Must use **standard library only** (no `pip` installs). Must support `--json` and `--help`.
*   **File Economy:** Edit existing files rather than creating new ones unless necessary.
*   **SKILL.md Limits:** Keep main skill files under 500 lines (ideally <200); move depth to `references/`.

## Workflow & Pipeline

*   **Production Pipeline:** Every skill follows: Intent → Research → Draft → Eval → Iterate → Compliance → Package → Deploy → Verify.
*   **Quality Gate:** Skills must pass a structured compliance check (Score ≥ 85%) before merging.
*   **Orchestration:** Combine Personas (Who), Skills (How), and Commands (What) to solve complex, cross-domain problems.

## Usage in Gemini CLI

*   **Install:** Run `./scripts/gemini-install.sh`.
*   **Activate:** Use `activate_skill(name="<skill-name>")`.
*   **Validate:** Use `engineering/skill-tester/scripts/skill_validator.py` for new modules.
