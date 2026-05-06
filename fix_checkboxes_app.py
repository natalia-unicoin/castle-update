import glob
import os

def fix_file(filename):
    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()
    
    changed = False
    
    # Spanish replacement
    if "_es.html" in filename or filename == "gracias.html":
        replacements = {
            '> Quiero acceso anticipado a Castle (Masterclass / App)</label>': '> Quiero acceso anticipado a Castle (Masterclass)</label>'
        }
    else:
        # English replacement
        replacements = {
            '> I want early access to Castle (Masterclass / App)</label>': '> I want early access to Castle (Masterclass)</label>'
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
