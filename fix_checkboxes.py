import glob
import os

def fix_file(filename):
    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()
    
    changed = False
    
    # Spanish replacement
    if "_es.html" in filename or filename == "gracias.html":
        replacements = {
            'Estoy interesada en (selecciona todas las opciones que correspondan):</label>': '¿Qué te gustaría hacer en Castle?<br><span style="font-size: 13px; font-weight: 400; color: #4B5563; margin-top: 4px; display: inline-block;">(puedes seleccionar más de una opción)</span></label>',
            '> Unirme a la lista de espera (Masterclass/App)</label>': '> Quiero acceso anticipado a Castle (Masterclass / App)</label>',
            '> Asociarme con Castle</label>': '> Quiero colaborar con Castle</label>',
            '> Contacto General</label>': '> Quiero hablar con el equipo</label>',
            '> Suscribirme al Newsletter</label>': '> Quiero recibir novedades y contenido</label>'
        }
    else:
        # English replacement
        replacements = {
            'I am interested in (select all that apply):</label>': 'What would you like to do at Castle?<br><span style="font-size: 13px; font-weight: 400; color: #4B5563; margin-top: 4px; display: inline-block;">(you can select more than one option)</span></label>',
            '> Join the Waitlist (Masterclass/App)</label>': '> I want early access to Castle (Masterclass / App)</label>',
            '> Partnering with Castle</label>': '> I want to collaborate with Castle</label>',
            '> General Contact</label>': '> I want to connect with the team</label>',
            '> Subscribe to Newsletter</label>': '> I want to receive updates and content</label>'
        }
        
    for old_text, new_text in replacements.items():
        if old_text in content:
            content = content.replace(old_text, new_text)
            changed = True
            
    if changed:
        with open(filename, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Fixed {filename}")

for file in glob.glob("*.html"):
    fix_file(file)
