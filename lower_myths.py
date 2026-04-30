import re

files = [
    "/Users/Nati/.gemini/antigravity/scratch/Castle_V3_Standalone/masterclass.html",
    "/Users/Nati/.gemini/antigravity/scratch/Castle_V3_Standalone/masterclass_es.html"
]

for filepath in files:
    with open(filepath, "r") as f:
        content = f.read()

    # Lower the text in Myths section by reducing bottom padding from 80px to 50px
    content = content.replace('padding: 0 4vw 80px 4vw;', 'padding: 0 4vw 50px 4vw;')

    with open(filepath, "w") as f:
        f.write(content)

print("Lowered Myths text by 30px")
