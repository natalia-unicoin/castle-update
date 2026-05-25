import re

block_to_add = """
                <div style="display: flex; align-items: center; justify-content: center; gap: 12px; margin-top: 40px; font-family: 'Inter', sans-serif; font-size: 14px; color: rgba(255,255,255,0.8); font-weight: 600; letter-spacing: 1px;">
                    Powered by <img src="./public/images/common/fundacion-light.png" alt="Unicoin Foundation" style="height: 28px; object-fit: contain; opacity: 0.9;">
                </div>"""

def process_file(filename, p_text):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # We find the specific <p> tag by matching its content
    pattern = r'(<p style="color: rgba\(255,255,255,0\.95\); font-size: clamp\(18px, 2\.5vw, 24px\); line-height: 1\.6; margin-bottom: 0; font-weight: 500;">.*?'+p_text+r'.*?</p>)'
    
    new_content = re.sub(pattern, r'\1' + block_to_add, content, flags=re.DOTALL)
    
    if new_content != content:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Added 'Powered by' to {filename}")
    else:
        print(f"Failed to find match in {filename}")

process_file('masterclass_v2.html', 'A 4-Day Immersive Experience')
process_file('masterclass_v2_es.html', 'Una experiencia inmersiva')

