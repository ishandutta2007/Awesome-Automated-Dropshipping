import re

readme_path = r'C:\Users\ishan\Documents\Projects\Awesome-Automated-Dropshipping\README.md'

with open(readme_path, 'r', encoding='utf-8') as f:
    content = f.read()

saas_table_regex = re.compile(r'(\| Product Name \|.*?)(?=\n\n##)', re.DOTALL)
match = saas_table_regex.search(content)

if match:
    table_str = match.group(1)
    lines = table_str.strip().split('\n')
    
    new_lines = []
    for line in lines:
        parts = line.split('|')
        if len(parts) >= 8:
            # Parts array for a standard row has empty strings at 0 and -1:
            # ['', ' Product Name ', ' Description ', ' Year First Used ', ' Paper Link ', ' Pricing ', ' Free Tier Limits ', ' Company Size ', '']
            # So indices to drop: 3 and 4
            new_parts = parts[:3] + parts[5:]
            new_lines.append('|'.join(new_parts))
        else:
            new_lines.append(line)
            
    content = content.replace(table_str, '\n'.join(new_lines))
    
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Table updated successfully.")
else:
    print("SaaS table not found.")
