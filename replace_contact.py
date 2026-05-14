import re

def update_contact_page(file_path, is_spanish):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Define the new content based on language
    if is_spanish:
        hero_title = "Hablemos de tu futuro"
        hero_subtitle = "¿Tienes alguna pregunta, idea para asociarnos o simplemente quieres saludar? Llena el formulario y nuestro equipo te contactará pronto."
        support_title = "Soporte General"
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
        
        eco_title = "Únete al Ecosistema que está transformando la riqueza femenina"
        eco_badges = ["Influencers", "Creadoras", "Marcas", "Expertas"]
        
        explore_title = "Explora Castle"
        explore_subtitle = "Descubre todo lo que nuestro ecosistema tiene para ofrecerte."
        
        card1_title = "MasterClass"
        card1_desc = "Aprende los fundamentos para tomar control de tu riqueza y construir tu portafolio."
        card1_link = "Ver Ahora &rarr;"
        card1_href = "masterclass_es.html"
        
        card2_title = "Partnerships"
        card2_desc = "Únete como creadora, influencer o marca para co-crear valor en la Web3."
        card2_link = "Ser Partner &rarr;"
        card2_href = "partners_es.html"
        
        card3_title = "Nuestra Historia"
        card3_desc = "Conoce la visión de Castle y por qué estamos construyendo el futuro de la riqueza."
        card3_link = "Leer Más &rarr;"
        card3_href = "about_es.html"
    else:
        hero_title = "Let's talk about your future"
        hero_subtitle = "Have a question, partnership idea, or just want to say hi? Fill out the form below and our team will get back to you shortly."
        support_title = "General Support"
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
        
        eco_title = "Join the Ecosystem transforming female wealth"
        eco_badges = ["Influencers", "Creators", "Brands", "Experts"]
        
        explore_title = "Explore Castle"
        explore_subtitle = "Discover everything our ecosystem has to offer."
        
        card1_title = "MasterClass"
        card1_desc = "Learn the fundamentals to take control of your wealth and build your portfolio."
        card1_link = "Watch Now &rarr;"
        card1_href = "masterclass.html"
        
        card2_title = "Partnerships"
        card2_desc = "Join as a creator, influencer, or brand to co-create value in Web3."
        card2_link = "Become a Partner &rarr;"
        card2_href = "partners.html"
        
        card3_title = "Our Story"
        card3_desc = "Learn about Castle's vision and why we are building the future of wealth."
        card3_link = "Read More &rarr;"
        card3_href = "about.html"

    # HTML string template
    new_html = f"""<section class="snap-section" style="background-color: #F8F8FA; padding: calc(150px + 4vw) 4vw 80px 4vw; min-height: 100vh; position: relative; border-bottom: 1px solid #E5E7EB;">
    <div class="container" style="max-width: 1400px; margin: 0 auto; display: grid; grid-template-columns: 1fr; gap: 60px; align-items: center;">
        <style>
            @media (min-width: 900px) {{
                .contact-grid {{ grid-template-columns: 1fr 1fr !important; }}
            }}
        </style>
        <div class="contact-grid" style="display: grid; grid-template-columns: 1fr; gap: 60px;">
            <!-- Left Side: Text -->
            <div style="text-align: left; padding-right: 0;">
                <div class="hero-eyebrow" style="color: #A03FA3; font-weight: 700; font-size: 14px; letter-spacing: 4px; margin-bottom: 20px; text-transform: uppercase;">{'Contacto' if is_spanish else 'Contact'}</div>
                <h1 class="hero-title color-reveal" style="color: #1A1A1A; font-size: clamp(48px, 6vw, 72px); letter-spacing: -2px; margin-bottom: 24px; line-height: 1;">{hero_title}</h1>
                <p style="color: #4B5563; font-size: clamp(18px, 2vw, 22px); line-height: 1.6; max-width: 600px; margin-bottom: 40px;">{hero_subtitle}</p>
                
                <!-- Quick Contacts -->
                <div style="display: flex; flex-direction: column; gap: 16px;">
                    <div style="display: flex; align-items: center; gap: 12px;">
                        <div style="width: 40px; height: 40px; border-radius: 50%; background: rgba(160,63,163,0.1); display: flex; align-items: center; justify-content: center; color: #A03FA3;">
                            <svg width="20" height="20" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"></path></svg>
                        </div>
                        <div>
                            <p style="font-size: 13px; font-weight: 700; color: #6B7280; text-transform: uppercase; letter-spacing: 1px; margin: 0;">{support_title}</p>
                            <a href="mailto:hello@buildyourcastle.ai" style="font-size: 16px; font-weight: 600; color: #1A1A1A; text-decoration: none;">hello@buildyourcastle.ai</a>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Right Side: Form -->
            <div style="background: #FFFFFF; border-radius: 12px; padding: 40px; box-shadow: 0 20px 40px rgba(0,0,0,0.08); border: 1px solid #E5E7EB;">
                <form action="https://buildyourcastle.us10.list-manage.com/subscribe/post?u=4766d7bd8debcf610dadddfb6&amp;id=53677e9563" method="POST" target="_blank" class="contact-page-form" style="display: flex; flex-direction: column; gap: 20px;">
                    <input type="hidden" name="SOURCE" value="ContactPage">
                    
                    <div class="form-row" style="display: grid; grid-template-columns: 1fr; gap: 20px;">
                        <style>@media (min-width: 600px) {{ .contact-page-form .form-row {{ grid-template-columns: 1fr 1fr !important; }} }}</style>
                        <div class="form-group" style="display: flex; flex-direction: column; gap: 8px;">
                            <label style="font-size: 14px; font-weight: 600; color: #1A1A1A;">{name_label}</label>
                            <input type="text" name="FNAME" required placeholder="{name_placeholder}" style="padding: 14px 16px; border: 1px solid #D1D5DB; border-radius: 6px; font-family: 'Inter', sans-serif; font-size: 15px; outline: none;">
                        </div>
                        <div class="form-group" style="display: flex; flex-direction: column; gap: 8px;">
                            <label style="font-size: 14px; font-weight: 600; color: #1A1A1A;">{email_label}</label>
                            <input type="email" name="EMAIL" required placeholder="{email_placeholder}" style="padding: 14px 16px; border: 1px solid #D1D5DB; border-radius: 6px; font-family: 'Inter', sans-serif; font-size: 15px; outline: none;">
                        </div>
                    </div>

                    <div class="form-group" style="display: flex; flex-direction: column; gap: 8px;">
                        <label style="font-size: 14px; font-weight: 600; color: #1A1A1A;">{topic_label}</label>
                        <select name="TOPIC" required style="padding: 14px 16px; border: 1px solid #D1D5DB; border-radius: 6px; font-family: 'Inter', sans-serif; font-size: 15px; outline: none; appearance: none; background: url('data:image/svg+xml;charset=US-ASCII,<svg xmlns=\\"http://www.w3.org/2000/svg\\" width=\\"16\\" height=\\"16\\" fill=\\"%23111111\\" viewBox=\\"0 0 16 16\\"><path d=\\"M4.293 5.293a1 1 0 0 1 1.414 0L8 8.586l2.293-2.293a1 1 0 1 1 1.414 1.414l-3 3a1 1 0 0 1-1.414 0l-3-3a1 1 0 0 1 0-1.414z\\"/></svg>') no-repeat right 16px center; background-color: #FFFFFF;">
                            <option value="" disabled selected>{topic_default}</option>
                            <option value="{topics[0]}">{topics[0]}</option>
                            <option value="{topics[1]}">{topics[1]}</option>
                            <option value="{topics[2]}">{topics[2]}</option>
                            <option value="{topics[3]}">{topics[3]}</option>
                        </select>
                    </div>

                    <div class="form-group" style="display: flex; flex-direction: column; gap: 8px;">
                        <label style="font-size: 14px; font-weight: 600; color: #1A1A1A;">{message_label}</label>
                        <textarea name="MESSAGE" rows="4" required placeholder="{message_placeholder}" style="padding: 14px 16px; border: 1px solid #D1D5DB; border-radius: 6px; font-family: 'Inter', sans-serif; font-size: 15px; outline: none; resize: vertical;"></textarea>
                    </div>

                    <div style="display: flex; align-items: flex-start; gap: 12px; margin-top: 10px;">
                        <input type="checkbox" id="privacy" required style="margin-top: 4px; width: 18px; height: 18px; accent-color: #A03FA3;">
                        <label for="privacy" style="font-size: 13px; color: #4B5563; line-height: 1.5; cursor: pointer;">{privacy_text}</label>
                    </div>

                    <button type="submit" style="background-color: #A03FA3; color: #FFFFFF; font-weight: 800; letter-spacing: 2px; padding: 18px 40px; border-radius: 50px; font-size: 15px; border: none; cursor: pointer; transition: transform 0.2s, box-shadow 0.2s; margin-top: 10px; width: 100%; box-shadow: 0 10px 20px rgba(160, 63, 163, 0.3); text-transform: uppercase;">{submit_btn}</button>
                </form>
            </div>
        </div>
    </div>
</section>

<!-- Social Proof / Ecosystem -->
<section style="background-color: #1A1A1A; padding: var(--section-pad-large) 0; overflow: hidden; text-align: center;">
    <h2 style="color: #FFFFFF; font-size: clamp(24px, 4vw, 36px); font-weight: 700; margin-bottom: 40px; padding: 0 20px;">{eco_title}</h2>
    
    <div style="display: flex; gap: 20px; justify-content: center; flex-wrap: wrap; max-width: 1200px; margin: 0 auto; padding: 0 4vw;">
        <div style="background: rgba(255,255,255,0.05); border: 1px solid rgba(255,255,255,0.1); padding: 16px 32px; border-radius: 50px; color: #FFFFFF; font-weight: 600; font-size: 16px;">{eco_badges[0]}</div>
        <div style="background: rgba(255,255,255,0.05); border: 1px solid rgba(255,255,255,0.1); padding: 16px 32px; border-radius: 50px; color: #FFFFFF; font-weight: 600; font-size: 16px;">{eco_badges[1]}</div>
        <div style="background: rgba(255,255,255,0.05); border: 1px solid rgba(255,255,255,0.1); padding: 16px 32px; border-radius: 50px; color: #FFFFFF; font-weight: 600; font-size: 16px;">{eco_badges[2]}</div>
        <div style="background: rgba(255,255,255,0.05); border: 1px solid rgba(255,255,255,0.1); padding: 16px 32px; border-radius: 50px; color: #FFFFFF; font-weight: 600; font-size: 16px;">{eco_badges[3]}</div>
    </div>
</section>

<!-- Quick Resources -->
<section style="background-color: #FFFFFF; padding: var(--section-pad-large) 4vw;">
    <div class="container" style="max-width: 1400px; margin: 0 auto;">
        <div style="text-align: center; margin-bottom: 60px;">
            <h2 class="section-title" style="margin-bottom: 10px; padding: 0;">{explore_title}</h2>
            <p class="section-subtitle" style="padding: 0; max-width: 600px; margin: 0 auto;">{explore_subtitle}</p>
        </div>

        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 24px;">
            <!-- Card 1 -->
            <a href="{card1_href}" style="text-decoration: none; display: flex; flex-direction: column; background: #F9F9F9; border-radius: 12px; padding: 40px; border: 1px solid #E5E7EB; transition: transform 0.3s, box-shadow 0.3s;" onmouseover="this.style.transform='translateY(-5px)'; this.style.boxShadow='0 20px 40px rgba(0,0,0,0.05)';" onmouseout="this.style.transform='translateY(0)'; this.style.boxShadow='none';">
                <div style="width: 48px; height: 48px; border-radius: 8px; background: rgba(160,63,163,0.1); color: #A03FA3; display: flex; align-items: center; justify-content: center; margin-bottom: 24px;">
                    <svg width="24" height="24" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M14.752 11.168l-3.197-2.132A1 1 0 0010 9.87v4.263a1 1 0 001.555.832l3.197-2.132a1 1 0 000-1.664z"></path><path stroke-linecap="round" stroke-linejoin="round" d="M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
                </div>
                <h3 style="font-size: 22px; font-weight: 700; color: #1A1A1A; margin-bottom: 12px;">{card1_title}</h3>
                <p style="font-size: 15px; color: #4B5563; line-height: 1.5; margin-bottom: 24px; flex-grow: 1;">{card1_desc}</p>
                <span style="font-size: 14px; font-weight: 700; color: #A03FA3; text-transform: uppercase; letter-spacing: 1px;">{card1_link}</span>
            </a>

            <!-- Card 2 -->
            <a href="{card2_href}" style="text-decoration: none; display: flex; flex-direction: column; background: #F9F9F9; border-radius: 12px; padding: 40px; border: 1px solid #E5E7EB; transition: transform 0.3s, box-shadow 0.3s;" onmouseover="this.style.transform='translateY(-5px)'; this.style.boxShadow='0 20px 40px rgba(0,0,0,0.05)';" onmouseout="this.style.transform='translateY(0)'; this.style.boxShadow='none';">
                <div style="width: 48px; height: 48px; border-radius: 8px; background: rgba(160,63,163,0.1); color: #A03FA3; display: flex; align-items: center; justify-content: center; margin-bottom: 24px;">
                    <svg width="24" height="24" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M12 4v16m8-8H4"></path></svg>
                </div>
                <h3 style="font-size: 22px; font-weight: 700; color: #1A1A1A; margin-bottom: 12px;">{card2_title}</h3>
                <p style="font-size: 15px; color: #4B5563; line-height: 1.5; margin-bottom: 24px; flex-grow: 1;">{card2_desc}</p>
                <span style="font-size: 14px; font-weight: 700; color: #A03FA3; text-transform: uppercase; letter-spacing: 1px;">{card2_link}</span>
            </a>

            <!-- Card 3 -->
            <a href="{card3_href}" style="text-decoration: none; display: flex; flex-direction: column; background: #F9F9F9; border-radius: 12px; padding: 40px; border: 1px solid #E5E7EB; transition: transform 0.3s, box-shadow 0.3s;" onmouseover="this.style.transform='translateY(-5px)'; this.style.boxShadow='0 20px 40px rgba(0,0,0,0.05)';" onmouseout="this.style.transform='translateY(0)'; this.style.boxShadow='none';">
                <div style="width: 48px; height: 48px; border-radius: 8px; background: rgba(160,63,163,0.1); color: #A03FA3; display: flex; align-items: center; justify-content: center; margin-bottom: 24px;">
                    <svg width="24" height="24" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
                </div>
                <h3 style="font-size: 22px; font-weight: 700; color: #1A1A1A; margin-bottom: 12px;">{card3_title}</h3>
                <p style="font-size: 15px; color: #4B5563; line-height: 1.5; margin-bottom: 24px; flex-grow: 1;">{card3_desc}</p>
                <span style="font-size: 14px; font-weight: 700; color: #A03FA3; text-transform: uppercase; letter-spacing: 1px;">{card3_link}</span>
            </a>
        </div>
    </div>
</section>
"""

    # We want to replace everything from <section class="hero snap-section" to just before <footer class="site-footer">
    # Because there might be extra things, let's use regex.
    pattern = re.compile(r'<section class="hero snap-section"[^>]*>.*?(?=<footer class="site-footer">)', re.DOTALL)
    
    if pattern.search(content):
        content = pattern.sub(new_html, content)
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {file_path}")
    else:
        print(f"Failed to find target section in {file_path}")

update_contact_page('contact_es.html', True)
update_contact_page('contact.html', False)

