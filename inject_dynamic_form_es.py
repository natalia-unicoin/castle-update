import glob
import re

def process_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the modal
    modal_start = content.find('<!-- Unified CTA Modal -->')
    if modal_start == -1:
        modal_start = content.find('<!-- Waitlist Modal -->')
        if modal_start == -1:
            print(f"Modal not found in {filename}")
            return
            
    script_pos = content.find('<script src="./js/mailchimp.js"></script>', modal_start)
    if script_pos == -1: script_pos = content.find('</body>', modal_start)
    last_div = content.rfind('</div>', modal_start, script_pos) + 6
    
    new_modal = """<!-- Unified CTA Modal -->
    <div id="waitlistModal" style="display: none; position: fixed; top: 0; left: 0; width: 100%; height: 100%; z-index: 99999; background: rgba(17,17,17,0.85); align-items: center; justify-content: center; backdrop-filter: blur(8px);">
        <div style="background: #FFFFFF; padding: 40px 40px; border-radius: 8px; max-width: 600px; width: 90%; position: relative; max-height: 90vh; overflow-y: auto; text-align: left; box-shadow: 0 40px 100px rgba(0,0,0,0.4); font-family: 'Inter', sans-serif;">
            <button onclick="document.getElementById('waitlistModal').style.display='none';" style="position: absolute; top: 15px; right: 20px; background: none; border: none; font-size: 30px; cursor: pointer; color: #2A2A2A; line-height: 1; padding: 0;">&times;</button>
            
            <h2 class="section-heading color-reveal" id="modalTitle" style="margin-top: 10px; margin-bottom: 10px; text-align: center; font-size: clamp(28px, 4vw, 36px);">Únete a Castle</h2>
            <p style="text-align: center; color: #4B5563; margin-bottom: 25px; line-height: 1.5; font-size: 15px;">Cuéntanos cómo quieres involucrarte.</p>
            
            <form id="unifiedForm" class="waitlist-form" onsubmit="event.preventDefault(); submitMailchimpJSONP(this);">
                <input type="hidden" name="SOURCE" id="unifiedSource" value="">
                
                <!-- Interests Checkboxes -->
                <div class="form-group" style="margin-bottom: 25px; background: #F9FAFB; padding: 20px; border-radius: 8px; border: 1px solid #E5E7EB;">
                    <label style="font-size: 14px; font-weight: 700; color: #111827; margin-bottom: 12px; display: block; text-transform: uppercase; letter-spacing: 0.5px;">Quiero (selecciona todas las que apliquen):</label>
                    <div style="display: flex; flex-direction: column; gap: 10px;">
                        <label style="display: flex; align-items: center; gap: 10px; cursor: pointer; font-size: 15px; color: #374151;">
                            <input type="checkbox" id="chk_masterclass" value="Masterclass" style="width:18px; height:18px; margin:0; accent-color: #A03FA3;"> Participar en la Masterclass
                        </label>
                        <label style="display: flex; align-items: center; gap: 10px; cursor: pointer; font-size: 15px; color: #374151;">
                            <input type="checkbox" id="chk_waitlist" value="Waitlist" style="width:18px; height:18px; margin:0; accent-color: #A03FA3;"> Unirme a la waitlist
                        </label>
                        <label style="display: flex; align-items: center; gap: 10px; cursor: pointer; font-size: 15px; color: #374151;">
                            <input type="checkbox" id="chk_partner" value="Partner" style="width:18px; height:18px; margin:0; accent-color: #A03FA3;"> Ser Partner
                        </label>
                        <label style="display: flex; align-items: center; gap: 10px; cursor: pointer; font-size: 15px; color: #374151;">
                            <input type="checkbox" id="chk_contact" value="Contact" style="width:18px; height:18px; margin:0; accent-color: #A03FA3;"> Hablar con el equipo
                        </label>
                        <label style="display: flex; align-items: center; gap: 10px; cursor: pointer; font-size: 15px; color: #374151;">
                            <input type="checkbox" id="chk_newsletter" value="Newsletter" checked style="width:18px; height:18px; margin:0; accent-color: #A03FA3;"> Recibir novedades
                        </label>
                    </div>
                </div>

                <div class="form-row">
                    <div class="form-group">
                        <label for="fname" style="font-weight: 600; font-size: 13px; color: #4B5563;">Nombre Completo *</label>
                        <input type="text" id="fname" name="FNAME" required placeholder="Tu nombre" style="border-radius: 6px; border: 1px solid #D1D5DB; padding: 12px; width: 100%; font-size: 15px;">
                    </div>
                    <div class="form-group">
                        <label for="email" style="font-weight: 600; font-size: 13px; color: #4B5563;">Correo Electrónico *</label>
                        <input type="email" id="email" name="EMAIL" required placeholder="tu@email.com" style="border-radius: 6px; border: 1px solid #D1D5DB; padding: 12px; width: 100%; font-size: 15px;">
                    </div>
                </div>
                <div class="form-row" style="margin-top: 15px;">
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
                </div>

                <!-- DYNAMIC FIELDS -->
                
                <!-- Contact Message -->
                <div class="form-group" id="dyn_contact" style="display: none; margin-top: 15px;">
                    <label for="message" style="font-weight: 600; font-size: 13px; color: #4B5563;">Mensaje</label>
                    <textarea id="message" name="MESSAGE" rows="3" placeholder="¿En qué te podemos ayudar?" style="border-radius: 6px; border: 1px solid #D1D5DB; padding: 12px; width: 100%; font-size: 15px; font-family: inherit; resize: vertical;"></textarea>
                </div>

                <!-- Partner Type -->
                <div id="dyn_partner" style="display: none; margin-top: 15px;">
                    <div class="form-group">
                        <label for="partnertype" style="font-weight: 600; font-size: 13px; color: #4B5563;">Tipo de Colaboración</label>
                        <select id="partnertype" name="PARTNERT" style="border-radius: 6px; border: 1px solid #D1D5DB; padding: 12px; width: 100%; font-size: 15px; background: #fff;">
                            <option value="" disabled selected>Selecciona una opción</option>
                            <option value="creator">Creator</option>
                            <option value="brand">Brand</option>
                            <option value="organization">Organization</option>
                            <option value="expert">Expert</option>
                        </select>
                    </div>
                    <div class="form-group" style="margin-top: 15px;">
                        <label for="partnermsg" style="font-weight: 600; font-size: 13px; color: #4B5563;">Comentarios adicionales (Opcional)</label>
                        <textarea id="partnermsg" name="PARTNERMSG" rows="3" placeholder="Cuéntanos más sobre cómo te gustaría colaborar..." style="border-radius: 6px; border: 1px solid #D1D5DB; padding: 12px; width: 100%; font-size: 15px; font-family: inherit; resize: vertical;"></textarea>
                    </div>
                </div>

                <!-- Invested / Interest -->
                <div id="dyn_invest" style="display: none; margin-top: 15px;">
                    <div class="form-row">
                        <div class="form-group">
                            <label style="font-weight: 600; font-size: 13px; color: #4B5563;">¿Has invertido antes?</label>
                            <div style="display: flex; gap: 20px; margin-top: 8px;">
                                <label style="display: flex; align-items: center; gap: 5px; font-size: 15px;"><input type="radio" name="INVESTED" value="Si" style="accent-color: #A03FA3;"> Sí</label>
                                <label style="display: flex; align-items: center; gap: 5px; font-size: 15px;"><input type="radio" name="INVESTED" value="No" style="accent-color: #A03FA3;"> No</label>
                            </div>
                        </div>
                    </div>
                    <div class="form-group" style="margin-top: 15px;">
                        <label for="investlevel" style="font-weight: 600; font-size: 13px; color: #4B5563;">Nivel de interés en inversión</label>
                        <select id="investlevel" name="INVESTLVL" style="border-radius: 6px; border: 1px solid #D1D5DB; padding: 12px; width: 100%; font-size: 15px; background: #fff;">
                            <option value="" disabled selected>Selecciona tu nivel</option>
                            <option value="Principiante">Principiante (quiero aprender a empezar)</option>
                            <option value="Intermedio">Intermedio (ya invierto pero quiero mejorar)</option>
                            <option value="Avanzado">Avanzado (busco nuevas oportunidades)</option>
                        </select>
                    </div>
                </div>

                <!-- Subscription Checkbox -->
                <div class="checkbox-group" style="margin-top: 25px; background: #F3F4F6; padding: 15px; border-radius: 6px;">
                    <label style="display: flex; align-items: flex-start; gap: 12px; cursor: pointer; font-size: 13px; font-weight: 500; color: #4B5563; line-height: 1.4;">
                        <input type="checkbox" id="chk_subscription" name="NEWSLETTER" value="Yes" checked style="margin-top: 2px; width: 18px; height: 18px; accent-color: #A03FA3; flex-shrink: 0;">
                        <span>Quiero recibir novedades, contenido y oportunidades de Castle</span>
                    </label>
                </div>

                <!-- Form message container -->
                <div id="form_message" style="display: none; margin-top: 15px; padding: 15px; border-radius: 6px; font-weight: 500; text-align: center; font-size: 14px;"></div>

                <button type="submit" id="submit_btn" style="width: 100%; background-color: #A03FA3; color: #FFFFFF; font-weight: 800; letter-spacing: 1.5px; padding: 16px; border-radius: 50px; border: none; font-size: 15px; cursor: pointer; transition: background 0.2s, transform 0.2s; box-shadow: 0 10px 20px rgba(160,63,163,0.3); font-family: 'Inter Tight', sans-serif; text-transform: uppercase; margin-top: 25px;">APLICAR AHORA</button>
            </form>
        </div>
    </div>"""

    content = content[:modal_start] + new_modal + content[last_div:]

    # JS Code
    js_start = content.find('<script>\n        function updateDynamicFields() {')
    if js_start == -1:
        js_start = content.find('<script>\n        function openUnifiedModal(sourceType) {')
    
    if js_start != -1:
        js_end = content.find('</script>', js_start) + 9
        content = content[:js_start] + content[js_end:] # remove old script

    new_js = """
    <script>
        function updateDynamicFields() {
            const isContact = document.getElementById('chk_contact').checked;
            const isPartner = document.getElementById('chk_partner').checked;
            const isMasterclass = document.getElementById('chk_masterclass').checked;
            const isWaitlist = document.getElementById('chk_waitlist').checked;
            
            document.getElementById('dyn_contact').style.display = isContact ? 'block' : 'none';
            document.getElementById('dyn_partner').style.display = isPartner ? 'block' : 'none';
            document.getElementById('dyn_invest').style.display = (isMasterclass || isWaitlist) ? 'block' : 'none';
            
            // Toggle required attributes
            document.getElementById('message').required = isContact;
            document.getElementById('partnertype').required = isPartner;
        }

        // Setup listeners
        document.addEventListener("DOMContentLoaded", function() {
            if(document.getElementById('chk_contact')) document.getElementById('chk_contact').addEventListener('change', updateDynamicFields);
            if(document.getElementById('chk_partner')) document.getElementById('chk_partner').addEventListener('change', updateDynamicFields);
            if(document.getElementById('chk_masterclass')) document.getElementById('chk_masterclass').addEventListener('change', updateDynamicFields);
            if(document.getElementById('chk_waitlist')) document.getElementById('chk_waitlist').addEventListener('change', updateDynamicFields);
        });
        
        let isOpening = false;
        function openUnifiedModal(sourceType) {
            if(isOpening) return;
            isOpening = true;
            
            if(document.getElementById('waitlistModal')) {
                document.getElementById('waitlistModal').style.display = 'flex';
                document.getElementById('form_message').style.display = 'none';
            }
            
            // Uncheck all main interests first
            if(document.getElementById('chk_waitlist')) document.getElementById('chk_waitlist').checked = false;
            if(document.getElementById('chk_masterclass')) document.getElementById('chk_masterclass').checked = false;
            if(document.getElementById('chk_partner')) document.getElementById('chk_partner').checked = false;
            if(document.getElementById('chk_contact')) document.getElementById('chk_contact').checked = false;
            if(document.getElementById('chk_newsletter')) document.getElementById('chk_newsletter').checked = false;
            
            // Always keep newsletter subscription checked by default
            if(document.getElementById('chk_subscription')) document.getElementById('chk_subscription').checked = true;

            // Check based on source
            if (sourceType === 'waitlist') {
                if(document.getElementById('chk_waitlist')) document.getElementById('chk_waitlist').checked = true;
            } else if (sourceType === 'masterclass') {
                if(document.getElementById('chk_masterclass')) document.getElementById('chk_masterclass').checked = true;
            } else if (sourceType === 'partner') {
                if(document.getElementById('chk_partner')) document.getElementById('chk_partner').checked = true;
            } else if (sourceType === 'contact') {
                if(document.getElementById('chk_contact')) document.getElementById('chk_contact').checked = true;
            } else if (sourceType === 'newsletter') {
                if(document.getElementById('chk_newsletter')) document.getElementById('chk_newsletter').checked = true;
            }

            updateDynamicFields();
            isOpening = false;
        }

        function submitMailchimpJSONP(form) {
            const btn = document.getElementById('submit_btn');
            btn.innerText = 'ENVIANDO...';
            btn.disabled = true;
            
            // Collect interests
            let interests = [];
            if (document.getElementById('chk_masterclass') && document.getElementById('chk_masterclass').checked) interests.push("Masterclass");
            if (document.getElementById('chk_waitlist') && document.getElementById('chk_waitlist').checked) interests.push("Waitlist");
            if (document.getElementById('chk_partner') && document.getElementById('chk_partner').checked) interests.push("Partner");
            if (document.getElementById('chk_contact') && document.getElementById('chk_contact').checked) interests.push("Contact");
            if (document.getElementById('chk_newsletter') && document.getElementById('chk_newsletter').checked) interests.push("Newsletter");
            
            if (interests.length === 0) {
                interests.push("No specific interest");
            }

            document.getElementById('unifiedSource').value = interests.join(", ");

            const params = new URLSearchParams();
            const formData = new FormData(form);
            for (const [key, value] of formData.entries()) {
                params.append(key, value);
            }
            // Append concatenated phone
            const phoneCode = document.getElementById('phone_code').value;
            const phoneNum = document.getElementById('phone_num').value;
            params.append('PHONE', phoneCode + ' ' + phoneNum);
            
            // Add honeypot
            params.append('b_4766d7bd8debcf610dadddfb6_53677e9563', '');
            
            // JSONP callback
            const callbackName = 'mcCallback' + Math.round(100000 * Math.random());
            params.append('c', callbackName);
            
            const url = "https://buildyourcastle.us10.list-manage.com/subscribe/post-json?u=4766d7bd8debcf610dadddfb6&id=53677e9563&" + params.toString();
            
            window[callbackName] = function(data) {
                btn.innerText = 'APLICAR AHORA';
                btn.disabled = false;
                const msgDiv = document.getElementById('form_message');
                msgDiv.style.display = 'block';
                if (data.result === 'success') {
                    msgDiv.style.backgroundColor = '#D1FAE5';
                    msgDiv.style.color = '#065F46';
                    msgDiv.innerHTML = '¡Gracias! Hemos recibido tus datos correctamente.';
                    form.reset();
                    updateDynamicFields();
                    setTimeout(() => { 
                        if(document.getElementById('waitlistModal')) document.getElementById('waitlistModal').style.display='none'; 
                        msgDiv.style.display='none'; 
                    }, 4000);
                } else {
                    msgDiv.style.backgroundColor = '#FEE2E2';
                    msgDiv.style.color = '#991B1B';
                    msgDiv.innerHTML = 'Hubo un error: ' + data.msg;
                }
                delete window[callbackName];
                document.body.removeChild(script);
            };
            
            const script = document.createElement('script');
            script.src = url;
            document.body.appendChild(script);
        }
    </script>
    """
    
    # Insert new js before </body>
    if '</body>' in content:
        content = content.replace('</body>', new_js + '\n</body>')
    else:
        content += new_js

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Processed {filename}")

for file in glob.glob("*_es.html"):
    if file == 'index_es_backup_13may.html': continue
    process_file(file)
