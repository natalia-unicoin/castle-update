import glob

def fix_file(filename):
    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()
    
    old_div = '<div style="display: flex; flex-direction: column; gap: 12px;">'
    new_div = '''<style>
                        .interests-grid { display: grid; gap: 12px; grid-template-columns: 1fr; }
                        @media(min-width: 600px) { .interests-grid { grid-template-columns: 1fr 1fr; } }
                    </style>
                    <div class="interests-grid">'''
                    
    if old_div in content:
        content = content.replace(old_div, new_div)
        with open(filename, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Fixed {filename}")

for file in glob.glob("*.html"):
    fix_file(file)
