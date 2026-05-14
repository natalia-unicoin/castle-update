import re

def update_resources(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Change section background
    html = html.replace('<section style="background-color: #1A1A1A; padding: var(--section-pad-y) 4vw;">', 
                        '<section style="background-color: #F8F8FA; padding: var(--section-pad-y) 4vw;">')
    
    # 2. Change title and subtitle colors
    html = html.replace('color: #FFFFFF;">Explora Castle</h2>', 'color: #1A1A1A;">Explora Castle</h2>')
    html = html.replace('color: #FFFFFF;">Explore Castle</h2>', 'color: #1A1A1A;">Explore Castle</h2>')
    html = html.replace('color: rgba(255,255,255,0.8);">Descubre todo lo que nuestro ecosistema tiene para ofrecerte.</p>',
                        'color: #4B5563;">Descubre todo lo que nuestro ecosistema tiene para ofrecerte.</p>')
    html = html.replace('color: rgba(255,255,255,0.8);">Discover everything our ecosystem has to offer.</p>',
                        'color: #4B5563;">Discover everything our ecosystem has to offer.</p>')

    # 3. Change aspect ratio back to 4/5 (tall)
    html = html.replace('aspect-ratio: 3/2 !important;', 'aspect-ratio: 4/5 !important;')

    # 4. Also wait, I changed aspect-ratio to 4/5, but let's make sure the width constraint on the grid makes sense for 4/5
    # `grid-template-columns: repeat(auto-fit, minmax(300px, 1fr))` with 3 items maxes out at 1/3 of the container. 
    # That's perfect.

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)
        print(f"Updated {filepath}")

update_resources('contact_es.html')
update_resources('contact.html')

