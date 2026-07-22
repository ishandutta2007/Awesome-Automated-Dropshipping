import re
import os

repo_dir = r"C:\Users\ishan\Documents\Projects\Awesome-Automated-Dropshipping"
readme_path = os.path.join(repo_dir, 'README.md')
assets_dir = os.path.join(repo_dir, 'assets')

with open(readme_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace SaaS bullets with a table
saas_bullets_regex = re.compile(r'### Core Platforms \(Automated Dropshipping\)\n\n(.*?)(?=\n## Open-Source GitHub Projects)', re.DOTALL)
match = saas_bullets_regex.search(content)

if match:
    bullets_text = match.group(1)
    # Parse bullets
    items = []
    for bullet in bullets_text.split('\n\n'):
        if bullet.strip():
            lines = bullet.strip().split('\n')
            name_link = re.search(r'\[(.*?)\]\((.*?)\)', lines[0])
            desc = lines[1].strip() if len(lines) > 1 else ""
            if name_link:
                items.append({
                    'name': name_link.group(1),
                    'link': name_link.group(2),
                    'desc': desc
                })

    table = "### 🏢 Core Platforms (Automated Dropshipping)\n\n"
    table += "| Product Name | Description | Year First Used | Paper Link | Pricing | Free Tier Limits |\n"
    table += "|---|---|---|---|---|---|\n"
    for item in items:
        # Create detailed pages
        safe_name = re.sub(r'[^a-zA-Z0-9]', '_', item['name'])
        page_filename = f"{safe_name}.md"
        page_path = os.path.join(repo_dir, page_filename)
        page_content = f"# {item['name']}\n\n"
        page_content += f"## Detailed Information\n{item['desc']}\n\n"
        page_content += f"[Official Website]({item['link']})\n\n"
        page_content += "## Architecture Diagram\n\n"
        page_content += "```mermaid\nflowchart TD\n  A[Source] --> B[Processing]\n  B --> C[Destination]\n```\n"
        
        with open(page_path, 'w', encoding='utf-8') as pf:
            pf.write(page_content)
        
        table += f"| [{item['name']}]({item['link']}) | {item['desc']} [Details]({page_filename}) | N/A | N/A | Varies | N/A |\n"
    
    content = content[:match.start()] + table + "\n" + content[match.end():]

# Badges and Banner
# Create SVG Banner
os.makedirs(assets_dir, exist_ok=True)
svg_content = '''<svg width="800" height="200" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="grad1" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:rgb(255,255,0);stop-opacity:1" />
      <stop offset="100%" style="stop-color:rgb(255,0,0);stop-opacity:1" />
    </linearGradient>
  </defs>
  <rect width="100%" height="100%" fill="url(#grad1)" />
  <text x="50%" y="50%" dominant-baseline="middle" text-anchor="middle" font-size="40" font-family="Arial" fill="white">Awesome Automated Dropshipping</text>
  <circle cx="50" cy="50" r="20" fill="white">
    <animate attributeName="r" values="20;30;20" dur="2s" repeatCount="indefinite" />
  </circle>
</svg>'''
with open(os.path.join(assets_dir, 'banner.svg'), 'w', encoding='utf-8') as f:
    f.write(svg_content)

badges = '<div align="center">\n\n'
badges += '<a href="https://github.com/ishandutta2007/Awesome-Awesome-Awesome"><img src="https://img.shields.io/badge/Awesome-%E2%9C%94-blueviolet?style=flat-square&logo=github" alt="Awesome"/></a>'
badges += '<a href="https://discord.gg/jc4xtF58Ve"><img src="https://img.shields.io/badge/Discord-5865F2?style=for-the-badge&logo=discord&logoColor=white" alt="Discord" /></a>'
badges += '&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'
badges += '<a href="https://github.com/ishandutta2007"><img alt="GitHub followers" src="https://img.shields.io/github/followers/ishandutta2007?label=Follow" /></a>\n\n'
badges += '<img src="assets/banner.svg" alt="Banner"/>\n\n'
badges += '</div>\n\n'

# Add to top
content = re.sub(r'# Awesome-Automated-Dropshipping\n', f'# 🚀 Awesome-Automated-Dropshipping\n\n{badges}', content)

# Embellish headings with emojis
content = content.replace('## Top Automated Dropshipping Platforms Ecosystem', '## 🌟 Top Automated Dropshipping Platforms Ecosystem')
content = content.replace('## Table of Contents', '## 📑 Table of Contents')
content = content.replace('## SaaS Products', '## 🛒 SaaS Products')
content = content.replace('## Open-Source GitHub Projects', '## 💻 Open-Source GitHub Projects')
content = content.replace('### Dedicated Dropshipping & Ecommerce Automation Tools', '### 🛠️ Dedicated Dropshipping & Ecommerce Automation Tools')
content = content.replace('### Additional Strong Open-Source Options', '### ➕ Additional Strong Open-Source Options')
content = content.replace('## How to Contribute', '## 🤝 How to Contribute')
content = content.replace('## Disclaimer', '## ⚠️ Disclaimer')

# Star history
star_history = '''
## ⭐ Star History
<div align="center">
<a href="https://www.star-history.com/?repos=ishandutta2007/Awesome-Automated-Dropshipping&type=date&legend=bottom-right">
<picture>
<source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=ishandutta2007/Awesome-Automated-Dropshipping&type=date&theme=dark&legend=bottom-right" />
<source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=ishandutta2007/Awesome-Automated-Dropshipping&type=date&legend=bottom-right" />
<img alt="Star History Chart" src="https://api.star-history.com/chart?repos=ishandutta2007/Awesome-Automated-Dropshipping&type=date&legend=bottom-right" />
</picture>
</a>
</div>
'''

content = content.replace('---\n\n**Made for dropshippers', star_history + '\n\n---\n\n**Made for dropshippers')

# Fix links
content = content.replace('chartrepos', 'chart?repos')
content = content.replace('https://github.com/sindresorhus/awesome', 'https://github.com/ishandutta2007/Awesome-Awesome-Awesome')

with open(readme_path, 'w', encoding='utf-8') as f:
    f.write(content)
