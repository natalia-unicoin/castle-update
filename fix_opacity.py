import re

def lighten_overlays(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Ecosystem Gradient
    html = html.replace(
        'background: linear-gradient(to top, rgba(17,17,17,0.95) 0%, rgba(17,17,17,0.5) 50%, rgba(17,17,17,0) 100%);',
        'background: linear-gradient(to top, rgba(17,17,17,0.6) 0%, rgba(17,17,17,0) 60%);'
    )

    # 2. Hero Gradient
    html = html.replace(
        'background: linear-gradient(180deg, rgba(0,0,0,0) 0%, rgba(0,0,0,0.85) 100%);',
        'background: linear-gradient(180deg, rgba(0,0,0,0) 0%, rgba(0,0,0,0.4) 100%);'
    )

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)
        print(f"Updated {filepath}")

lighten_overlays('contact_es.html')
lighten_overlays('contact.html')

