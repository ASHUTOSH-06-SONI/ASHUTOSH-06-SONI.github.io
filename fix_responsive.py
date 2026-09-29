import re

# Base mobile-first CSS template to inject.
# We'll customize it for each file.
def fix_index():
    with open('index.html', 'r') as f:
        content = f.read()

    new_css = """
    * { margin: 0; padding: 0; box-sizing: border-box; }

    :root {
      --bg: #ffffff;
      --text: #111111;
      --muted: #666666;
      --link: #111111;
    }

    [data-theme="dark"] {
      --bg: #111111;
      --text: #eeeeee;
      --muted: #888888;
      --link: #eeeeee;
    }

    @media (prefers-reduced-motion: reduce) {
      * {
        animation-duration: 0.01ms !important;
        animation-iteration-count: 1 !important;
        transition-duration: 0.01ms !important;
        scroll-behavior: auto !important;
      }
    }

    body {
      background: var(--bg);
      color: var(--text);
      font-family: 'EB Garamond', Georgia, serif;
      font-size: clamp(1.1rem, 1rem + 0.5vw, 1.25rem);
      line-height: 1.8;
      transition: background 0.2s, color 0.2s;
      overflow-x: hidden;
    }

    .wrap {
      width: 100%;
      max-width: 1000px;
      margin: 0 auto;
      padding: clamp(3rem, 5vw, 5rem) clamp(1.2rem, 4vw, 1.5rem) clamp(4rem, 6vw, 6rem);
    }

    h1 {
      font-size: clamp(1.8rem, 1.5rem + 1.5vw, 2.2rem);
      font-weight: 500;
      margin-bottom: 0.15rem;
      letter-spacing: -0.01em;
    }

    .tagline {
      color: var(--muted);
      font-style: italic;
      font-size: clamp(0.9rem, 0.8rem + 0.5vw, 1rem);
      margin-bottom: clamp(1.5rem, 3vw, 2.5rem);
    }

    p { margin-bottom: 1rem; word-break: break-word; overflow-wrap: break-word; }

    h2 {
      font-size: clamp(0.9rem, 0.8rem + 0.5vw, 1rem);
      font-weight: 500;
      letter-spacing: 0.15em;
      text-transform: uppercase;
      color: var(--muted);
      margin: clamp(1.5rem, 4vw, 2.5rem) 0 0.8rem;
      font-family: Georgia, serif;
    }

    ul {
      list-style: none;
      padding: 0;
    }

    ul ul {
      margin-left: 1.5rem;
    }

    ul li {
      padding: 0.2rem 0;
    }

    ul li::before {
      content: "– ";
      color: var(--muted);
    }

    a {
      color: var(--link);
      text-decoration: underline;
      text-underline-offset: 3px;
      text-decoration-color: #aaaaaa;
      word-break: break-word;
      overflow-wrap: break-word;
      display: inline-block;
      padding: 0.1rem 0;
    }

    a:hover {
      text-decoration-color: var(--text);
    }

    .info-grid {
      display: grid;
      grid-template-columns: 1fr;
      gap: 2rem;
      align-items: start;
      margin-top: 1.5rem;
    }

    @media (min-width: 768px) {
      .info-grid {
        grid-template-columns: minmax(0, 1.2fr) minmax(0, 1fr);
        gap: 0;
      }
    }

    .info-panel {
      padding: 0;
    }

    @media (min-width: 768px) {
      .info-panel {
        padding: 0 1.5rem 0 0;
      }
      .info-panel + .info-panel {
        padding-left: 1.5rem;
        padding-right: 0;
      }
      .info-panel + .info-panel::before {
        content: "";
        position: absolute;
        top: 0;
        bottom: 0;
        left: 0;
        width: 1px;
        background: #d6d6d6;
      }
      [data-theme="dark"] .info-panel + .info-panel::before {
        background: #333333;
      }
    }

    .info-panel + .info-panel {
      position: relative;
    }

    .project-grid {
      display: grid;
      grid-template-columns: 1fr;
      gap: 1rem;
      margin-top: 0.7rem;
    }

    @media (min-width: 480px) {
      .project-grid {
        grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
      }
    }

    .project-card {
      display: block;
      text-decoration: none;
      color: var(--text);
      transition: opacity 0.2s ease;
      padding: 0.5rem 0;
    }

    .project-card:hover {
      opacity: 0.8;
    }

    .project-card strong {
      display: block;
      font-weight: 500;
      margin-bottom: 0.2rem;
    }

    .project-card span {
      color: var(--muted);
      font-size: 0.9rem;
      line-height: 1.45;
    }

    .socials {
      display: flex;
      flex-wrap: wrap;
      gap: 0.5rem 1.5rem;
      margin-top: 0.4rem;
    }

    .socials a {
      font-size: clamp(0.95rem, 0.9rem + 0.5vw, 1rem);
      padding: 0.3rem 0;
    }

    .toggle {
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
    }

    .toggle:hover, .toggle:focus { color: var(--text); border-color: var(--text); outline: none; }

    [data-theme="dark"] hr { border-top-color: #2a2a2a; }

    .blog-date {
      color: var(--muted);
      font-size: 0.9rem;
      font-style: italic;
    }
"""

    content = re.sub(r'<style>.*?</style>', f'<style>\n{new_css}</style>', content, flags=re.DOTALL)
    
    # Ensure viewport meta tag is exact
    viewport_meta = '<meta name="viewport" content="width=device-width, initial-scale=1.0">'
    content = re.sub(r'<meta name="viewport" content=".*?">', viewport_meta, content)

    with open('index.html', 'w') as f:
        f.write(content)

fix_index()
