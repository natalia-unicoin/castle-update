import re

with open('inject_dynamic_form_es.py', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add intl-tel-input CSS to the modal (before <style> or inside it)
# We will inject the CSS link in the new_modal string
css_link = """<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/intl-tel-input@18.2.1/build/css/intlTelInput.css">
    <style>
        .iti { width: 100%; display: block; }
        .iti__flag {background-image: url("https://cdn.jsdelivr.net/npm/intl-tel-input@18.2.1/build/img/flags.png");}
        @media (min-resolution: 2x) { .iti__flag {background-image: url("https://cdn.jsdelivr.net/npm/intl-tel-input@18.2.1/build/img/flags@2x.png");} }
    </style>"""

content = content.replace('<!-- Unified CTA Modal -->', '<!-- Unified CTA Modal -->\n    ' + css_link)

# 2. Revert Company/Role and Phone changes
# Replace the current Company/Role in base fields and Phone select
old_base_fields = """<div class="form-row" style="margin-top: 15px;">
                    <div class="form-group">
                        <label for="company" style="font-weight: 600; font-size: 13px; color: #4B5563;">Empresa</label>
                        <input type="text" id="company" name="COMPANY" placeholder="Ej. Acme Corp" style="border-radius: 6px; border: 1px solid #D1D5DB; padding: 12px; width: 100%; font-size: 15px;">
                    </div>
                    <div class="form-group">
                        <label for="role" style="font-weight: 600; font-size: 13px; color: #4B5563;">Cargo</label>
                        <input type="text" id="role" name="ROLE" placeholder="Ej. Founder / CEO" style="border-radius: 6px; border: 1px solid #D1D5DB; padding: 12px; width: 100%; font-size: 15px;">
                    </div>
                </div>
                <div class="form-row" style="margin-top: 15px;">
                    <div class="form-group">
                        <label for="country" style="font-weight: 600; font-size: 13px; color: #4B5563;">País de Residencia *</label>
                        <select id="country" name="COUNTRY" required style="border-radius: 6px; border: 1px solid #D1D5DB; padding: 12px; width: 100%; font-size: 15px; background: #fff;">
                            <option value="" disabled selected>Selecciona tu país</option>
                            <option value="Estados Unidos">Estados Unidos</option>
                            <option value="España">España</option>
                            <option value="México">México</option>
                            <option value="Argentina">Argentina</option>
                            <option value="Colombia">Colombia</option>
                            <option value="Chile">Chile</option>
                            <option value="Perú">Perú</option>
                            <option value="Ecuador">Ecuador</option>
                            <option value="Uruguay">Uruguay</option>
                            <option value="Venezuela">Venezuela</option>
                            <option value="Guatemala">Guatemala</option>
                            <option value="Costa Rica">Costa Rica</option>
                            <option value="Panamá">Panamá</option>
                            <option value="El Salvador">El Salvador</option>
                            <option value="Honduras">Honduras</option>
                            <option value="Nicaragua">Nicaragua</option>
                            <option value="Bolivia">Bolivia</option>
                            <option value="Paraguay">Paraguay</option>
                            <option value="República Dominicana">República Dominicana</option>
                            <option value="Puerto Rico">Puerto Rico</option>
                            <option value="Otro">Otro</option>
                        </select>
                    </div>
                    <div class="form-group">
                        <label style="font-weight: 600; font-size: 13px; color: #4B5563;">Teléfono *</label>
                        <div style="display: flex; gap: 8px;">
                            <select id="phone_code" required style="border-radius: 6px; border: 1px solid #D1D5DB; padding: 12px 8px; width: 40%; font-size: 14px; background: #fff;">
                                <option value="+1">🇺🇸 +1</option>
                                <option value="+34">🇪🇸 +34</option>
                                <option value="+52">🇲🇽 +52</option>
                                <option value="+54">🇦🇷 +54</option>
                                <option value="+57">🇨🇴 +57</option>
                                <option value="+56">🇨🇱 +56</option>
                                <option value="+51">🇵🇪 +51</option>
                                <option value="+593">🇪🇨 +593</option>
                                <option value="+598">🇺🇾 +598</option>
                                <option value="+58">🇻🇪 +58</option>
                                <option value="+502">🇬🇹 +502</option>
                                <option value="+506">🇨🇷 +506</option>
                                <option value="+507">🇵🇦 +507</option>
                                <option value="+503">🇸🇻 +503</option>
                                <option value="+504">🇭🇳 +504</option>
                                <option value="+505">🇳🇮 +505</option>
                                <option value="+591">🇧🇴 +591</option>
                                <option value="+595">🇵🇾 +595</option>
                                <option value="+1">🇵🇷 +1</option>
                                <option value="+1">🇩🇴 +1</option>
                                <option value="">Otro</option>
                            </select>
                            <input type="tel" id="phone_num" required placeholder="Número" style="border-radius: 6px; border: 1px solid #D1D5DB; padding: 12px; width: 60%; font-size: 15px;">
                        </div>
                    </div>
                </div>"""

new_base_fields = """<div class="form-row" style="margin-top: 15px;">
                    <div class="form-group">
                        <label for="country" style="font-weight: 600; font-size: 13px; color: #4B5563;">País de Residencia *</label>
                        <select id="country" name="COUNTRY" required style="border-radius: 6px; border: 1px solid #D1D5DB; padding: 12px; width: 100%; font-size: 15px; background: #fff;">
                            <option value="" disabled selected>Selecciona tu país</option>
                            <option value="Estados Unidos">Estados Unidos</option>
                            <option value="España">España</option>
                            <option value="México">México</option>
                            <option value="Argentina">Argentina</option>
                            <option value="Colombia">Colombia</option>
                            <option value="Chile">Chile</option>
                            <option value="Perú">Perú</option>
                            <option value="Ecuador">Ecuador</option>
                            <option value="Uruguay">Uruguay</option>
                            <option value="Venezuela">Venezuela</option>
                            <option value="Guatemala">Guatemala</option>
                            <option value="Costa Rica">Costa Rica</option>
                            <option value="Panamá">Panamá</option>
                            <option value="El Salvador">El Salvador</option>
                            <option value="Honduras">Honduras</option>
                            <option value="Nicaragua">Nicaragua</option>
                            <option value="Bolivia">Bolivia</option>
                            <option value="Paraguay">Paraguay</option>
                            <option value="República Dominicana">República Dominicana</option>
                            <option value="Puerto Rico">Puerto Rico</option>
                            <option value="Otro">Otro</option>
                        </select>
                    </div>
                    <div class="form-group">
                        <label for="phone_intl" style="font-weight: 600; font-size: 13px; color: #4B5563; display:block;">Teléfono *</label>
                        <input type="tel" id="phone_intl" required style="border-radius: 6px; border: 1px solid #D1D5DB; padding: 12px 12px 12px 50px; font-size: 15px; width: 100%; outline: none; box-sizing: border-box;">
                    </div>
                </div>"""

content = content.replace(old_base_fields, new_base_fields)

# 3. Add Company and Role to dyn_partner
old_partner = """<div class="form-group" style="margin-top: 15px;">
                        <label for="partnermsg" style="font-weight: 600; font-size: 13px; color: #4B5563;">Comentarios adicionales (Opcional)</label>
                        <textarea id="partnermsg" name="PARTNERMSG" rows="3" placeholder="Cuéntanos más sobre cómo te gustaría colaborar..." style="border-radius: 6px; border: 1px solid #D1D5DB; padding: 12px; width: 100%; font-size: 15px; font-family: inherit; resize: vertical;"></textarea>
                    </div>"""
                    
new_partner = """<div class="form-row" style="margin-top: 15px;">
                        <div class="form-group">
                            <label for="company" style="font-weight: 600; font-size: 13px; color: #4B5563;">Empresa</label>
                            <input type="text" id="company" name="COMPANY" placeholder="Ej. Acme Corp" style="border-radius: 6px; border: 1px solid #D1D5DB; padding: 12px; width: 100%; font-size: 15px;">
                        </div>
                        <div class="form-group">
                            <label for="role" style="font-weight: 600; font-size: 13px; color: #4B5563;">Cargo</label>
                            <input type="text" id="role" name="ROLE" placeholder="Ej. Founder / CEO" style="border-radius: 6px; border: 1px solid #D1D5DB; padding: 12px; width: 100%; font-size: 15px;">
                        </div>
                    </div>
                    <div class="form-group" style="margin-top: 15px;">
                        <label for="partnermsg" style="font-weight: 600; font-size: 13px; color: #4B5563;">Comentarios adicionales (Opcional)</label>
                        <textarea id="partnermsg" name="PARTNERMSG" rows="3" placeholder="Cuéntanos más sobre cómo te gustaría colaborar..." style="border-radius: 6px; border: 1px solid #D1D5DB; padding: 12px; width: 100%; font-size: 15px; font-family: inherit; resize: vertical;"></textarea>
                    </div>"""
                    
content = content.replace(old_partner, new_partner)

# 4. Add JS initialization for intl-tel-input
js_libs = """    <script src="https://cdn.jsdelivr.net/npm/intl-tel-input@18.2.1/build/js/intlTelInput.min.js"></script>
    <script>
        let iti;
        document.addEventListener("DOMContentLoaded", function() {
            const phoneInput = document.querySelector("#phone_intl");
            if (phoneInput) {
                iti = window.intlTelInput(phoneInput, {
                    utilsScript: "https://cdn.jsdelivr.net/npm/intl-tel-input@18.2.1/build/js/utils.js",
                    preferredCountries: ['es', 'us', 'mx', 'ar', 'co'],
                    separateDialCode: true
                });
            }"""
            
content = content.replace('document.addEventListener("DOMContentLoaded", function() {', js_libs)

# 5. Fix Mailchimp submission logic
old_mc = """            for (const [key, value] of formData.entries()) {
                params.append(key, value);
            }
            // Append concatenated phone
            const phoneCode = document.getElementById('phone_code').value;
            const phoneNum = document.getElementById('phone_num').value;
            params.append('PHONE', phoneCode + ' ' + phoneNum);"""

new_mc = """            for (const [key, value] of formData.entries()) {
                params.append(key, value);
            }
            // Append formatted phone using intl-tel-input
            if(iti && iti.isValidNumber()) {
                params.append('PHONE', iti.getNumber());
            } else if (iti) {
                params.append('PHONE', document.getElementById('phone_intl').value); // fallback
            }"""

content = content.replace(old_mc, new_mc)

with open('inject_dynamic_form_es.py', 'w', encoding='utf-8') as f:
    f.write(content)

