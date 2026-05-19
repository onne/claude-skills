# Alireza Rezvani Skills Collection (Engineering & DevOps Edition)

> A highly curated library of AI agent skills, prompts, and automation workflows focused exclusively on Engineering, DevOps, Architecture, and Developer Tooling (including Atlassian).

[![CI](https://github.com/alirezarezvani/claude-skills/actions/workflows/ci-quality-gate.yml/badge.svg)](https://github.com/alirezarezvani/claude-skills/actions)

## What is this?

This repository is a pruned, engineering-focused fork of the Alireza Rezvani Skills Collection. It contains ~180 specialized agentic workflows designed to extend the capabilities of AI agents (like Claude Code and Gemini CLI) in professional software development environments.

---

## Quick Start

### Prerequisites

| Tool | Version | Install |
|------|---------|---------|
| Python | 3.8+ | `brew install python` |
| Git | 2.x | `brew install git` |

### Setup (2 minutes)

```bash
git clone git@github.com:onne/claude-skills.git
cd claude-skills
# Optional: explore scripts
ls scripts/
```

### Verify it works

- [ ] Repository structure is visible
- [ ] `GEMINI.md` exists in the root
- [ ] The `engineering/` directory is present and populated

---

## Architecture

### System Overview

```
[Developer/Agent CLI]
    |
    v
[Engineering Skills Repository]
    |
    +-> [Domain: Architecture] -> [Skill: system-designer, database-schema]
    +-> [Domain: DevOps]       -> [Skill: ci-cd-builder, terraform-expert]
    +-> [Domain: Dev Tools]    -> [Skill: codebase-onboarding, llm-wiki]
    +-> [Domain: Atlassian]    -> [Skill: jira-expert, confluence-expert]
```

### Tech Stack

| Layer | Technology | Why |
|-------|-----------|-----|
| Skill Definitions | Markdown (SKILL.md) | Human-readable and agent-parseable |
| Automation | Python / Shell | Cross-platform scripting |
| Documentation | MkDocs | Static site generation for skills catalog |
| CI/CD | GitHub Actions | Quality gates and skill validation |

---

## Key Files

| Path | Purpose |
|------|---------|
| `GEMINI.md` | Core project instructions and agent context |
| `CORPUS_MAP.md` | Auto-generated semantic map of all 180 remaining skills |
| `SKILL-AUTHORING-STANDARD.md` | Requirements for adding new skills |
| `engineering/skills/` | Deep technical and developer experience skills |
| `project-management/skills/`| Restored Atlassian tool integrations |
| `.gemini/skills-index.json` | The active registry of available skills |

---

## Common Developer Tasks

### Add a New Dev Tool Skill

Follow the `SKILL-AUTHORING-STANDARD.md` and use the `skill-creator` skill.

```bash
# Example: Use the skill-creator (if available in your agent)
"Create a new skill for 'rust-cargo-optimizer'"
```

### Explore the Codebase

```bash
python3 engineering/skills/codebase-onboarding/scripts/codebase_analyzer.py .
```

---

## Contribution Guidelines

### Skill Addition Process

1. Create a new branch `feat/skill-name`.
2. Follow the authoring standard in `SKILL-AUTHORING-STANDARD.md`.
3. Ensure `SKILL.md` is present in the skill's root directory.
4. Update relevant index files.

### Commit Convention

- `feat(engineering): add new skill-name`
- `fix(skill): resolve issue in skill-name`
- `docs: update documentation`
