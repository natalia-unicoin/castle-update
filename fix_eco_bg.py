import re

def update_eco_bg(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    # The section string we want to replace
    old_section_pattern = r'<section style="background-color: #6B7280; background-size: cover; background-position: center; background-attachment: fixed; min-height: 100vh; display: flex; flex-direction: column; justify-content: center; padding: var\(--section-pad-y\) 0; overflow: hidden; text-align: center;">(.*?)<!-- Quick Resources -->'
    
    match = re.search(old_section_pattern, html, re.DOTALL)
    if match:
        content = match.group(1)
        
        # We need to wrap the content in a relative z-index container
        # Let's see what's inside content: 
        # <h2 class="section-title"...
        # <div style="display: flex; gap: 20px;...
        
        new_section = f"""<section style="background-image: url('./public/images/common/ecosystem-bg.jpg'); background-size: cover; background-position: center; background-attachment: fixed; min-height: 100vh; display: flex; flex-direction: column; justify-content: center; padding: var(--section-pad-y) 0; overflow: hidden; text-align: center; position: relative;">
    <div style="position: absolute; bottom: 0; left: 0; width: 100%; height: 60%; background: linear-gradient(to top, rgba(17,17,17,0.95) 0%, rgba(17,17,17,0.5) 50%, rgba(17,17,17,0) 100%); z-index: 1;"></div>
    <div style="position: relative; z-index: 2;">{content}</div>
</section>

<!-- Quick Resources -->"""

        html = html[:match.start()] + new_section + html[match.end():]
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html)
            print(f"Updated {filepath}")
    else:
        print(f"Could not find section in {filepath}")

update_eco_bg('contact_es.html')
update_eco_bg('contact.html')

