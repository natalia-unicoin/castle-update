import re

def update_eco(filepath, is_spanish):
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    # Define replacement strings for text
    if is_spanish:
        old_title = r'Únete al Ecosistema que está transformando la <span style="font-family: \'Caveat\', cursive; font-size: 1.4em; color: #A03FA3; font-weight: 400; text-transform: lowercase;">riqueza femenina</span>'
        new_title = r'Únete al Ecosistema<br>que está transformando<br><span style="font-family: \'Caveat\', cursive; font-size: 1.6em; color: #A03FA3; font-weight: 400; text-transform: lowercase; display: inline-block; margin-top: 5px;">la riqueza femenina</span>'
    else:
        old_title = r'Join the Ecosystem transforming <span style="font-family: \'Caveat\', cursive; font-size: 1.4em; color: #A03FA3; font-weight: 400; text-transform: lowercase;">female wealth</span>'
        new_title = r'Join the Ecosystem<br>transforming<br><span style="font-family: \'Caveat\', cursive; font-size: 1.6em; color: #A03FA3; font-weight: 400; text-transform: lowercase; display: inline-block; margin-top: 5px;">female wealth</span>'

    html = html.replace(old_title, new_title)

    # Add parallax (background-attachment: fixed) to the section
    old_section = r'<section style="background-color: #6B7280; background-size: cover; background-position: center; min-height: 100vh; display: flex; flex-direction: column; justify-content: center; padding: var(--section-pad-y) 0; overflow: hidden; text-align: center;">'
    new_section = r'<section style="background-color: #6B7280; background-size: cover; background-position: center; background-attachment: fixed; min-height: 100vh; display: flex; flex-direction: column; justify-content: center; padding: var(--section-pad-y) 0; overflow: hidden; text-align: center;">'
    
    html = html.replace(old_section, new_section)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)
        print(f"Updated {filepath}")

update_eco('contact_es.html', True)
update_eco('contact.html', False)

