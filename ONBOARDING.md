# Alireza Rezvani Skills Collection

> A comprehensive library of AI agent skills, prompts, and automation workflows for engineering, product, business operations, and executive leadership.

[![CI](https://github.com/alirezarezvani/claude-skills/actions/workflows/ci-quality-gate.yml/badge.svg)](https://github.com/alirezarezvani/claude-skills/actions)

## What is this?

This repository is a structured monorepo containing a vast collection of "skills" designed for AI agents (specifically Claude and Gemini). It serves as a centralized hub for specialized agentic workflows, prompts, and scripts that extend the capabilities of LLMs in professional environments.

---

## Quick Start

### Prerequisites

| Tool | Version | Install |
|------|---------|---------|
| Python | 3.8+ | `brew install python` |
| Git | 2.x | `brew install git` |

### Setup (2 minutes)

```bash
git clone https://github.com/alirezarezvani/claude-skills.git
cd claude-skills
# Optional: explore scripts
ls scripts/
```

### Verify it works

- [ ] Repository structure is visible
- [ ] `GEMINI.md` exists in the root
- [ ] At least one domain folder (e.g., `engineering/`) contains `skills/`

---

## Architecture

### System Overview

```
[User/Agent]
    |
    v
[Skills Repository]
    |
    +-> [Domain: Engineering] -> [Skill: codebase-onboarding]
    +-> [Domain: Product]     -> [Skill: prd-generator]
    +-> [Domain: Business]    -> [Skill: competitive-matrix]
    +-> [Domain: C-Level]     -> [Skill: cto-advisor]
```

### Tech Stack

| Layer | Technology | Why |
|-------|-----------|-----|
| Skill Definitions | Markdown (SKILL.md) | Human-readable and agent-parseable |
| Automation | Python | Cross-platform scripting |
| Documentation | MkDocs | Static site generation for skills catalog |
| CI/CD | GitHub Actions | Quality gates and skill validation |

---

## Key Files

| Path | Purpose |
|------|---------|
| `GEMINI.md` | Core project instructions and agent context |
| `SKILL-AUTHORING-STANDARD.md` | Requirements for adding new skills |
| `engineering/skills/` | Deep technical and developer experience skills |
| `business-operations/` | Operational and process automation skills |
| `.gemini/skills-index.json` | Registry of available skills for Gemini |
| `scripts/` | Shared utility scripts for skill execution |

---

## Common Developer Tasks

### Create a new skill

Follow the `SKILL-AUTHORING-STANDARD.md` and use the `skill-creator` skill.

```bash
# Example: Use the skill-creator (if available in your agent)
"Create a new skill for 'database-optimizer'"
```

### Run a codebase analysis

```bash
python3 engineering/skills/codebase-onboarding/scripts/codebase_analyzer.py .
```

---

## Debugging Guide

### Common Issues

- **Skill not found:** Check if the skill name matches the directory name and is indexed in `.gemini/skills-index.json`.
- **Script failures:** Ensure Python 3 is installed and all standard library modules are available.
- **MkDocs build errors:** Check `mkdocs.yml` for navigation inconsistencies.

---

## Contribution Guidelines

### Skill Addition Process

1. Create a new branch `feat/skill-name`.
2. Follow the authoring standard in `SKILL-AUTHORING-STANDARD.md`.
3. Ensure `SKILL.md` is present in the skill's root directory.
4. Update relevant index files.

### Commit Convention

- `feat(domain): add new skill-name`
- `fix(skill): resolve issue in skill-name`
- `docs: update documentation`

---

## Audience-Specific Notes

### Engineers
- Focus on `engineering/` and `engineering-team/` domains.
- Leverage `scripts/` for automating repetitive tasks.

### Product/Business Owners
- Explore `product-team/` and `business-growth/` for strategic alignment.

### Skill Authors
- Strictly adhere to `SKILL-AUTHORING-STANDARD.md` to maintain consistency across the library.
