import re
import time

files = [
    "/Users/Nati/.gemini/antigravity/scratch/Castle_V3_Standalone/masterclass.html",
    "/Users/Nati/.gemini/antigravity/scratch/Castle_V3_Standalone/masterclass_es.html"
]

for filepath in files:
    with open(filepath, "r") as f:
        content = f.read()

    # Change section 4 bottom padding from 120px to 40px
    content = content.replace('padding: 40px 4vw 120px 4vw;', 'padding: 40px 4vw 40px 4vw;')

    # Center the text inside the boxes
    content = content.replace('text-align: left;', 'text-align: center;')

    # Change the Caveat title color from #A03FA3 to #FFFFFF
    content = content.replace('color: #A03FA3; margin-bottom: 5px; line-height: 1;', 'color: #FFFFFF; margin-bottom: 5px; line-height: 1;')

    # Bust cache just in case
    v = str(int(time.time()))
    content = re.sub(r'masterclass-myths-bg\.jpg(?:\?v=\d+)?', f'masterclass-myths-bg.jpg?v={v}', content)

    with open(filepath, "w") as f:
        f.write(content)
        
print("Updated grid styling: white caveat titles, centered text, 40px bottom margin.")
