import glob

def fix_file(filename):
    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()
    
    changed = False
    
    old_style = 'style="margin-top: 10px; margin-bottom: 10px; text-align: center; font-size: clamp(32px, 4vw, 42px);"'
    new_style = 'style="margin-top: 10px; margin-bottom: 10px; text-align: center; font-size: clamp(22px, 6vw, 42px); white-space: nowrap;"'
    
    if old_style in content:
        content = content.replace(old_style, new_style)
        changed = True
            
    if changed:
        with open(filename, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Fixed {filename}")

for file in glob.glob("*.html"):
    fix_file(file)
