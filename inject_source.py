import glob
import re

files = glob.glob("*.html")
files = [f for f in files if "backup" not in f]

for f in files:
    with open(f, "r") as file:
        content = file.read()
    
    # We will look for all forms and inject the hidden SOURCE field based on contents.
    
    # 1. Subscribe forms (Newsletter)
    # <form action="..." ... class="subscribe-form" ...>
    content = re.sub(
        r'(<form[^>]*class="subscribe-form"[^>]*>)',
        r'\1\n                <input type="hidden" name="SOURCE" value="Newsletter">',
        content
    )
    
    # 2. Waitlist forms vs Contact forms
    # Both use class="waitlist-form". We must differentiate by checking if they contain name="PHONE".
    # Since regex over multiline HTML can be tricky, we can find all <form ... class="waitlist-form"> ... </form>
    # and do a replacement per form.
    
    forms = re.split(r'(<form[^>]*class="waitlist-form"[^>]*>)', content)
    new_content = forms[0]
    for i in range(1, len(forms), 2):
        form_open = forms[i]
        form_body = forms[i+1] # This goes up to the next form open or end of file, but wait, re.split behaves differently.
        pass
        
    # Better approach: find all form blocks
    # Actually, we can just replace all waitlist-form openings with Waitlist source,
    # and then do a specific fix for the Contact page forms.
    # On contact.html and contact_es.html, the main form is the only one with name="PHONE".
    
    content = re.sub(
        r'(<form[^>]*class="waitlist-form"[^>]*>)',
        r'\1\n                <input type="hidden" name="SOURCE" value="Waitlist">',
        content
    )
    
    with open(f, "w") as file:
        file.write(content)

# Now specifically update the contact forms to have value="Contacto" instead of Waitlist
for f in ["contact.html", "contact_es.html"]:
    with open(f, "r") as file:
        content = file.read()
    
    # The contact form has name="PHONE". The Waitlist Modal does not.
    # In contact.html, there are two waitlist-forms. The main one, and the modal one.
    # The main one has <label for="phone">
    # Let's find the Waitlist source injection and change it to Contacto IF it's followed by name="PHONE" within the same form.
    # Because of regex limitations, it's easier to just replace "Waitlist" with "Contacto" for the form that contains "PHONE".
    
    blocks = content.split('<form ')
    new_content = blocks[0]
    for block in blocks[1:]:
        if 'class="waitlist-form"' in block and 'name="PHONE"' in block:
            block = block.replace('<input type="hidden" name="SOURCE" value="Waitlist">', '<input type="hidden" name="SOURCE" value="Contacto">')
        new_content += '<form ' + block
    
    with open(f, "w") as file:
        file.write(new_content)

print("SOURCE hidden fields injected.")
