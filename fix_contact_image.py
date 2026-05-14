import re

def update_bg_image(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    # Change hero-silvina.jpg to hero-contact.jpg
    html = html.replace("url('./public/images/common/hero-silvina.jpg')", "url('./public/images/common/hero-contact.jpg')")

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)
        print(f"Updated {filepath}")

update_bg_image('contact_es.html')
update_bg_image('contact.html')

