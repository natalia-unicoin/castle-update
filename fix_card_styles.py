import re

def update_cards(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    # The current inline style is:
    # style="aspect-ratio: 4/5 !important; text-decoration: none; display: block; position: relative; overflow: hidden; border-radius: 8px; transition: transform 0.3s; box-shadow: 0 4px 20px rgba(0,0,0,0.2);"
    old_style = 'style="aspect-ratio: 4/5 !important; text-decoration: none; display: block; position: relative; overflow: hidden; border-radius: 8px; transition: transform 0.3s; box-shadow: 0 4px 20px rgba(0,0,0,0.2);"'
    new_style = 'style="aspect-ratio: 4/5 !important; text-decoration: none; display: block; position: relative; overflow: hidden; border-radius: 0 !important; box-shadow: none !important; transition: transform 0.3s;"'
    
    html = html.replace(old_style, new_style)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)
        print(f"Updated {filepath}")

update_cards('contact_es.html')
update_cards('contact.html')

