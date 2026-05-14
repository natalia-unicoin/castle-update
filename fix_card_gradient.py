import re

def update_gradients(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    # The current gradient is:
    # background: linear-gradient(to top, rgba(0,0,0,0.95) 0%, rgba(0,0,0,0.2) 60%)
    old_grad = 'background: linear-gradient(to top, rgba(0,0,0,0.95) 0%, rgba(0,0,0,0.2) 60%);'
    new_grad = 'background: linear-gradient(to top, rgba(0,0,0,0.9) 0%, rgba(0,0,0,0) 60%);'
    
    html = html.replace(old_grad, new_grad)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)
        print(f"Updated {filepath}")

update_gradients('contact_es.html')
update_gradients('contact.html')

