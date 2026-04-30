import re

files = [
    "/Users/Nati/.gemini/antigravity/scratch/Castle_V3_Standalone/masterclass.html",
    "/Users/Nati/.gemini/antigravity/scratch/Castle_V3_Standalone/masterclass_es.html"
]

for filepath in files:
    with open(filepath, "r") as f:
        content = f.read()

    # Revert Section 2 Caveat back to Inter
    if "te estuviera limitando?" in content:
        content = content.replace('<span style="color: #A03FA3; font-family: \'Caveat\', cursive; font-size: clamp(48px, 6vw, 72px); font-weight: 700; display: block; margin-top: 10px;">te estuviera limitando?</span>', 
                                  '<span style="color: #A03FA3;">te estuviera limitando?</span>')
    if "Was keeping you small?" in content:
        content = content.replace('<span style="color: #A03FA3; font-family: \'Caveat\', cursive; font-size: clamp(48px, 6vw, 72px); font-weight: 700; display: block; margin-top: 10px;">Was keeping you small?</span>', 
                                  '<span style="color: #A03FA3;">Was keeping you small?</span>')

    # Increase Section 3 Black text slightly
    # From clamp(28px, 4vw, 42px) to clamp(36px, 5vw, 56px)
    content = content.replace('font-size: clamp(28px, 4vw, 42px);', 'font-size: clamp(36px, 5vw, 56px);')

    with open(filepath, "w") as f:
        f.write(content)
    
    print(f"Updated {filepath}")
