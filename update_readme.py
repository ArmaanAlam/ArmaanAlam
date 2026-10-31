import re

PROJECTS_DATA = {
    'NLP-to-SQL-Language-Conversion': {
        'icon': '💬',
        'title': 'NLP-to-SQL-Language-Conversion',
        'subtitle': 'Natural Language to Deterministic SQL Engine',
        'desc': 'Translates natural language into dialect-aware SQL with zero-shot schema linking, AST-level query validation, and safe read-only execution sandboxes.',
        'tags': '<code>Python</code> • <code>LangChain</code> • <code>PostgreSQL</code> • <code>FastAPI</code>'
    },
    'Production-RAG': {
        'icon': '🔄',
        'title': 'Production-RAG',
        'subtitle': 'Enterprise Retrieval-Augmented Generation',
        'desc': 'Production RAG architecture with hybrid vector + BM25 keyword search, reciprocal rank fusion (RRF), cross-encoder re-ranking, and low-latency chunk retrieval.',
        'tags': '<code>RAG</code> • <code>VectorDB</code> • <code>LangGraph</code> • <code>Pydantic</code>'
    },
    'CodeBase-Assistant': {
        'icon': '🧠',
        'title': 'CodeBase-Assistant',
        'subtitle': 'Intelligent Codebase Query & Refactor Agent',
        'desc': 'Navigates large code repositories, analyzes dependencies and call graphs, and answers architecture and debugging questions with full AST context.',
        'tags': '<code>LLMs</code> • <code>AST Parsing</code> • <code>Embeddings</code> • <code>Python</code>'
    },
    'Transformer-from-Scratch': {
        'icon': '⚡',
        'title': 'Transformer-from-Scratch',
        'subtitle': 'Pure PyTorch Transformer Implementation',
        'desc': 'Ground-up implementation of the seminal <i>"Attention Is All You Need"</i> paper, featuring multi-head self-attention, positional encoding, and complete training loops.',
        'tags': '<code>PyTorch</code> • <code>Deep Learning</code> • <code>Attention</code>'
    }
}

def generate_table(repos):
    html = '<table width="100%">\n'
    for i in range(0, len(repos), 2):
        row = repos[i:i+2]
        html += '  <tr>\n'
        for repo in row:
            info = PROJECTS_DATA.get(repo, {
                'icon': '📦',
                'title': repo,
                'subtitle': repo,
                'desc': 'Open source project by Armaan Alam.',
                'tags': '<code>AI</code> • <code>Backend</code>'
            })
            html += f'''    <td width="50%" valign="top">
      <h3>{info['icon']} <a href="https://github.com/ArmaanAlam/{repo}">{info['title']}</a></h3>
      <p><b>{info['subtitle']}</b><br/>
      {info['desc']}</p>
      {info['tags']}
    </td>\n'''
        for _ in range(2 - len(row)):
            html += '    <td width="50%"></td>\n'
        html += '  </tr>\n'
    html += '</table>'
    return html

def update_readme():
    repos = [
        'NLP-to-SQL-Language-Conversion',
        'Production-RAG',
        'CodeBase-Assistant',
        'Transformer-from-Scratch'
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
