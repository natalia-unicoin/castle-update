import glob
import re

def process_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    is_es = '_es.html' in filename or filename == 'gracias.html'

    # 1. Update the Modal HTML
    # We will replace the entire <!-- Waitlist Modal --> ... </div> block.
    # To do this safely, we will use regex to find the start and end.
    modal_start = content.find('<!-- Waitlist Modal -->')
    if modal_start == -1:
        print(f"Modal not found in {filename}")
        return

    # Find the end of the modal. The modal ends just before <script src="./js/mailchimp.js"></script> or </body>
    script_pos = content.find('<script src="./js/mailchimp.js"></script>', modal_start)
    if script_pos == -1:
        script_pos = content.find('</body>', modal_start)
    
    # We need to backtrack to the closing </div> of the modal.
    # Let's just find the last </div> before script_pos.
    last_div = content.rfind('</div>', modal_start, script_pos) + 6
    
    old_modal = content[modal_start:last_div]

    # New Modal Content
    if is_es:
        modal_title = "Únete al Movimiento Castle"
        modal_desc = "Toma el control de tu futuro financiero. Únete a la revolución de riqueza liderada por Mujeres."
        fname_label = "Nombre Completo *"
        email_label = "Correo Electrónico *"
        phone_label = "Número de Teléfono"
        age_label = "Edad"
        country_label = "País"
        linkedin_label = "URL de LinkedIn"
        company_label = "Empresa / Organización"
        role_label = "Tu Rol / Cargo"
        instagram_label = "Usuario de Instagram"
        consent_label = "Doy mi consentimiento para que Castle me contacte con actualizaciones de la plataforma e invitaciones."
        submit_btn = "Enviar Solicitud"
        interest_label = "Estoy interesada en (selecciona todas las opciones que correspondan):"
        opt_waitlist = "Unirme a la lista de espera (Masterclass/App)"
        opt_partner = "Asociarme con Castle"
        opt_contact = "Contacto General"
        opt_news = "Suscribirme al Newsletter"
        age_options = '<option value="" disabled selected>Selecciona rango de edad</option>'
        country_options = '<option value="" disabled selected>Selecciona tu país</option>'
        # Keep same countries for simplicity or translate 'Other'
    else:
        modal_title = "Join the Castle Movement"
        modal_desc = "Take control of your financial future. Join the Women-led Wealth revolution."
        fname_label = "Full Name *"
        email_label = "Email Address *"
        phone_label = "Phone Number"
        age_label = "Age"
        country_label = "Country"
        linkedin_label = "LinkedIn URL"
        company_label = "Company / Organization"
        role_label = "Your Role / Title"
        instagram_label = "Instagram Handle"
        consent_label = "I consent to Castle contacting me to share updates about the platform, launch information, and Community events."
        submit_btn = "Submit Application"
        interest_label = "I am interested in (select all that apply):"
        opt_waitlist = "Join the Waitlist (Masterclass/App)"
        opt_partner = "Partnering with Castle"
        opt_contact = "General Contact"
        opt_news = "Subscribe to Newsletter"
        age_options = '<option value="" disabled selected>Select age range</option>'
        country_options = '<option value="" disabled selected>Select your country</option>'

    # Reconstruct the form inner HTML keeping styling
    new_modal = f"""<!-- Unified CTA Modal -->
    <div id="waitlistModal" style="display: none; position: fixed; top: 0; left: 0; width: 100%; height: 100%; z-index: 99999; background: rgba(17,17,17,0.85); align-items: center; justify-content: center; backdrop-filter: blur(8px);">
        <div style="background: #FFFFFF; padding: 40px 40px; border-radius: 8px; max-width: 650px; width: 90%; position: relative; max-height: 90vh; overflow-y: auto; text-align: left; box-shadow: 0 40px 100px rgba(0,0,0,0.4);">
            <button onclick="document.getElementById('waitlistModal').style.display='none';" style="position: absolute; top: 15px; right: 20px; background: none; border: none; font-size: 30px; cursor: pointer; color: #2A2A2A; line-height: 1; padding: 0;">&times;</button>
            
            <h2 class="section-heading color-reveal" id="modalTitle" style="margin-top: 10px; margin-bottom: 10px; text-align: center; font-size: clamp(32px, 4vw, 42px);">{modal_title}</h2>
            <p style="text-align: center; color: #2A2A2A; font-family: 'Inter', sans-serif; margin-bottom: var(--spacer-30); line-height: 1.5;">{modal_desc}</p>
            
            <form action="https://buildyourcastle.us10.list-manage.com/subscribe/post?u=4766d7bd8debcf610dadddfb6&amp;id=53677e9563" target="_blank" method="POST" id="unifiedForm" class="waitlist-form" onsubmit="prepareUnifiedFormSubmit(event)">
                <input type="hidden" name="SOURCE" id="unifiedSource" value="Waitlist">
                <div aria-hidden="true" style="position: absolute; left: -5000px;"><input type="text" name="b_4766d7bd8debcf610dadddfb6_53677e9563" tabindex="-1" value=""></div>
                
                <!-- Interests Checkboxes -->
                <div class="form-group" style="margin-bottom: 20px; background: #F9FAFB; padding: 20px; border-radius: 6px; border: 1px solid #D1D5DB;">
                    <label style="font-size: 15px; font-weight: 700; color: #1A1A1A; margin-bottom: 15px; display: block;">{interest_label}</label>
                    <div style="display: flex; flex-direction: column; gap: 12px;">
                        <label style="display: flex; align-items: center; gap: 10px; cursor: pointer; font-size: 14px; font-weight: 500;"><input type="checkbox" id="chk_waitlist" value="Waitlist" style="width:18px; height:18px; margin:0;"> {opt_waitlist}</label>
                        <label style="display: flex; align-items: center; gap: 10px; cursor: pointer; font-size: 14px; font-weight: 500;"><input type="checkbox" id="chk_partner" value="Partner" style="width:18px; height:18px; margin:0;"> {opt_partner}</label>
                        <label style="display: flex; align-items: center; gap: 10px; cursor: pointer; font-size: 14px; font-weight: 500;"><input type="checkbox" id="chk_contact" value="Contact" style="width:18px; height:18px; margin:0;"> {opt_contact}</label>
                        <label style="display: flex; align-items: center; gap: 10px; cursor: pointer; font-size: 14px; font-weight: 500;"><input type="checkbox" id="chk_newsletter" value="Newsletter" checked style="width:18px; height:18px; margin:0; accent-color: #A03FA3;"> {opt_news}</label>
                    </div>
                </div>

                <div class="form-row">
                    <div class="form-group">
                        <label for="fname">{fname_label}</label>
                        <input type="text" id="fname" name="FNAME" required placeholder="Jane Doe">
                    </div>
                    <div class="form-group">
                        <label for="email">{email_label}</label>
                        <input type="email" id="email" name="EMAIL" required placeholder="jane@example.com">
                    </div>
                </div>

                <div class="form-row">
                    <div class="form-group">
                        <label for="phone">{phone_label}</label>
                        <input type="tel" id="phone" name="PHONE" placeholder="+1 234 567 8900">
                    </div>
                    <div class="form-group">
                        <label for="age">{age_label}</label>
                        <select id="age" name="AGE">
                            {age_options}
                            <option value="18-24">18-24</option>
                            <option value="25-29">25-29</option>
                            <option value="30-34">30-34</option>
                            <option value="35-39">35-39</option>
                            <option value="40-44">40-44</option>
                            <option value="45-49">45-49</option>
                            <option value="50-54">50-54</option>
                            <option value="55-59">55-59</option>
                            <option value="60+">60+</option>
                        </select>
                    </div>
                </div>

                <div class="form-row">
                    <div class="form-group">
                        <label for="country">{country_label}</label>
                        <select id="country" name="COUNTRY">
                            {country_options}
                            <option value="United States">United States</option>
                            <option value="United Kingdom">United Kingdom</option>
                            <option value="Canada">Canada</option>
                            <option value="Australia">Australia</option>
                            <option value="Argentina">Argentina</option>
                            <option value="Brazil">Brazil</option>
                            <option value="Chile">Chile</option>
                            <option value="Colombia">Colombia</option>
                            <option value="Mexico">Mexico</option>
                            <option value="Peru">Peru</option>
                            <option value="Spain">Spain</option>
                            <option value="Other">Other</option>
                        </select>
                    </div>
                    <div class="form-group">
                        <label for="linkedin">{linkedin_label}</label>
                        <input type="url" id="linkedin" name="LINKEDIN" placeholder="https://linkedin.com/in/janedoe">
                    </div>
                </div>

                <div class="form-row">
                    <div class="form-group">
                        <label for="company">{company_label}</label>
                        <input type="text" id="company" name="COMPANY" placeholder="Acme Corp">
                    </div>
                    <div class="form-group">
                        <label for="role">{role_label}</label>
                        <input type="text" id="role" name="ROLE" placeholder="Founder / CEO">
                    </div>
                </div>

                <div class="form-group">
                    <label for="instagram">{instagram_label}</label>
                    <input type="text" id="instagram" name="INSTAGRAM" placeholder="@janedoe">
                </div>

                <div class="checkbox-group" style="margin-top: 15px;">
                    <input type="checkbox" id="consent" name="CONSENT" required style="width: 18px; height: 18px;">
                    <label for="consent" style="margin-left: 8px;">{consent_label}</label>
                </div>

                <!-- Anti-spam Honeypot -->
                <div style="position: absolute; left: -5000px;" aria-hidden="true"><input type="text" name="b_name" tabindex="-1" value=""></div>

                <button type="submit" class="waitlist-submit" style="margin-top: 20px;">{submit_btn}</button>
            </form>
        </div>
    </div>"""

    content = content[:modal_start] + new_modal + content[last_div:]

    # 2. Inject Javascript for Unified Form
    js_code = """
    <script>
        function openUnifiedModal(sourceType) {
            // Uncheck all main interests first
            document.getElementById('chk_waitlist').checked = false;
            document.getElementById('chk_partner').checked = false;
            document.getElementById('chk_contact').checked = false;
            
            // Always keep newsletter checked by default
            document.getElementById('chk_newsletter').checked = true;

            // Check based on source
            if (sourceType === 'waitlist') {
                document.getElementById('chk_waitlist').checked = true;
            } else if (sourceType === 'partner') {
                document.getElementById('chk_partner').checked = true;
            } else if (sourceType === 'contact') {
                document.getElementById('chk_contact').checked = true;
            } else if (sourceType === 'newsletter') {
                // If they specifically clicked newsletter, we just ensure it's checked
                document.getElementById('chk_newsletter').checked = true;
            }

            // Show modal
            document.getElementById('waitlistModal').style.display = 'flex';
        }

        function prepareUnifiedFormSubmit(e) {
            // Intercept submit to populate SOURCE with all checked interests
            let interests = [];
            if (document.getElementById('chk_waitlist').checked) interests.push("Waitlist");
            if (document.getElementById('chk_partner').checked) interests.push("Partner");
            if (document.getElementById('chk_contact').checked) interests.push("Contact");
            if (document.getElementById('chk_newsletter').checked) interests.push("Newsletter");
            
            if (interests.length === 0) {
                interests.push("No specific interest");
            }

            document.getElementById('unifiedSource').value = interests.join(", ");
        }
    </script>
    """
    if 'function openUnifiedModal' not in content:
        content = content.replace('</body>', js_code + '\n</body>')

    # 3. Replace all inline onclicks
    # Replace old waitlist modal opens
    content = content.replace("document.getElementById('waitlistModal').style.display='flex';", "openUnifiedModal('waitlist');")
    
    # Update Footer Newsletter forms
    # We replace the entire form block with a button.
    # We need to find: <form class="subscribe-form"...> ... </form>
    import re
    news_btn_text = "SUSCRIBIRSE" if is_es else "SUBSCRIBE"
    news_desc = "Únete al movimiento. Recibe las últimas novedades sobre la construcción de Riqueza e inversiones directamente en tu bandeja de entrada." if is_es else "Join the movement. Get the latest insights on Wealth building and investments sent straight to your inbox."
    news_title = "Suscríbete a nuestro Newsletter" if is_es else "Subscribe to our Newsletter"
    
    # We can just replace the form with a button
    btn_html = f'<button onclick="openUnifiedModal(\\\'newsletter\\\')" style="background-color: #A03FA3; color: #FFFFFF; font-weight: 800; letter-spacing: 1.5px; padding: 16px 40px; border-radius: 50px; border: none; font-size: 14px; cursor: pointer; transition: background 0.2s, transform 0.2s; box-shadow: 0 4px 15px rgba(160,63,163,0.3); font-family: \\\'Inter Tight\\\', sans-serif; text-transform: uppercase;">{news_btn_text}</button>'
    
    content = re.sub(
        r'<form[^>]*class="subscribe-form"[^>]*>.*?</form>',
        btn_html.replace('\\\'', "'"),
        content,
        flags=re.DOTALL
    )

    # 4. Handle Contact Page Embedded Form
    if filename in ['contact.html', 'contact_es.html']:
        # Contact page has an embedded form: <form action="https://buildyourcastle... class="waitlist-form" target="_blank"> ... </form>
        # Let's replace it with a button container
        contact_btn_text = "CONTACTAR AHORA" if is_es else "CONTACT US NOW"
        btn_container = f'''<div style="text-align: center; margin-top: 40px; margin-bottom: 40px;">
            <p style="font-size: 18px; margin-bottom: 20px; color: #4B5563;">{"Haz clic abajo para abrir nuestro formulario de contacto unificado." if is_es else "Click below to open our unified contact form."}</p>
            <button onclick="openUnifiedModal('contact')" style="background-color: #A03FA3; color: #FFFFFF; font-weight: 800; letter-spacing: 2px; padding: 18px 45px; border-radius: 50px; border: none; font-size: 15px; cursor: pointer; transition: transform 0.2s; box-shadow: 0 10px 20px rgba(160, 63, 163, 0.3); text-transform: uppercase;">{contact_btn_text}</button>
        </div>'''
        
        # Regex to find the embedded form inside contact page
        # Usually starts with <form action=... class="waitlist-form"
        content = re.sub(
            r'<form[^>]*class="waitlist-form"[^>]*>.*?</form>',
            btn_container,
            content,
            flags=re.DOTALL,
            count=1 # Only replace the first one (the embedded one), the modal one is already unified above!
        )
        
        # Wait, the modal is also class="waitlist-form". BUT we already replaced the modal, and our new modal has id="unifiedForm".
        # So we can safely replace the embedded form. Wait, the regex above might replace the modal if it comes first.
        # Let's be careful. Let's do this replacement BEFORE updating the modal!
        pass # I will adjust the script below.

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Processed {filename}")

# Adjusted processing sequence
def process_file_safe(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
        
    is_es = '_es.html' in filename or filename == 'gracias.html'

    # Step A: Update Contact Page Embedded Form
    # If contact page, find the FIRST form with class="waitlist-form" and NO id="waitlistForm"
    if filename in ['contact.html', 'contact_es.html']:
        contact_btn_text = "CONTACTAR AHORA" if is_es else "CONTACT US NOW"
        btn_container = f'''<div style="text-align: center; margin-top: 40px; margin-bottom: 40px;">
            <p style="font-size: 18px; margin-bottom: 20px; color: #4B5563; font-family: 'Inter', sans-serif;">{"Haz clic abajo para abrir nuestro formulario de contacto." if is_es else "Click below to open our contact form."}</p>
            <button onclick="openUnifiedModal('contact')" style="background-color: #A03FA3; color: #FFFFFF; font-weight: 800; letter-spacing: 2px; padding: 18px 45px; border-radius: 50px; border: none; font-size: 15px; cursor: pointer; transition: transform 0.2s; box-shadow: 0 10px 20px rgba(160, 63, 163, 0.3); text-transform: uppercase; display: inline-block;">{contact_btn_text}</button>
        </div>'''
        
        # We find the embedded form block manually
        form_start = content.find('<form')
        while form_start != -1:
            form_end = content.find('</form>', form_start) + 7
            form_block = content[form_start:form_end]
            if 'class="waitlist-form"' in form_block and 'id="waitlistForm"' not in form_block:
                content = content[:form_start] + btn_container + content[form_end:]
                break
            form_start = content.find('<form', form_end)

    # Step B: Update Partner Buttons
    if is_es:
        content = content.replace('href="#partner-form"', 'href="javascript:void(0);" onclick="openUnifiedModal(\'partner\')"')
    else:
        content = content.replace('href="#partner-form"', 'href="javascript:void(0);" onclick="openUnifiedModal(\'partner\')"')

    # Step C: Update Footer Newsletter Form
    news_btn_text = "SUSCRIBIRSE" if is_es else "SUBSCRIBE"
    btn_html = f'<button onclick="openUnifiedModal(\\\'newsletter\\\')" style="background-color: #A03FA3; color: #FFFFFF; font-weight: 800; letter-spacing: 1.5px; padding: 16px 40px; border-radius: 50px; border: none; font-size: 14px; cursor: pointer; transition: background 0.2s, transform 0.2s; box-shadow: 0 4px 15px rgba(160,63,163,0.3); font-family: \\\'Inter Tight\\\', sans-serif; text-transform: uppercase;">{news_btn_text}</button>'
    content = re.sub(r'<form[^>]*class="subscribe-form"[^>]*>.*?</form>', btn_html.replace('\\\'', "'"), content, flags=re.DOTALL)

    # Step D: Update the Modal
    modal_start = content.find('<!-- Waitlist Modal -->')
    if modal_start != -1:
        script_pos = content.find('<script src="./js/mailchimp.js"></script>', modal_start)
        if script_pos == -1: script_pos = content.find('</body>', modal_start)
        last_div = content.rfind('</div>', modal_start, script_pos) + 6
        
        if is_es:
            modal_title = "Únete al Movimiento Castle"
            modal_desc = "Toma el control de tu futuro financiero. Únete a la revolución de riqueza liderada por Mujeres."
            fname_label = "Nombre Completo *"
            email_label = "Correo Electrónico *"
            phone_label = "Número de Teléfono"
            age_label = "Edad"
            country_label = "País"
            linkedin_label = "URL de LinkedIn"
            company_label = "Empresa / Organización"
            role_label = "Tu Rol / Cargo"
            instagram_label = "Usuario de Instagram"
            consent_label = "Doy mi consentimiento para que Castle me contacte con actualizaciones de la plataforma e invitaciones."
            submit_btn = "Enviar Solicitud"
            interest_label = "Estoy interesada en (selecciona todas las opciones que correspondan):"
            opt_waitlist = "Unirme a la lista de espera (Masterclass/App)"
            opt_partner = "Asociarme con Castle"
            opt_contact = "Contacto General"
            opt_news = "Suscribirme al Newsletter"
            age_options = '<option value="" disabled selected>Selecciona rango de edad</option>'
            country_options = '<option value="" disabled selected>Selecciona tu país</option>'
        else:
            modal_title = "Join the Castle Movement"
            modal_desc = "Take control of your financial future. Join the Women-led Wealth revolution."
            fname_label = "Full Name *"
            email_label = "Email Address *"
            phone_label = "Phone Number"
            age_label = "Age"
            country_label = "Country"
            linkedin_label = "LinkedIn URL"
            company_label = "Company / Organization"
            role_label = "Your Role / Title"
            instagram_label = "Instagram Handle"
            consent_label = "I consent to Castle contacting me to share updates about the platform, launch information, and Community events."
            submit_btn = "Submit Application"
            interest_label = "I am interested in (select all that apply):"
            opt_waitlist = "Join the Waitlist (Masterclass/App)"
            opt_partner = "Partnering with Castle"
            opt_contact = "General Contact"
            opt_news = "Subscribe to Newsletter"
            age_options = '<option value="" disabled selected>Select age range</option>'
            country_options = '<option value="" disabled selected>Select your country</option>'

        new_modal = f"""<!-- Unified CTA Modal -->
    <div id="waitlistModal" style="display: none; position: fixed; top: 0; left: 0; width: 100%; height: 100%; z-index: 99999; background: rgba(17,17,17,0.85); align-items: center; justify-content: center; backdrop-filter: blur(8px);">
        <div style="background: #FFFFFF; padding: 40px 40px; border-radius: 8px; max-width: 650px; width: 90%; position: relative; max-height: 90vh; overflow-y: auto; text-align: left; box-shadow: 0 40px 100px rgba(0,0,0,0.4);">
            <button onclick="document.getElementById('waitlistModal').style.display='none';" style="position: absolute; top: 15px; right: 20px; background: none; border: none; font-size: 30px; cursor: pointer; color: #2A2A2A; line-height: 1; padding: 0;">&times;</button>
            
            <h2 class="section-heading color-reveal" id="modalTitle" style="margin-top: 10px; margin-bottom: 10px; text-align: center; font-size: clamp(32px, 4vw, 42px);">{modal_title}</h2>
            <p style="text-align: center; color: #2A2A2A; font-family: 'Inter', sans-serif; margin-bottom: var(--spacer-30); line-height: 1.5;">{modal_desc}</p>
            
            <form action="https://buildyourcastle.us10.list-manage.com/subscribe/post?u=4766d7bd8debcf610dadddfb6&amp;id=53677e9563" target="_blank" method="POST" id="unifiedForm" class="waitlist-form" onsubmit="prepareUnifiedFormSubmit(event)">
                <input type="hidden" name="SOURCE" id="unifiedSource" value="Waitlist">
                <div aria-hidden="true" style="position: absolute; left: -5000px;"><input type="text" name="b_4766d7bd8debcf610dadddfb6_53677e9563" tabindex="-1" value=""></div>
                
                <!-- Interests Checkboxes -->
                <div class="form-group" style="margin-bottom: 20px; background: #F9FAFB; padding: 20px; border-radius: 6px; border: 1px solid #D1D5DB;">
                    <label style="font-size: 15px; font-weight: 700; color: #1A1A1A; margin-bottom: 15px; display: block;">{interest_label}</label>
                    <div style="display: flex; flex-direction: column; gap: 12px;">
                        <label style="display: flex; align-items: center; gap: 10px; cursor: pointer; font-size: 14px; font-weight: 500;"><input type="checkbox" id="chk_waitlist" value="Waitlist" style="width:18px; height:18px; margin:0;"> {opt_waitlist}</label>
                        <label style="display: flex; align-items: center; gap: 10px; cursor: pointer; font-size: 14px; font-weight: 500;"><input type="checkbox" id="chk_partner" value="Partner" style="width:18px; height:18px; margin:0;"> {opt_partner}</label>
                        <label style="display: flex; align-items: center; gap: 10px; cursor: pointer; font-size: 14px; font-weight: 500;"><input type="checkbox" id="chk_contact" value="Contact" style="width:18px; height:18px; margin:0;"> {opt_contact}</label>
                        <label style="display: flex; align-items: center; gap: 10px; cursor: pointer; font-size: 14px; font-weight: 500;"><input type="checkbox" id="chk_newsletter" value="Newsletter" checked style="width:18px; height:18px; margin:0; accent-color: #A03FA3;"> {opt_news}</label>
                    </div>
                </div>

                <div class="form-row">
                    <div class="form-group">
                        <label for="fname">{fname_label}</label>
                        <input type="text" id="fname" name="FNAME" required placeholder="Jane Doe">
                    </div>
                    <div class="form-group">
                        <label for="email">{email_label}</label>
                        <input type="email" id="email" name="EMAIL" required placeholder="jane@example.com">
                    </div>
                </div>

                <div class="form-row">
                    <div class="form-group">
                        <label for="phone">{phone_label}</label>
                        <input type="tel" id="phone" name="PHONE" placeholder="+1 234 567 8900">
                    </div>
                    <div class="form-group">
                        <label for="age">{age_label}</label>
                        <select id="age" name="AGE">
                            {age_options}
                            <option value="18-24">18-24</option>
                            <option value="25-29">25-29</option>
                            <option value="30-34">30-34</option>
                            <option value="35-39">35-39</option>
                            <option value="40-44">40-44</option>
                            <option value="45-49">45-49</option>
                            <option value="50-54">50-54</option>
                            <option value="55-59">55-59</option>
                            <option value="60+">60+</option>
                        </select>
                    </div>
                </div>

                <div class="form-row">
                    <div class="form-group">
                        <label for="country">{country_label}</label>
                        <select id="country" name="COUNTRY">
                            {country_options}
                            <option value="United States">United States</option>
                            <option value="United Kingdom">United Kingdom</option>
                            <option value="Canada">Canada</option>
                            <option value="Australia">Australia</option>
                            <option value="Argentina">Argentina</option>
                            <option value="Brazil">Brazil</option>
                            <option value="Chile">Chile</option>
                            <option value="Colombia">Colombia</option>
                            <option value="Mexico">Mexico</option>
                            <option value="Peru">Peru</option>
                            <option value="Spain">Spain</option>
                            <option value="Other">Other</option>
                        </select>
                    </div>
                    <div class="form-group">
                        <label for="linkedin">{linkedin_label}</label>
                        <input type="url" id="linkedin" name="LINKEDIN" placeholder="https://linkedin.com/in/janedoe">
                    </div>
                </div>

                <div class="form-row">
                    <div class="form-group">
                        <label for="company">{company_label}</label>
                        <input type="text" id="company" name="COMPANY" placeholder="Acme Corp">
                    </div>
                    <div class="form-group">
                        <label for="role">{role_label}</label>
                        <input type="text" id="role" name="ROLE" placeholder="Founder / CEO">
                    </div>
                </div>

                <div class="form-group">
                    <label for="instagram">{instagram_label}</label>
                    <input type="text" id="instagram" name="INSTAGRAM" placeholder="@janedoe">
                </div>

                <div class="checkbox-group" style="margin-top: 15px;">
                    <input type="checkbox" id="consent" name="CONSENT" required style="width: 18px; height: 18px;">
                    <label for="consent" style="margin-left: 8px;">{consent_label}</label>
                </div>

                <!-- Anti-spam Honeypot -->
                <div style="position: absolute; left: -5000px;" aria-hidden="true"><input type="text" name="b_name" tabindex="-1" value=""></div>

                <button type="submit" class="waitlist-submit" style="margin-top: 20px;">{submit_btn}</button>
            </form>
        </div>
    </div>"""
        
        content = content[:modal_start] + new_modal + content[last_div:]

    # Step E: Replace JS calls and inject the script
    content = content.replace("document.getElementById('waitlistModal').style.display='flex';", "openUnifiedModal('waitlist');")
    
    js_code = """
    <script>
        function openUnifiedModal(sourceType) {
            // Uncheck all main interests first
            if(document.getElementById('chk_waitlist')) document.getElementById('chk_waitlist').checked = false;
            if(document.getElementById('chk_partner')) document.getElementById('chk_partner').checked = false;
            if(document.getElementById('chk_contact')) document.getElementById('chk_contact').checked = false;
            
            // Always keep newsletter checked by default
            if(document.getElementById('chk_newsletter')) document.getElementById('chk_newsletter').checked = true;

            // Check based on source
            if (sourceType === 'waitlist') {
                if(document.getElementById('chk_waitlist')) document.getElementById('chk_waitlist').checked = true;
            } else if (sourceType === 'partner') {
                if(document.getElementById('chk_partner')) document.getElementById('chk_partner').checked = true;
            } else if (sourceType === 'contact') {
                if(document.getElementById('chk_contact')) document.getElementById('chk_contact').checked = true;
            } else if (sourceType === 'newsletter') {
                // If they specifically clicked newsletter, we just ensure it's checked
                if(document.getElementById('chk_newsletter')) document.getElementById('chk_newsletter').checked = true;
            }

            // Show modal
            if(document.getElementById('waitlistModal')) document.getElementById('waitlistModal').style.display = 'flex';
        }

        function prepareUnifiedFormSubmit(e) {
            // Intercept submit to populate SOURCE with all checked interests
            let interests = [];
            if (document.getElementById('chk_waitlist') && document.getElementById('chk_waitlist').checked) interests.push("Waitlist");
            if (document.getElementById('chk_partner') && document.getElementById('chk_partner').checked) interests.push("Partner");
            if (document.getElementById('chk_contact') && document.getElementById('chk_contact').checked) interests.push("Contact");
            if (document.getElementById('chk_newsletter') && document.getElementById('chk_newsletter').checked) interests.push("Newsletter");
            
            if (interests.length === 0) {
                interests.push("No specific interest");
            }

            if(document.getElementById('unifiedSource')) document.getElementById('unifiedSource').value = interests.join(", ");
        }
    </script>
    """
    if 'function openUnifiedModal' not in content:
        content = content.replace('</body>', js_code + '\n</body>')

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Processed {filename}")

for file in glob.glob("*.html"):
    if file == 'index_backup_28abr.html': continue
    process_file_safe(file)

