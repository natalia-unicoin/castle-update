import re

files = ["js/mailchimp.js", "gracias.html", "thank-you.html"]

for f in files:
    with open(f, "r") as file:
        content = file.read()
    
    # Update waitlist modal and thank you pages
    content = content.replace("background-color: #E8F5E9;", "background-color: #F5E8F6;")
    content = content.replace('stroke="#4CAF50"', 'stroke="#A03FA3"')
    
    # Update inline newsletter success
    content = content.replace("background: #E8F5E9; color: #2E7D32;", "background: #F5E8F6; color: #A03FA3;")
    
    with open(f, "w") as file:
        file.write(content)

print("Updated checkmark colors to brand purple.")
