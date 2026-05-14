import re

def empty_third_card(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    # The image path is mc-bg2.jpg in the third card.
    html = html.replace('<img src="./public/images/common/mc-bg2.jpg" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; object-fit: cover; z-index: 1;">', '')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)
        print(f"Updated {filepath}")

empty_third_card('contact_es.html')
empty_third_card('contact.html')

