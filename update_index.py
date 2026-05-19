import json

with open('.gemini/skills-index.json', 'r') as f:
    data = json.load(f)

# Keep only engineering related agents and skills
new_skills = []
for item in data.get('skills', []):
    cat = item.get('category', '').lower()
    name = item.get('name', '').lower()
    source = item.get('source', '').lower()
    
    # Check if the skill belongs to an eliminated domain
    is_eliminated = False
    eliminated_domains = ['business-growth', 'business-operations', 'c-level', 'commercial', 'compliance-os', 'finance', 'marketing', 'product', 'project-management', 'ra-qm']
    
    for domain in eliminated_domains:
        if domain in source or domain in name or domain in cat:
            is_eliminated = True
            break
            
    # Explicit exclusions based on agent names that were deleted
    if name in ['cs-growth-strategist', 'cs-ceo-advisor', 'cs-cto-advisor', 'cs-financial-analyst', 'cs-aeo', 'cs-content-creator', 'cs-demand-gen-specialist', 'cs-agile-product-owner', 'cs-product-analyst', 'cs-product-manager', 'cs-product-strategist', 'cs-ux-researcher', 'cs-project-manager', 'cs-quality-regulatory']:
        is_eliminated = True
        
    if not is_eliminated:
        new_skills.append(item)

data['skills'] = new_skills
data['total_skills'] = len(new_skills)

with open('.gemini/skills-index.json', 'w') as f:
    json.dump(data, f, indent=2)

print(f"Updated skills-index.json. Reduced to {len(new_skills)} skills.")
