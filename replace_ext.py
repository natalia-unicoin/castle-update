import re

def fix(filename):
    with open(filename, 'r') as f:
        content = f.read()
    new_content = content.replace('ecosystem-sunset.png', 'ecosystem-sunset.jpg')
    with open(filename, 'w') as f:
        f.write(new_content)
    print(f"Updated {filename}")

fix('contact.html')
fix('contact_es.html')
