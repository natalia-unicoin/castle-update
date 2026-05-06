import glob

def fix_file(filename):
    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Spanish replacement
    if "_es.html" in filename or filename == "gracias.html":
        old_title = 'Únete al Movimiento Castle'
        new_title = 'Bienvenida a Castle'
        old_sub = 'Toma el control de tu futuro financiero. Únete a la revolución de riqueza liderada por Mujeres.'
        new_sub = 'Toma el control de tu futuro financiero y empieza a construir tu propia riqueza.'
    # English replacement
    else:
        old_title = 'Join the Castle Movement'
        new_title = 'Welcome to Castle'
        old_sub = 'Take control of your financial future. Join the Women-led Wealth revolution.'
        new_sub = 'Take control of your financial future and start building your own wealth.'
        
    changed = False
    if old_title in content:
        content = content.replace(old_title, new_title)
        changed = True
    if old_sub in content:
        content = content.replace(old_sub, new_sub)
        changed = True
        
    if changed:
        with open(filename, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Fixed {filename}")

for file in glob.glob("*.html"):
    fix_file(file)
