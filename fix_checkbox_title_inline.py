import glob

def fix_file(filename):
    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()
    
    changed = False
    
    replacements = {
        '¿Qué te gustaría hacer en Castle?<br><span style="font-size: 13px; font-weight: 400; color: #4B5563; margin-top: 4px; display: inline-block;">(puedes seleccionar más de una opción)</span>': '¿Qué te gustaría hacer en Castle? <span style="font-size: 13px; font-weight: 400; color: #4B5563; margin-left: 6px;">(puedes seleccionar más de una opción)</span>',
        'What would you like to do at Castle?<br><span style="font-size: 13px; font-weight: 400; color: #4B5563; margin-top: 4px; display: inline-block;">(you can select more than one option)</span>': 'What would you like to do at Castle? <span style="font-size: 13px; font-weight: 400; color: #4B5563; margin-left: 6px;">(you can select more than one option)</span>'
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
