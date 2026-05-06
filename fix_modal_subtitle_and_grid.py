import glob

def fix_file(filename):
    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()
    
    changed = False
    
    # 1. Remove ES Subtitle
    es_subtitle = '<p style="text-align: center; color: #2A2A2A; font-family: \'Inter\', sans-serif; margin-bottom: var(--spacer-30); line-height: 1.5;">Toma el control de tu futuro financiero y empieza a construir tu propia riqueza.</p>'
    if es_subtitle in content:
        content = content.replace(es_subtitle, '')
        changed = True

    # 2. Remove EN Subtitle
    en_subtitle = '<p style="text-align: center; color: #2A2A2A; font-family: \'Inter\', sans-serif; margin-bottom: var(--spacer-30); line-height: 1.5;">Take control of your financial future and start building your own wealth.</p>'
    if en_subtitle in content:
        content = content.replace(en_subtitle, '')
        changed = True

    # 3. Change to 1 column
    old_style_block = """                    <style>
                        .interests-grid { display: grid; gap: 12px; grid-template-columns: 1fr; }
                        @media(min-width: 600px) { .interests-grid { grid-template-columns: 1fr 1fr; } }
                    </style>"""
    new_style_block = """                    <style>
                        .interests-grid { display: grid; gap: 12px; grid-template-columns: 1fr; }
                    </style>"""
                    
    if old_style_block in content:
        content = content.replace(old_style_block, new_style_block)
        changed = True

    if changed:
        with open(filename, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Fixed {filename}")

for file in glob.glob("*.html"):
    fix_file(file)
