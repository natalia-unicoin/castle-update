import re

files = [
    "/Users/Nati/.gemini/antigravity/scratch/Castle_V3_Standalone/masterclass.html",
    "/Users/Nati/.gemini/antigravity/scratch/Castle_V3_Standalone/masterclass_es.html"
]

def fix_caveat_color(filepath):
    with open(filepath, "r") as f:
        content = f.read()

    # The caveat text in the myths section has color: #EABFFF
    # Replace with #A03FA3
    if "#EABFFF" in content:
        content = content.replace("#EABFFF", "#A03FA3")

    with open(filepath, "w") as f:
        f.write(content)
    print(f"Fixed Caveat color in {filepath}")

fix_caveat_color(files[0])
fix_caveat_color(files[1])
