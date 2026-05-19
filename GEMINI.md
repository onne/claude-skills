# Gemini CLI - Engineering & Developer Tools Library

This repository is a heavily curated, engineering-focused fork of the Claude Skills & Agent Plugins Library. It has been pruned from 350+ skills down to a core set of ~180 specialized capabilities tailored specifically for software engineers, architects, and DevOps practitioners.

## Repository Architecture

### 1. Domain Clusters (The Core)
The repository is organized strictly around technical and project execution:
*   **Engineering & DevOps:** `/engineering`, `/engineering-team` (Architecture, SecOps, CI/CD, QA).
*   **Developer Tooling:** `/project-management` (Restored Atlassian tools like Jira/Confluence workflows).

### 2. Hierarchical Modules
*   **Skills:** Modular instruction sets (`SKILL.md`) that define *how* to execute technical tasks.
*   **Agents:** Curated technical personas (`agents/`) with distinct voices and skill loadouts (e.g., Senior Engineer, DevOps Engineer).
*   **Commands:** Markdown-based "slash commands" (`/commands`) for direct developer workflows.
*   **Reference Assets:** Deep knowledge bases (`references/`) and templates (`assets/`).

## Operational Standards ("The Rules of the Game")

All interactions and contributions MUST adhere to these foundational principles:

### 1. Skill Authoring Patterns
*   **Context-First:** Always check for domain context files (e.g., `project-context.md`) before modifying architecture.
*   **Practitioner Voice:** Act as a senior technical expert (opinionated, direct).
*   **Multi-Mode:** Design for multiple entry points (Scaffold from scratch vs. Refactor existing).
*   **Proactive Triggers:** Surface technical debt, security risks, and architectural flaws without being asked when patterns are detected.

### 2. Technical Constraints
*   **Python Scripts:** Must use **standard library only** (no `pip` installs). Must support `--json` and `--help`.
*   **File Economy:** Edit existing files rather than creating new ones unless necessary.
*   **SKILL.md Limits:** Keep main skill files under 500 lines (ideally <200); move technical depth to `references/`.
*   **Markdown AST:** Documentation and skills are treated as "Code". The AST of markdown files (Frontmatter, H1, H2) is used to map repository structures.

## Usage in Gemini CLI

*   **Install:** Run `./scripts/gemini-install.sh`.
*   **Activate:** Use `activate_skill(name="<skill-name>")`.
*   **Discover:** Refer to `CORPUS_MAP.md` for a semantic map of all currently available engineering skills.
