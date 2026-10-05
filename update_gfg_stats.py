import urllib.request
import re
import sys

def get_html(url):
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    return urllib.request.urlopen(req).read().decode('utf-8')

def main():
    username = 'armaanalam'
    try:
        # Fetch broken SVG from API
        svg = get_html(f'https://gfgstatscard.vercel.app/{username}?theme=dark')
        
        # Fetch GFG Profile HTML
        html = get_html(f'https://auth.geeksforgeeks.org/user/{username}')
        
        # Scrape Total Problems Solved
        m_prob = re.findall(r'"[^"]*problems?[^"]*"\s*:\s*(\d+)', html, re.IGNORECASE)
        problems_solved = m_prob[0] if m_prob else "0"
        
        # Scrape Coding Score (often near problems solved, or in a similar json block)
        m_score = re.findall(r'"[^"]*score[^\w"]*"\s*:\s*(\d+)', html, re.IGNORECASE)
        coding_score = m_score[0] if m_score else "0"
        
        print(f"Scraped - Problems: {problems_solved}, Score: {coding_score}")
        
        # Replace broken fields in SVG
        svg = re.sub(r'<text id="total-solved-count">_ _</text>', f'<text id="total-solved-count">{problems_solved}</text>', svg)
        svg = re.sub(r'<text id="overall-score-count">_ _</text>', f'<text id="overall-score-count">{coding_score}</text>', svg)
        # Assuming monthly score isn't easily scrapeable, just default to 0
        svg = re.sub(r'<text id="month-score-count">_ _', f'<text id="month-score-count">0', svg)
        
        with open('gfg-stats.svg', 'w', encoding='utf-8') as f:
            f.write(svg)
            
    except Exception as e:
        print(f"Error updating stats: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()
