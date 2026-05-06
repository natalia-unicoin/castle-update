import glob

def fix_file(filename):
    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()
    
    changed = False
    
    replacements = {
        '> Quiero acceso anticipado a Castle (Masterclass)</label>': '> Quiero acceso anticipado a Castle</label>',
        '> Quiero recibir novedades y contenido</label>': '> Quiero recibir novedades</label>',
        '> I want early access to Castle (Masterclass)</label>': '> I want early access to Castle</label>',
        '> I want to receive updates and content</label>': '> I want to receive updates</label>'
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
