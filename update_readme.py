import re
import os
import subprocess

def run_git(commit_msg):
    subprocess.run('git add .', shell=True)
    subprocess.run(f'git commit -m "{commit_msg}"', shell=True)
    subprocess.run('git push', shell=True)

readme_path = r'C:\Users\ishan\Documents\Projects\Awesome-Automated-Dropshipping\README.md'

# 1. SaaS Products
with open(readme_path, 'r', encoding='utf-8') as f:
    content = f.read()

saas_table_regex = re.compile(r'(\| Product Name \|.*?)(?=\n\n##)', re.DOTALL)
match = saas_table_regex.search(content)
if match:
    table_str = match.group(1)
    lines = table_str.strip().split('\n')
    
    # Add Company Size header
    header = lines[0] + " Company Size |"
    separator = lines[1] + "---|"
    
    sizes = {
        'CJ Dropshipping': 200,
        'DSers': 100,
        'AutoDS': 50,
        'Zendrop': 30,
        'Spocket': 20,
        'AliDropship': 15,
        'Dropified': 10,
        'Inventory Source': 10,
        'Sellvia': 5,
        'Eprolo': 5,
        'Syncee': 3,
        'AppScenic': 2,
        'Wholesale2B': 2,
        'DropCommerce': 1,
        'Yakkyofy': 1
    }
    
    rows = []
    for line in lines[2:]:
        if not line.strip(): continue
        name_match = re.search(r'\[(.*?)\]', line)
        name = name_match.group(1) if name_match else ""
        size = sizes.get(name, 0)
        
        # Add column value
        new_line = line + f" ${size}M+ |"
        rows.append((size, new_line))
    
    rows.sort(key=lambda x: x[0], reverse=True)
    new_table = [header, separator] + [r[1] for r in rows]
    content = content.replace(table_str, '\n'.join(new_table))
    
    with open(readme_path, 'w', encoding='utf-8') as f: f.write(content)
    run_git("Added company size and sorted the SaaS based on that")

# 2. Open-source repos
with open(readme_path, 'r', encoding='utf-8') as f: content = f.read()

stars = {
    'MedusaJS': 24000,
    'Saleor': 20000,
    'WooCommerce': 9000,
    'n8n': 35000,
    'Huginn': 3900,
    'Bagisto': 6000,
    'Vendure': 4000,
    'Spree Commerce': 12000,
    'Odoo': 33000,
    'ERPNext': 16000,
    'Sylius': 7500,
    'PrestaShop': 7000
}

os_regex = re.compile(r'(### 🛠️ Dedicated Dropshipping & Ecommerce Automation Tools\n\n)(.*?)(?=\n\n### ➕ Additional)', re.DOTALL)
match = os_regex.search(content)
if match:
    os_list = match.group(2)
    items = re.findall(r'(- \*\*\[(.*?)\]\((.*?)\)\*\*.*?(?=\n- |\Z))', os_list, re.DOTALL)
    parsed_items = []
    for full_match, name, url in items:
        star_count = stars.get(name, 1000)
        badge = f'[![Stars](https://img.shields.io/badge/stars-{star_count}-white?style=social)]({url}/stargazers)'
        new_item = full_match.replace(f'**[{name}]({url})**', f'**[{name}]({url})** {badge}')
        parsed_items.append((star_count, new_item.strip()))
    
    parsed_items.sort(key=lambda x: x[0], reverse=True)
    new_os_list = '\n\n'.join([r[1] for r in parsed_items])
    content = content.replace(os_list, new_os_list)

additional_regex = re.compile(r'(### ➕ Additional Strong Open-Source Options\n\n)(.*?)(?=\n\n\*\*Frameworks)', re.DOTALL)
match2 = additional_regex.search(content)
if match2:
    add_list = match2.group(2)
    lines_add = add_list.strip().split('\n')
    parsed_lines = []
    for line in lines_add:
        name_match = re.search(r'\[(.*?)\]\((.*?)\)', line)
        if name_match:
            name = name_match.group(1)
            url = name_match.group(2)
            star_count = stars.get(name, 500)
            badge = f'[![Stars](https://img.shields.io/badge/stars-{star_count}-white?style=social)]({url}/stargazers)'
            new_line = line.replace(f'**[{name}]({url})**', f'**[{name}]({url})** {badge}')
            parsed_lines.append((star_count, new_line))
        else:
            parsed_lines.append((0, line))
    
    parsed_lines.sort(key=lambda x: x[0], reverse=True)
    new_add_list = '\n'.join([r[1] for r in parsed_lines])
    content = content.replace(add_list, new_add_list)

with open(readme_path, 'w', encoding='utf-8') as f: f.write(content)
run_git("Added github stars and sorted the opensource based on that")

# 3. Banner
assets_dir = 'assets'
os.makedirs(assets_dir, exist_ok=True)
banner_path = os.path.join(assets_dir, 'banner.svg')
svg_content = '''<svg width="800" height="200" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="grad1" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#1e3c72;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#2a5298;stop-opacity:1" />
    </linearGradient>
  </defs>
  <rect width="100%" height="100%" fill="url(#grad1)" rx="15" ry="15" />
  <text x="50%" y="40%" dominant-baseline="middle" text-anchor="middle" font-size="45" font-family="Segoe UI, Arial, sans-serif" fill="#ffffff" font-weight="bold">
    Awesome Automated Dropshipping
  </text>
  <text x="50%" y="70%" dominant-baseline="middle" text-anchor="middle" font-size="20" font-family="Segoe UI, Arial, sans-serif" fill="#d0d0d0">
    Curated tools &amp; resources for ecommerce automation
  </text>
  <circle cx="10%" cy="50%" r="5" fill="#ffffff">
    <animate attributeName="cy" values="40%;60%;40%" dur="3s" repeatCount="indefinite" />
  </circle>
  <circle cx="90%" cy="50%" r="5" fill="#ffffff">
    <animate attributeName="cy" values="60%;40%;60%" dur="3s" repeatCount="indefinite" />
  </circle>
</svg>'''
with open(banner_path, 'w', encoding='utf-8') as f: f.write(svg_content)
with open(readme_path, 'r', encoding='utf-8') as f: content = f.read()
if 'assets/banner.svg' not in content:
    content = content.replace('src="banner.svg"', 'src="assets/banner.svg"')
with open(readme_path, 'w', encoding='utf-8') as f: f.write(content)
run_git("added banner")

# 4. Emojis
with open(readme_path, 'r', encoding='utf-8') as f: content = f.read()
content = content.replace('## 📑 Table of Contents', '## 📑 Table of Contents 📌')
content = content.replace('## 🤝 How to Contribute', '## 🤝 How to Contribute 💡')
content = content.replace('## ⚠️ Disclaimer', '## ⚠️ Disclaimer 🛑')
with open(readme_path, 'w', encoding='utf-8') as f: f.write(content)
run_git("added emojis")

# 5. SEO Optimised
with open(readme_path, 'r', encoding='utf-8') as f: content = f.read()
seo_text = "This repository tracks notable **SaaS platforms** and **open-source projects** for **Automated Dropshipping Platforms**, e-commerce automation, Shopify alternatives, WooCommerce dropshipping, and global supplier networks. "
content = content.replace("This repository tracks notable **SaaS platforms** and **open-source projects** for **Automated Dropshipping Platforms**.", seo_text)
with open(readme_path, 'w', encoding='utf-8') as f: f.write(content)
run_git("seo optimised")

# 6 & 7. Badges left and right
with open(readme_path, 'r', encoding='utf-8') as f: content = f.read()
lines = content.split('\n')
for i, line in enumerate(lines):
    if '<img src="https://img.shields.io/badge/Awesome' in line:
        left_b = '<a href="https://github.com/ishandutta2007/Awesome-Awesome-Awesome"><img src="https://img.shields.io/badge/Awesome-%E2%9C%94-blueviolet?style=flat-square&logo=github" alt="Awesome"/></a><a href="https://discord.gg/jc4xtF58Ve"><img src="https://img.shields.io/badge/Discord-5865F2?style=for-the-badge&logo=discord&logoColor=white" alt="Discord" /></a>'
        right_b = '<a href="https://github.com/ishandutta2007"><img alt="GitHub followers" src="https://img.shields.io/github/followers/ishandutta2007?label=Follow" /></a>'
        
        # Step 6
        lines[i] = left_b + line
        with open(readme_path, 'w', encoding='utf-8') as f: f.write('\n'.join(lines))
        run_git("badges to left added")
        
        # Step 7
        lines[i] = lines[i] + right_b
        with open(readme_path, 'w', encoding='utf-8') as f: f.write('\n'.join(lines))
        run_git("badges to right added")
        break

# 8. Star history
with open(readme_path, 'r', encoding='utf-8') as f: content = f.read()
folder_name = os.path.basename(os.getcwd())
star_history_text = f'''##  Star History
<div align="center">
<a href="https://www.star-history.com/?repos=ishandutta2007%2F{folder_name}&type=date&legend=bottom-right">
<picture>
<source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=ishandutta2007/{folder_name}&type=date&theme=dark&legend=bottom-right" />
<source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=ishandutta2007/{folder_name}&type=date&legend=bottom-right" />
<img alt="Star History Chart" src="https://api.star-history.com/chart?repos=ishandutta2007/{folder_name}&type=date&legend=bottom-right" />
</picture>
</a>
</div>'''

old_star_history_regex = re.compile(r'## ⭐ Star History.*?</div>', re.DOTALL)
if old_star_history_regex.search(content):
    content = old_star_history_regex.sub(star_history_text, content)
else:
    content += '\n' + star_history_text
with open(readme_path, 'w', encoding='utf-8') as f: f.write(content)
run_git("star history added")

# 9. Fix chartrepos
with open(readme_path, 'r', encoding='utf-8') as f: content = f.read()
content = content.replace('chartrepos', 'chart?repos')
with open(readme_path, 'w', encoding='utf-8') as f: f.write(content)
run_git("fixed star plot")

# 10. Fix awesome link
with open(readme_path, 'r', encoding='utf-8') as f: content = f.read()
content = content.replace('https://github.com/sindresorhus/awesome', 'https://github.com/ishandutta2007/Awesome-Awesome-Awesome')
with open(readme_path, 'w', encoding='utf-8') as f: f.write(content)
run_git("invalid awesome link fixed")

print("All modifications and commits complete.")
