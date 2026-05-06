import glob

def fix_file(filename):
    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()
    
    changed = False
    
    # The actual string is:
    # <div class="form-group" style="margin-bottom: 20px; background: #F9FAFB; padding: 20px; border-radius: 6px; border: 1px solid #D1D5DB;">
    
    old_style = '<div class="form-group" style="margin-bottom: 20px; background: #F9FAFB; padding: 20px; border-radius: 6px; border: 1px solid #D1D5DB;">'
    new_style = '<div class="form-group" style="margin-bottom: 20px;">'
    
    if old_style in content:
        content = content.replace(old_style, new_style)
        changed = True

    if changed:
        with open(filename, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Fixed {filename}")

for file in glob.glob("*.html"):
    fix_file(file)
