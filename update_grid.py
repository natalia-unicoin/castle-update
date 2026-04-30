import re
import time

files = [
    "/Users/Nati/.gemini/antigravity/scratch/Castle_V3_Standalone/masterclass.html",
    "/Users/Nati/.gemini/antigravity/scratch/Castle_V3_Standalone/masterclass_es.html"
]

def generate_grid_html(is_es):
    if is_es:
        boxes = [
            ("Reprogramar", "tu mentalidad sobre el dinero y la abundancia.", "[Image 1]"),
            ("Construir", "una confianza financiera inquebrantable.", "[Image 2]"),
            ("Aprender", "a identificar y actuar sobre oportunidades.", "[Image 3]"),
            ("Convertirte", "en la versión financiera poderosa que mereces ser.", "[Image 4]"),
        ]
    else:
        boxes = [
            ("Reprogram", "your mindset around money and abundance.", "[Image 1]"),
            ("Build", "unshakeable financial confidence.", "[Image 2]"),
            ("Learn", "to identify and act on opportunities.", "[Image 3]"),
            ("Become", "the powerful financial version you deserve to be.", "[Image 4]"),
        ]

    html = '<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 10px; margin-bottom: 0;">\n'
    for caveat, text, img_txt in boxes:
        html += f'''                <div style="aspect-ratio: 3/4; position: relative; border-radius: 5px; overflow: hidden; background-color: #E5E7EB; display: flex; flex-direction: column; justify-content: flex-end; padding: 30px 20px; transition: transform 0.3s;">
                    <div style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; background: linear-gradient(to bottom, rgba(0,0,0,0) 0%, rgba(0,0,0,0.85) 100%); z-index: 1;"></div>
                    <div style="position: relative; z-index: 2; text-align: left;">
                        <div style="font-family: 'Caveat', cursive; font-size: clamp(36px, 4vw, 42px); color: #A03FA3; margin-bottom: 5px; line-height: 1;">{caveat}</div>
                        <p style="color: #FFFFFF; font-size: 16px; font-weight: 500; line-height: 1.4; margin-bottom: 0;">{text}</p>
                    </div>
                    <div style="position: absolute; bottom: 10px; left: 10px; z-index: 1; color: rgba(255,255,255,0.4); font-size: 12px;">{img_txt}</div>
                </div>\n'''
    html += '            </div>'
    return html

for filepath in files:
    is_es = filepath.endswith("_es.html")
    with open(filepath, "r") as f:
        content = f.read()

    # Regex to find the entire grid section
    regex = r'<div style="display: grid; grid-template-columns: repeat\(auto-fit, minmax\(240px, 1fr\)\); gap: 10px; margin-bottom: 0;">.*?</div>\n\s*</div>\n\s*</section>'
    
    new_grid = generate_grid_html(is_es)
    
    # We replace up to the end of the section just to be safe with the regex
    replacement = new_grid + '\n        </div>\n    </section>'
    
    if re.search(regex, content, re.DOTALL):
        content = re.sub(regex, replacement, content, flags=re.DOTALL)
    
    # Cache bust Myths image
    v = str(int(time.time()))
    content = re.sub(r'masterclass-myths-bg\.jpg(?:\?v=\d+)?', f'masterclass-myths-bg.jpg?v={v}', content)

    with open(filepath, "w") as f:
        f.write(content)
    print(f"Updated grid and cache bust in {filepath}")
