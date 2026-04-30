import re
import time

files = [
    "/Users/Nati/.gemini/antigravity/scratch/Castle_V3_Standalone/masterclass.html",
    "/Users/Nati/.gemini/antigravity/scratch/Castle_V3_Standalone/masterclass_es.html"
]

v = str(int(time.time())) # unique timestamp for robust cache busting

for filepath in files:
    with open(filepath, "r") as f:
        content = f.read()

    # Replace masterclass-myths-bg.jpg optionally followed by ?v=...
    content = re.sub(r'masterclass-myths-bg\.jpg(?:\?v=\d+)?', f'masterclass-myths-bg.jpg?v={v}', content)
    
    # Replace masterclass-hook.jpg optionally followed by ?v=...
    content = re.sub(r'masterclass-hook\.jpg(?:\?v=\d+)?', f'masterclass-hook.jpg?v={v}', content)

    # Also the hero just in case
    content = re.sub(r'masterclass-hero\.png(?:\?v=\d+)?', f'masterclass-hero.png?v={v}', content)

    with open(filepath, "w") as f:
        f.write(content)
        
print(f"Added cache busting ?v={v} to all masterclass images.")
