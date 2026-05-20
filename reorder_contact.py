import re

def process_file(filename):
    with open(filename, 'r') as f:
        content = f.read()

    # Find sections by HTML comments
    
    hero_match = re.search(r'(<!-- 1\. Hero Section -->.*?</section>)', content, re.DOTALL)
    form_sec_match = re.search(r'(<!-- 2\. Form Section -->\s*<section id="contact-form-section".*?</section>)', content, re.DOTALL)
    social_sec_match = re.search(r'(<!-- Social Proof / Ecosystem -->\s*<section.*?</section>)', content, re.DOTALL)
    resources_sec_match = re.search(r'(<!-- Quick Resources -->\s*<section.*?</section>)', content, re.DOTALL)
    
    if not form_sec_match or not social_sec_match or not resources_sec_match or not hero_match:
        print(f"Could not find all sections in {filename}")
        return

    hero_html = hero_match.group(1)
    form_html = form_sec_match.group(1)
    social_html = social_sec_match.group(1)
    res_html = resources_sec_match.group(1)

    # In contact.html, the Form section also contains the form itself inside the container!
    # Wait! In contact.html:
    # "2. Form Section" contains the ENTIRE static form instead of just the button!
    # BUT wait, the contact.html still has a button?
    # Let me check my previous output for contact.html
    # "2. Form Section" -> <form action="https://buildyourcastle.us10.list-manage.com/subscribe/post..."
    # Oh! `contact.html` was not updated to use the unified modal yet! It still has the static form.
    # The user asked: "en la pagina contacto, cambiemos el orden ... y que ese bloque tenga el botón de contacto ... y cuando tengamos ok esp vamos a inglés"
    # This implies I should change Spanish first, and then apply it to English. Since I already updated Spanish, let's fix English too. But English needs the form replaced by the button first!

    pass

