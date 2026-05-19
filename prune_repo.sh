#!/bin/bash
echo "Pruning unselected domains..."

# Directories to remove based on user elimination
DIRS_TO_REMOVE=(
    "business-growth"
    "business-operations"
    "c-level-advisor"
    "commercial"
    "compliance-os"
    "finance"
    "marketing"
    "marketing-skill"
    "product-team"
    "project-management"
    "ra-qm-team"
    "agents/business-growth"
    "agents/c-level"
    "agents/finance"
    "agents/marketing"
    "agents/product"
    "agents/project-management"
    "agents/ra-qm-team"
    ".gemini/skills/cs-aeo"
    ".gemini/skills/cmd-cs-aeo"
)

for dir in "${DIRS_TO_REMOVE[@]}"; do
    if [ -d "$dir" ]; then
        echo "Removing $dir..."
        rm -rf "$dir"
    fi
done

echo "Done."
