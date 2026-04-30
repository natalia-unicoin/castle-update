import re
import time

files = [
    "/Users/Nati/.gemini/antigravity/scratch/Castle_V3_Standalone/masterclass.html",
    "/Users/Nati/.gemini/antigravity/scratch/Castle_V3_Standalone/masterclass_es.html"
]

for filepath in files:
    with open(filepath, "r") as f:
        content = f.read()

    # Increase container max-width in Final CTA from 800px to 1000px
    # In my previous script I used: <div class="container" style="position: relative; z-index: 2; width: 100%; max-width: 800px; margin: 0 auto; display: flex; flex-direction: column; align-items: center;">
    content = content.replace('max-width: 800px;', 'max-width: 1000px;')

    # Bust cache again just in case
    v = str(int(time.time()))
    content = re.sub(r'masterclass-finalcta\.jpg(?:\?v=\d+)?', f'masterclass-finalcta.jpg?v={v}', content)

    with open(filepath, "w") as f:
        f.write(content)

print("Updated Final CTA container width to 1000px")
