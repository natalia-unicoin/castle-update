import glob

def fix_file(filename):
    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()
    
    changed = False
    
    replacements = {
        '>Enviar Solicitud</button>': '>Enviar</button>',
        '>Submit Application</button>': '>Submit</button>'
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
