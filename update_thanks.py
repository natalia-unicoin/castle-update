import re

def update_file(filename, lang):
    with open(filename, "r") as f:
        html = f.read()
    
    if lang == 'es':
        old_p = 'Mientras esperas respuesta, te invitamos a ser parte de nuestra comunidad.'
        new_p = 'Mientras esperas respuesta, te invitamos a ser parte de nuestra comunidad.<br><br>Pronto nos ponemos en contacto contigo.'
        old_cta = '<a href="https://www.instagram.com/buildyourcastle_ai/" target="_blank" class="waitlist-submit" style="display: inline-block; text-decoration: none; width: auto; padding: 16px 32px; font-weight: 700; background: #A03FA3;">SÍGUENOS EN INSTAGRAM</a>'
        new_cta = """
            <div style="display: flex; gap: 16px; justify-content: center; flex-wrap: wrap;">
                <a href="https://www.instagram.com/buildyourcastle_ai/" target="_blank" class="waitlist-submit" style="margin-top: 0; display: inline-block; text-decoration: none; width: auto; padding: 16px 32px; font-weight: 700; background: #A03FA3;">SÍGUENOS EN INSTAGRAM</a>
                <a href="https://www.linkedin.com/company/buildyourcastle/about/" target="_blank" class="waitlist-submit" style="margin-top: 0; display: inline-block; text-decoration: none; width: auto; padding: 16px 32px; font-weight: 700; background: #0A66C2;">SÍGUENOS EN LINKEDIN</a>
            </div>
"""
    else:
        old_p = 'While you wait, we invite you to join our community.'
        new_p = "While you wait, we invite you to join our community.<br><br>You'll hear from us soon."
        old_cta = '<a href="https://www.instagram.com/buildyourcastle_ai/" target="_blank" class="waitlist-submit" style="display: inline-block; text-decoration: none; width: auto; padding: 16px 32px; font-weight: 700; background: #A03FA3;">FOLLOW ON INSTAGRAM</a>'
        new_cta = """
            <div style="display: flex; gap: 16px; justify-content: center; flex-wrap: wrap;">
                <a href="https://www.instagram.com/buildyourcastle_ai/" target="_blank" class="waitlist-submit" style="margin-top: 0; display: inline-block; text-decoration: none; width: auto; padding: 16px 32px; font-weight: 700; background: #A03FA3;">FOLLOW ON INSTAGRAM</a>
                <a href="https://www.linkedin.com/company/buildyourcastle/about/" target="_blank" class="waitlist-submit" style="margin-top: 0; display: inline-block; text-decoration: none; width: auto; padding: 16px 32px; font-weight: 700; background: #0A66C2;">FOLLOW ON LINKEDIN</a>
            </div>
"""
    
    html = html.replace(old_p, new_p)
    html = html.replace(old_cta, new_cta)
    
    with open(filename, "w") as f:
        f.write(html)

update_file("gracias.html", "es")
update_file("thank-you.html", "en")
print("Updated thank you pages.")
