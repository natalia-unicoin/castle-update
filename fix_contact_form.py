import re

def fix_form_and_cta(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Remove the CTA
    # The pattern looks for the div containing the 'LLENAR FORMULARIO' or 'FILL OUT FORM' button.
    html = re.sub(r'<div style="margin-top: 40px;">\s*<a href="#contact-form-section" class="btn".*?</a>\s*</div>', '', html)

    # 2. Remove the borders/box from the form container
    # Old: <div style="background: #FFFFFF; border-radius: 12px; padding: 50px 40px; box-shadow: 0 20px 40px rgba(0,0,0,0.05); border: 1px solid #E5E7EB; width: 100%;">
    # New: <div style="width: 100%;">
    html = html.replace(
        '<div style="background: #FFFFFF; border-radius: 12px; padding: 50px 40px; box-shadow: 0 20px 40px rgba(0,0,0,0.05); border: 1px solid #E5E7EB; width: 100%;">',
        '<div style="width: 100%;">'
    )

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)
        print(f"Updated {filepath}")

fix_form_and_cta('contact_es.html')
fix_form_and_cta('contact.html')

