import glob

def fix_file(filename):
    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()
    
    old_label = '.form-group label { font-size: 14px; font-weight: 600; color: #1A1A1A; margin-bottom: 8px; text-align: left; margin-left: 2px; }'
    new_label = '.form-group label { font-size: 14px; font-weight: 600; color: #1A1A1A; margin-bottom: 8px; text-align: left !important; margin-left: 0 !important; padding-left: 0 !important; align-self: flex-start; }'
    
    if old_label in content:
        content = content.replace(old_label, new_label)
        with open(filename, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Fixed {filename}")

for file in glob.glob("*.html"):
    fix_file(file)
