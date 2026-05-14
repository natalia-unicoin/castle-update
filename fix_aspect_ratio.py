import re

def update_aspect_ratio(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    # The cards currently have aspect-ratio: 4/5 !important;
    html = html.replace('aspect-ratio: 4/5 !important;', 'aspect-ratio: 3/2 !important;')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)
        print(f"Updated {filepath}")

update_aspect_ratio('contact_es.html')
update_aspect_ratio('contact.html')

