import re

def generate_table(repos):
    html = '<table width="100%">\n'
    for i in range(0, len(repos), 2):
        row = repos[i:i+2]
        html += '  <tr>\n'
        for repo in row:
            html += f'''    <td width="50%" valign="top">
      <a href="https://github.com/ArmaanAlam/{repo}">
        <img src="https://github-readme-stats.vercel.app/api/pin/?username=ArmaanAlam&repo={repo}&title_color=4ade80&text_color=c9d1d9&icon_color=4ade80&bg_color=0d1117&border_color=30363d" width="100%" alt="{repo}" />
      </a>
    </td>\n'''
        # fill empty cells if row < 2
        for _ in range(2 - len(row)):
            html += '    <td width="50%"></td>\n'
        html += '  </tr>\n'
    html += '</table>'
    return html

def update_readme():
    repos = [
        'CodeBase-Assistant',
        'Transformer-from-Scratch',
        'NLP-to-SQL-Language-Conversion',
        'Production-RAG'
    ]
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
