import urllib.request
import json
import os
import re

def get_repos():
    req = urllib.request.Request(
        'https://api.github.com/users/ArmaanAlam/repos?sort=updated&per_page=50',
        headers={'User-Agent': 'Mozilla/5.0'}
    )
    res = urllib.request.urlopen(req)
    data = json.loads(res.read().decode('utf-8'))
    
    # Filter out forks and the profile repository itself
    repos = [r for r in data if not r['fork'] and r['name'] != 'ArmaanAlam']
    return repos[:5] # Top 5 latest working repos

def generate_table(repos):
    html = '<table width="100%">\n'
    for i in range(0, len(repos), 3):
        row = repos[i:i+3]
        html += '  <tr>\n'
        for repo in row:
            html += f'''    <td width="33%" valign="top">
      <a href="{repo['html_url']}">
        <img src="https://github-readme-stats.vercel.app/api/pin/?username=ArmaanAlam&repo={repo['name']}&title_color=4ade80&text_color=c9d1d9&icon_color=4ade80&bg_color=0d1117&border_color=30363d" width="100%" alt="{repo['name']}" />
      </a>
    </td>\n'''
        # fill empty cells if row < 3
        for _ in range(3 - len(row)):
            html += '    <td width="33%"></td>\n'
        html += '  </tr>\n'
    html += '</table>'
    return html

def update_readme():
    repos = get_repos()
    table_html = generate_table(repos)
    
    with open('README.md', 'r', encoding='utf-8') as f:
        content = f.read()
        
    start_marker = '<!-- START_SECTION:featured_projects -->'
    end_marker = '<!-- END_SECTION:featured_projects -->'
    
    pattern = re.compile(f'{start_marker}.*?{end_marker}', re.DOTALL)
    new_content = pattern.sub(f'{start_marker}\n{table_html}\n{end_marker}', content)
    
    with open('README.md', 'w', encoding='utf-8') as f:
        f.write(new_content)

if __name__ == '__main__':
    update_readme()
