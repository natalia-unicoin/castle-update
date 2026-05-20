import re

def update_file(filename):
    with open(filename, 'r') as f:
        content = f.read()

    # 1. Update the section wrapper to center it
    content = re.sub(
        r'(<section class="snap-section" style="background-image: url\([^)]+\);\s*background-size: cover;\s*background-position: center;\s*min-height: 100vh;\s*display: flex;\s*flex-direction: column;\s*)justify-content: flex-end;\s*padding-bottom: 15vh;',
        r'\1justify-content: center; padding-bottom: 0;',
        content
    )

    # 2. Update the gradient overlay to cover the image better for centered text
    # Current: <div style="position: absolute; bottom: 0; left: 0; width: 100%; height: 80%; background: linear-gradient(to top, rgba(17,17,17,0.9) 0%, rgba(17,17,17,0) 100%); z-index: 1;"></div>
    content = re.sub(
        r'<div style="position: absolute; bottom: 0; left: 0; width: 100%; height: 80%; background: linear-gradient[^>]+></div>',
        r'<div style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; background: rgba(17,17,17,0.4); z-index: 1;"></div>',
        content
    )

    # 3. Increase the font size of the h2
    # Current: <h2 class="section-title" style="color: #FFFFFF; padding: 0 20px; margin-bottom: 40px; line-height: 1.1;">
    content = re.sub(
        r'<h2 class="section-title" style="color: #FFFFFF; padding: 0 20px; margin-bottom: 40px; line-height: 1\.1;">',
        r'<h2 class="section-title" style="color: #FFFFFF; padding: 0 20px; margin-bottom: 40px; line-height: 1.1; font-size: clamp(48px, 6vw, 80px);">',
        content
    )
    
    with open(filename, 'w') as f:
        f.write(content)
    print(f"Updated {filename}")

update_file('contact.html')
update_file('contact_es.html')
