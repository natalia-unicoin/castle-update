import re

def update_eco(filepath, is_spanish):
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    # Define replacement strings
    if is_spanish:
        old_title = r'Únete al Ecosistema que está transformando la riqueza femenina'
        new_title = r'Únete al Ecosistema que está transformando la <span style="font-family: \'Caveat\', cursive; font-size: 1.4em; color: #A03FA3; font-weight: 400; text-transform: lowercase;">riqueza femenina</span>'
    else:
        old_title = r'Join the Ecosystem transforming female wealth'
        new_title = r'Join the Ecosystem transforming <span style="font-family: \'Caveat\', cursive; font-size: 1.4em; color: #A03FA3; font-weight: 400; text-transform: lowercase;">female wealth</span>'

    # Update Title
    html = re.sub(old_title, new_title, html)

    # Update Section container
    # <section style="background-color: #1A1A1A; padding: var(--section-pad-y) 0; overflow: hidden; text-align: center;">
    html = re.sub(
        r'<section style="background-color: #1A1A1A; padding: var\(--section-pad-y\) 0; overflow: hidden; text-align: center;">',
        r'<section style="background-color: #6B7280; background-size: cover; background-position: center; min-height: 100vh; display: flex; flex-direction: column; justify-content: center; padding: var(--section-pad-y) 0; overflow: hidden; text-align: center;">',
        html
    )

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)
        print(f"Updated {filepath}")

update_eco('contact_es.html', True)
update_eco('contact.html', False)

