import re

files = [
    "/Users/Nati/.gemini/antigravity/scratch/Castle_V3_Standalone/masterclass.html",
    "/Users/Nati/.gemini/antigravity/scratch/Castle_V3_Standalone/masterclass_es.html"
]

for filepath in files:
    with open(filepath, "r") as f:
        content = f.read()

    # 1. Update Hook Image
    old_hook = r'<div class="image-placeholder" style="background-color: #E5E7EB; border-radius: 5px; aspect-ratio: 3/4; width: 100%;">\s*<span style="color: #9CA3AF;">\[Hook Image\]</span>\s*</div>'
    new_hook = """<div style="border-radius: 5px; aspect-ratio: 3/4; width: 100%; background: url('./public/images/common/masterclass-hook.jpg') center/cover no-repeat; box-shadow: 0 20px 40px rgba(0,0,0,0.1);"></div>"""
    content = re.sub(old_hook, new_hook, content)

    # 2. Update Myths section (Section 3)
    # The black text H2:
    content = content.replace('font-size: clamp(40px, 6vw, 70px);', 'font-size: clamp(28px, 4vw, 42px);')
    
    # The colored text:
    old_colored = 'font-size: clamp(30px, 4vw, 48px); font-weight: 900; color: #A03FA3; letter-spacing: -1px;'
    new_colored = 'font-family: \\\'Caveat\\\', cursive; font-size: clamp(60px, 8vw, 90px); font-weight: 700; color: #A03FA3; line-height: 1; margin-top: 20px;'
    content = content.replace(old_colored, new_colored)

    # Also, in Section 2, there is colored text. She might want that Caveat too. Let's make "Was keeping you small?" and "te estuviera limitando?" caveat too.
    # In masterclass.html: <span style="color: #A03FA3;">Was keeping you small?</span>
    content = content.replace('<span style="color: #A03FA3;">Was keeping you small?</span>', 
                              '<span style="color: #A03FA3; font-family: \'Caveat\', cursive; font-size: clamp(48px, 6vw, 72px); font-weight: 700; display: block; margin-top: 10px;">Was keeping you small?</span>')
    content = content.replace('<span style="color: #A03FA3;">te estuviera limitando?</span>', 
                              '<span style="color: #A03FA3; font-family: \'Caveat\', cursive; font-size: clamp(48px, 6vw, 72px); font-weight: 700; display: block; margin-top: 10px;">te estuviera limitando?</span>')


    with open(filepath, "w") as f:
        f.write(content)
    
    print(f"Updated {filepath}")
