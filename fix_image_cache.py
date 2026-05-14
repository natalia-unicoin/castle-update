import re

def update_cache(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    # Change card-masterclass.jpg to card-masterclass.jpg?v=3
    html = html.replace('card-masterclass.jpg', 'card-masterclass.jpg?v=3')
    # If there's already ?v=2, it will become ?v=2?v=3 which is messy.
    html = re.sub(r'card-masterclass\.jpg(\?v=\d+)?', 'card-masterclass.jpg?v=3', html)
    html = re.sub(r'card-partners\.jpg(\?v=\d+)?', 'card-partners.jpg?v=3', html)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)
        print(f"Updated {filepath}")

update_cache('contact_es.html')
update_cache('contact.html')

