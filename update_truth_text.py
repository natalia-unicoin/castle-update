import re
import time

files = [
    "/Users/Nati/.gemini/antigravity/scratch/Castle_V3_Standalone/masterclass.html",
    "/Users/Nati/.gemini/antigravity/scratch/Castle_V3_Standalone/masterclass_es.html"
]

for filepath in files:
    with open(filepath, "r") as f:
        content = f.read()

    # Shrink the H2 text
    # Original: font-size: clamp(36px, 5vw, 64px);
    content = content.replace('font-size: clamp(36px, 5vw, 64px);', 'font-size: clamp(28px, 4vw, 52px);')

    # Change small text color from rgba(255,255,255,0.8) to Ghost White (#F8F8FF)
    # Original: color: rgba(255,255,255,0.8);
    # There might be multiple instances (like in final CTA), so let's be careful.
    # The exact string in the Truth section:
    if filepath.endswith("_es.html"):
        content = content.replace('color: rgba(255,255,255,0.8);">Porque la verdad es simple:</p>', 'color: #F8F8FF;">Porque la verdad es simple:</p>')
    else:
        content = content.replace('color: rgba(255,255,255,0.8);">Because the truth is simple:</p>', 'color: #F8F8FF;">Because the truth is simple:</p>')

    # Bust cache just in case
    v = str(int(time.time()))
    content = re.sub(r'masterclass-finalcta\.jpg(?:\?v=\d+)?', f'masterclass-finalcta.jpg?v={v}', content)

    with open(filepath, "w") as f:
        f.write(content)

print("Updated Truth section text size and color")
