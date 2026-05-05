import re

def create_thankyou(source_file, target_file, lang="es"):
    with open(source_file, "r") as f:
        html = f.read()

    # We need to replace the content inside the "snap-section" that contains the contact form
    # The contact form section starts with: <section class="snap-section" style="background-color: #F8F8FA;
    # We can use regex or simple string replacement.
    
    start_str = '<section class="snap-section" style="background-color: #F8F8FA;'
    end_str = '</section>'
    
    start_idx = html.find(start_str)
    if start_idx == -1:
        print(f"Could not find start in {source_file}")
        return
        
    end_idx = html.find(end_str, start_idx) + len(end_str)
    
    # Also change the title/hero
    hero_start = '<h1 style="font-size: clamp(3rem, 6vw, 4.5rem);'
    hero_end = '</h1>'
    
    if lang == "es":
        new_hero_h1 = '<h1 style="font-size: clamp(3rem, 6vw, 4.5rem); font-weight: 900; letter-spacing: -2px; margin-bottom: 20px; line-height: 1.1; color: #1A1A1A;">¡Gracias por contactarnos!</h1>'
        new_hero_p = '<p style="font-size: 1.25rem; font-weight: 400; color: #666; max-width: 600px; margin: 0 auto;">Hemos recibido tu información y nuestro equipo se pondrá en contacto contigo pronto.</p>'
    else:
        new_hero_h1 = '<h1 style="font-size: clamp(3rem, 6vw, 4.5rem); font-weight: 900; letter-spacing: -2px; margin-bottom: 20px; line-height: 1.1; color: #1A1A1A;">Thank you for reaching out!</h1>'
        new_hero_p = '<p style="font-size: 1.25rem; font-weight: 400; color: #666; max-width: 600px; margin: 0 auto;">We have received your information and our team will get back to you shortly.</p>'

    # Replace hero text
    html = re.sub(r'<h1 style="font-size: clamp\(3rem, 6vw, 4\.5rem\).*?</h1>', new_hero_h1, html, flags=re.DOTALL)
    html = re.sub(r'<p style="font-size: 1\.25rem.*?p>', new_hero_p, html, flags=re.DOTALL)
    
    # Create the success block
    if lang == "es":
        success_block = """
    <section class="snap-section" style="background-color: #F8F8FA; padding: var(--section-pad-large) 4vw; display: flex; justify-content: center; align-items: center; min-height: 50vh;">
        <div class="container" style="max-width: 700px; width: 100%; text-align: center; padding: 40px; background: white; border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.05);">
            <div style="width: 80px; height: 80px; background-color: #E8F5E9; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto 24px;">
                <svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="#4CAF50" stroke-width="3" stroke-linecap="round" stroke-linejoin="round">
                    <polyline points="20 6 9 17 4 12"></polyline>
                </svg>
            </div>
            <h2 style="font-size: 2rem; font-weight: 800; color: #1A1A1A; margin-bottom: 16px;">¡Mensaje Enviado!</h2>
            <p style="font-size: 1.1rem; color: #666; margin-bottom: 32px; line-height: 1.6;">
                Tu aplicación ha sido enviada exitosamente al ecosistema Castle. 
                <br>Mientras esperas respuesta, te invitamos a ser parte de nuestra comunidad.
            </p>
            <a href="https://www.instagram.com/buildyourcastle_ai/" target="_blank" class="waitlist-submit" style="display: inline-block; text-decoration: none; width: auto; padding: 16px 32px; font-weight: 700; background: #A03FA3;">SÍGUENOS EN INSTAGRAM</a>
            <div style="margin-top: 24px;">
                <a href="index_es.html" style="color: #666; text-decoration: underline; font-weight: 500;">Volver al inicio</a>
            </div>
        </div>
    </section>
"""
    else:
        success_block = """
    <section class="snap-section" style="background-color: #F8F8FA; padding: var(--section-pad-large) 4vw; display: flex; justify-content: center; align-items: center; min-height: 50vh;">
        <div class="container" style="max-width: 700px; width: 100%; text-align: center; padding: 40px; background: white; border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.05);">
            <div style="width: 80px; height: 80px; background-color: #E8F5E9; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto 24px;">
                <svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="#4CAF50" stroke-width="3" stroke-linecap="round" stroke-linejoin="round">
                    <polyline points="20 6 9 17 4 12"></polyline>
                </svg>
            </div>
            <h2 style="font-size: 2rem; font-weight: 800; color: #1A1A1A; margin-bottom: 16px;">Message Sent!</h2>
            <p style="font-size: 1.1rem; color: #666; margin-bottom: 32px; line-height: 1.6;">
                Your application has been successfully submitted to the Castle ecosystem. 
                <br>While you wait, we invite you to join our community.
            </p>
            <a href="https://www.instagram.com/buildyourcastle_ai/" target="_blank" class="waitlist-submit" style="display: inline-block; text-decoration: none; width: auto; padding: 16px 32px; font-weight: 700; background: #A03FA3;">FOLLOW ON INSTAGRAM</a>
            <div style="margin-top: 24px;">
                <a href="index.html" style="color: #666; text-decoration: underline; font-weight: 500;">Back to home</a>
            </div>
        </div>
    </section>
"""

    html = html[:start_idx] + success_block + html[end_idx:]
    
    # Update title
    if lang == "es":
        html = html.replace("<title>Contact Us - Castle</title>", "<title>¡Gracias! - Castle</title>")
        html = html.replace("<title>Contacto - Castle</title>", "<title>¡Gracias! - Castle</title>")
    else:
        html = html.replace("<title>Contact Us - Castle</title>", "<title>Thank You - Castle</title>")
    
    with open(target_file, "w") as f:
        f.write(html)
        
    print(f"Created {target_file}")

create_thankyou("contact_es.html", "gracias.html", "es")
create_thankyou("contact.html", "thank-you.html", "en")
