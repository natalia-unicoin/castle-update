import re
for f in ["contact.html", "contact_es.html"]:
    with open(f, "r") as file:
        content = file.read()
    
    # Let's fix the waitlist modal form in contact pages specifically
    content = re.sub(
        r'(<form[^>]*id="waitlistForm"[^>]*>)\s*<input type="hidden" name="SOURCE" value="Contacto">',
        r'\1\n                <input type="hidden" name="SOURCE" value="Waitlist">',
        content
    )
    
    with open(f, "w") as file:
        file.write(content)
print("Fixed Waitlist modal in contact pages.")
