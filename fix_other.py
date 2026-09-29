import re

files_to_update = {
    'despair.html': {
        'max_width': '720px',
        'has_image': True,
    },
    'hitting-walls.html': {
        'max_width': '980px',
        'has_image': False,
    }
}

for filename, config in files_to_update.items():
    new_css = f"""  <style>
    * {{ margin: 0; padding: 0; box-sizing: border-box; }}

    :root {{
      --bg: #ffffff;
      --text: #111111;
      --muted: #666666;
      --link: #111111;
    }}

    [data-theme="dark"] {{
      --bg: #111111;
      --text: #eeeeee;
      --muted: #888888;
      --link: #eeeeee;
    }}

    @media (prefers-reduced-motion: reduce) {{
      * {{
        animation-duration: 0.01ms !important;
        animation-iteration-count: 1 !important;
        transition-duration: 0.01ms !important;
        scroll-behavior: auto !important;
      }}
    }}

    body {{
      background: var(--bg);
      color: var(--text);
      font-family: 'EB Garamond', Georgia, serif;
      font-size: clamp(1.1rem, 1rem + 1vw, 1.38rem);
      line-height: 1.9;
      transition: background 0.2s, color 0.2s;
      overflow-x: hidden;
      -webkit-font-smoothing: antialiased;
      text-rendering: optimizeLegibility;
    }}

    .wrap {{
      width: 100%;
      max-width: {config['max_width']};
      margin: 0 auto;
      padding: clamp(3rem, 5vw, 5rem) clamp(1.2rem, 4vw, 2rem) clamp(4rem, 6vw, 6rem);
    }}

    nav {{
      display: flex;
      flex-wrap: wrap;
      gap: 1rem 1.5rem;
      margin-bottom: clamp(2rem, 4vw, 3rem);
      font-size: 1rem;
    }}

    nav a {{
      color: var(--muted);
      text-decoration: none;
      padding: 0.5rem 0;
    }}

    nav a:hover,
    nav a.active {{
      color: var(--text);
    }}

    h1 {{
      font-size: clamp(1.8rem, 1.5rem + 2vw, 2.8rem);
      font-weight: 500;
      margin-bottom: 0.5rem;
      letter-spacing: -0.01em;
    }}

    .meta {{
      color: var(--muted);
      font-style: italic;
      font-size: 1rem;
      margin-bottom: clamp(2rem, 4vw, 3rem);
    }}

    p {{
      margin-bottom: clamp(1.5rem, 3vw, 2rem);
      max-width: 100%;
      word-break: break-word;
      overflow-wrap: break-word;
    }}

    a {{
      color: var(--link);
      text-decoration: underline;
      text-underline-offset: 3px;
      text-decoration-color: #aaaaaa;
      word-break: break-word;
      overflow-wrap: break-word;
    }}

    .toggle {{
      position: fixed;
      top: 1rem;
      right: 1rem;
      background: var(--bg);
      border: 1px solid var(--muted);
      color: var(--muted);
      font-family: inherit;
      font-size: 1rem;
      padding: 0;
      width: 44px;
      height: 44px;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      border-radius: 4px;
      transition: color 0.2s, border-color 0.2s, background 0.2s;
      z-index: 1000;
    }}

    .toggle:hover, .toggle:focus {{
      color: var(--text);
      border-color: var(--text);
      outline: none;
    }}
  </style>"""

    with open(filename, 'r') as f:
        content = f.read()
    
    content = re.sub(r'<style>.*?</style>', new_css, content, flags=re.DOTALL)
    
    if config['has_image']:
        content = content.replace('style="width:100%;', 'style="max-width:100%;height:auto;')
        
    # Check for duplicate media query at the end in hitting-walls
    content = re.sub(r'@media \(max-width: 768px\).*?\}', '', content, flags=re.DOTALL)
    
    with open(filename, 'w') as f:
        f.write(content)
