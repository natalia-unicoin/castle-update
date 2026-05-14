import re

def update_contact_layout(filepath, is_spanish):
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    if is_spanish:
        hero_title = "Contáctanos"
        hero_subtitle = "¿Tienes alguna pregunta, idea para asociarnos o simplemente quieres saludar? Estamos aquí para escucharte."
        name_label = "Nombre Completo *"
        name_placeholder = "Tu nombre"
        email_label = "Correo Electrónico *"
        email_placeholder = "tu@email.com"
        topic_label = "Tema de Interés *"
        topic_default = "Selecciona un tema"
        topics = ["Soporte General", "Prensa y Medios", "Inversores", "Partnerships"]
        message_label = "Mensaje *"
        message_placeholder = "¿En qué podemos ayudarte?"
        privacy_text = 'Acepto la <a href="#" style="color: #A03FA3;">Política de Privacidad</a> y consiento el procesamiento de mis datos.'
        submit_btn = "ENVIAR MENSAJE"
    else:
        hero_title = "Contact Us"
        hero_subtitle = "Have a question, partnership idea, or just want to say hi? We are here to listen."
        name_label = "Full Name *"
        name_placeholder = "Your name"
        email_label = "Email Address *"
        email_placeholder = "you@email.com"
        topic_label = "Topic of Interest *"
        topic_default = "Select a topic"
        topics = ["General Support", "Press & Media", "Investors", "Partnerships"]
        message_label = "Message *"
        message_placeholder = "How can we help you?"
        privacy_text = 'I accept the <a href="#" style="color: #A03FA3;">Privacy Policy</a> and consent to data processing.'
        submit_btn = "SEND MESSAGE"

    new_hero_and_form = f"""<!-- 1. Hero Section -->
    <section class="hero snap-section" style="background-image: url('./public/images/common/hero-contact.jpg'); background-size: cover; background-position: center; background-attachment: fixed; background-repeat: no-repeat; display: flex; align-items: flex-end; padding: 150px 4vw 80px 4vw; min-height: 100vh; position: relative;">
        <!-- Black Gradient Overlay -->
        <div style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; background: linear-gradient(180deg, rgba(0,0,0,0) 0%, rgba(0,0,0,0.85) 100%); z-index: 1;"></div>
        
        <div class="container" style="max-width: 1000px; margin: 0 auto; display: flex; justify-content: center; align-items: center; position: relative; z-index: 2;">
            <div style="text-align: center; width: 100%;">
                <h1 class="hero-title color-reveal" style="color: #FFFFFF; font-size: clamp(50px, 7vw, 90px); letter-spacing: -2px; margin-bottom: 24px; text-shadow: 0 4px 12px rgba(0,0,0,0.5); font-family: 'Inter', sans-serif; font-weight: 700;">{hero_title}</h1>
                <p class="hero-subtitle color-reveal" style="color: rgba(255,255,255,0.95); font-size: clamp(18px, 2vw, 24px); line-height: 1.5; max-width: 700px; margin: 0 auto; font-family: 'Inter', sans-serif;">{hero_subtitle}</p>
                <div style="margin-top: 40px;">
                    <a href="#contact-form-section" class="btn" style="padding: 18px 45px; letter-spacing: 1.5px; font-size: 15px;">{"LLENAR FORMULARIO" if is_spanish else "FILL OUT FORM"}</a>
                </div>
            </div>
        </div>
    </section>

    <!-- 2. Form Section -->
    <section id="contact-form-section" class="snap-section" style="background-color: #F8F8FA; padding: var(--section-pad-large) 4vw; display: flex; justify-content: center; align-items: center;">
        <div class="container" style="max-width: 700px; width: 100%; text-align: left; padding: 0;">
            <div style="background: #FFFFFF; border-radius: 12px; padding: 50px 40px; box-shadow: 0 20px 40px rgba(0,0,0,0.05); border: 1px solid #E5E7EB; width: 100%;">
                <form action="https://buildyourcastle.us10.list-manage.com/subscribe/post?u=4766d7bd8debcf610dadddfb6&amp;id=53677e9563" method="POST" target="_blank" class="contact-page-form" style="display: flex; flex-direction: column; gap: 20px;">
                    <input type="hidden" name="SOURCE" value="ContactPage">
                    
                    <div class="form-row" style="display: grid; grid-template-columns: 1fr; gap: 20px;">
                        <style>@media (min-width: 600px) {{ .contact-page-form .form-row {{ grid-template-columns: 1fr 1fr !important; }} }}</style>
                        <div class="form-group" style="display: flex; flex-direction: column; gap: 8px;">
                            <label style="font-size: 14px; font-weight: 600; color: #1A1A1A; font-family: 'Inter', sans-serif;">{name_label}</label>
                            <input type="text" name="FNAME" required placeholder="{name_placeholder}" style="padding: 14px 16px; border: 1px solid #D1D5DB; border-radius: 6px; font-family: 'Inter', sans-serif; font-size: 15px; outline: none; color: #1A1A1A;">
                        </div>
                        <div class="form-group" style="display: flex; flex-direction: column; gap: 8px;">
                            <label style="font-size: 14px; font-weight: 600; color: #1A1A1A; font-family: 'Inter', sans-serif;">{email_label}</label>
                            <input type="email" name="EMAIL" required placeholder="{email_placeholder}" style="padding: 14px 16px; border: 1px solid #D1D5DB; border-radius: 6px; font-family: 'Inter', sans-serif; font-size: 15px; outline: none; color: #1A1A1A;">
                        </div>
                    </div>

                    <div class="form-group" style="display: flex; flex-direction: column; gap: 8px;">
                        <label style="font-size: 14px; font-weight: 600; color: #1A1A1A; font-family: 'Inter', sans-serif;">{topic_label}</label>
                        <select name="TOPIC" required style="padding: 14px 16px; border: 1px solid #D1D5DB; border-radius: 6px; font-family: 'Inter', sans-serif; font-size: 15px; outline: none; appearance: none; color: #1A1A1A; background: url('data:image/svg+xml;charset=US-ASCII,<svg xmlns=\\"http://www.w3.org/2000/svg\\" width=\\"16\\" height=\\"16\\" fill=\\"%23111111\\" viewBox=\\"0 0 16 16\\"><path d=\\"M4.293 5.293a1 1 0 0 1 1.414 0L8 8.586l2.293-2.293a1 1 0 1 1 1.414 1.414l-3 3a1 1 0 0 1-1.414 0l-3-3a1 1 0 0 1 0-1.414z\\"/></svg>') no-repeat right 16px center; background-color: #F9FAFB;">
                            <option value="" disabled selected>{topic_default}</option>
                            <option value="{topics[0]}">{topics[0]}</option>
                            <option value="{topics[1]}">{topics[1]}</option>
                            <option value="{topics[2]}">{topics[2]}</option>
                            <option value="{topics[3]}">{topics[3]}</option>
                        </select>
                    </div>

                    <div class="form-group" style="display: flex; flex-direction: column; gap: 8px;">
                        <label style="font-size: 14px; font-weight: 600; color: #1A1A1A; font-family: 'Inter', sans-serif;">{message_label}</label>
                        <textarea name="MESSAGE" rows="5" required placeholder="{message_placeholder}" style="padding: 14px 16px; border: 1px solid #D1D5DB; border-radius: 6px; font-family: 'Inter', sans-serif; font-size: 15px; outline: none; resize: vertical; color: #1A1A1A;"></textarea>
                    </div>

                    <div style="display: flex; align-items: flex-start; gap: 12px; margin-top: 10px;">
                        <input type="checkbox" id="privacy" required style="margin-top: 4px; width: 18px; height: 18px; accent-color: #A03FA3;">
                        <label for="privacy" style="font-size: 13px; color: #4B5563; line-height: 1.5; cursor: pointer; font-family: 'Inter', sans-serif;">{privacy_text}</label>
                    </div>

                    <button type="submit" style="background-color: #A03FA3; color: #FFFFFF; font-weight: 800; letter-spacing: 2px; padding: 18px 40px; border-radius: 50px; font-size: 15px; border: none; cursor: pointer; transition: transform 0.2s, box-shadow 0.2s; margin-top: 15px; width: 100%; box-shadow: 0 10px 20px rgba(160, 63, 163, 0.3); text-transform: uppercase;">{submit_btn}</button>
                </form>
            </div>
        </div>
    </section>"""

    # We need to replace from <section class="hero snap-section" down to <!-- Social Proof / Ecosystem -->
    pattern = re.compile(r'<section class="hero snap-section".*?(?=<!-- Social Proof / Ecosystem -->)', re.DOTALL)
    
    if pattern.search(html):
        html = pattern.sub(new_hero_and_form + "\n\n", html)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"Updated layout in {filepath}")
    else:
        print(f"Could not match pattern in {filepath}")

update_contact_layout('contact_es.html', True)
update_contact_layout('contact.html', False)

