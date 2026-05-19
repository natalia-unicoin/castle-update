import re

def fix_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Fix Caveat font
    html = html.replace("\\'Caveat\\'", "'Caveat'")

    # 2. Remove the hero overlay gradient
    # <div style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; background: linear-gradient(180deg, rgba(0,0,0,0) 0%, rgba(0,0,0,0.85) 100%); z-index: 1;"></div>
    overlay_pattern = r'<div style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; background: linear-gradient\(180deg, rgba\(0,0,0,0\) 0%, rgba\(0,0,0,0\.85\) 100%\); z-index: 1;"></div>'
    html = re.sub(overlay_pattern, '', html)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)
        print(f"Updated {filepath}")

fix_file('contact_es.html')
fix_file('contact.html')

