with open('inject_dynamic_form_es.py', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Swap dyn_contact and dyn_b2b
dyn_contact = """                <!-- Contact Message -->
                <div class="form-group" id="dyn_contact" style="display: none; margin-top: 12px;">
                    <label for="message" style="font-weight: 600; font-size: 13px; color: #4B5563;">Mensaje</label>
                    <textarea id="message" name="MESSAGE" rows="3" placeholder="¿En qué te podemos ayudar?" style="border-radius: 6px; border: 1px solid #D1D5DB; padding: 12px; width: 100%; font-size: 15px; font-family: inherit; resize: vertical;"></textarea>
                </div>"""

dyn_b2b = """                <!-- B2B Fields -->
                <div class="form-row" id="dyn_b2b" style="display: none; margin-top: 12px;">
                    <div class="form-group">
                        <label for="company" style="font-weight: 600; font-size: 13px; color: #4B5563;">Empresa</label>
                        <input type="text" id="company" name="COMPANY" placeholder="Ej. Acme Corp" style="border-radius: 6px; border: 1px solid #D1D5DB; padding: 12px; width: 100%; font-size: 15px;">
                    </div>
                    <div class="form-group">
                        <label for="role" style="font-weight: 600; font-size: 13px; color: #4B5563;">Profesión / Cargo</label>
                        <input type="text" id="role" name="ROLE" placeholder="Ej. Médico / CEO" style="border-radius: 6px; border: 1px solid #D1D5DB; padding: 12px; width: 100%; font-size: 15px;">
                    </div>
                </div>"""

# Remove both blocks first
content = content.replace(dyn_contact, '')
content = content.replace(dyn_b2b, '')

# Add them back in the new order (B2B first, then Contact) right after <!-- DYNAMIC FIELDS -->
target = "                <!-- DYNAMIC FIELDS -->"
new_blocks = f"{target}\n\n{dyn_b2b}\n\n{dyn_contact}"
content = content.replace(target, new_blocks)

# 2. Compress spacing
content = content.replace('margin-top: 12px;', 'margin-top: 10px;')
content = content.replace('margin-bottom: 15px; background: #F9FAFB;', 'margin-bottom: 10px; background: #F9FAFB;')
content = content.replace('margin-top: 15px; background: #F3F4F6;', 'margin-top: 10px; background: #F3F4F6;')
content = content.replace('padding: 20px; border-radius: 8px;', 'padding: 15px; border-radius: 8px;') # Checkbox container padding
content = content.replace('gap: 10px;">', 'gap: 8px;">') # Checkbox row gaps
content = content.replace('padding: 15px; border-radius: 6px;">', 'padding: 12px; border-radius: 6px;">') # Subscription container padding
content = content.replace('padding: 16px;', 'padding: 14px;') # Submit button padding

with open('inject_dynamic_form_es.py', 'w', encoding='utf-8') as f:
    f.write(content)
