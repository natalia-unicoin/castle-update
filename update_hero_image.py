import re

files = [
    "/Users/Nati/.gemini/antigravity/scratch/Castle_V3_Standalone/masterclass.html",
    "/Users/Nati/.gemini/antigravity/scratch/Castle_V3_Standalone/masterclass_es.html"
]

old_placeholder_regex = r'<div class="image-placeholder" style="background-color: #E5E7EB; border-radius: 5px; aspect-ratio: 4/3; width: 100%;">\s*<span style="color: #9CA3AF;">\[Hero Image / Video\]</span>\s*</div>'

new_image_block = """<div style="border-radius: 5px; aspect-ratio: 16/9; width: 100%; background: url('./public/images/common/masterclass-hero.png') center/cover no-repeat; box-shadow: 0 20px 50px rgba(0,0,0,0.3);">
            </div>"""

for filepath in files:
    with open(filepath, "r") as f:
        content = f.read()

    if re.search(old_placeholder_regex, content):
        content = re.sub(old_placeholder_regex, new_image_block, content)
        with open(filepath, "w") as f:
            f.write(content)
        print(f"Updated hero image in {filepath}")
    else:
        print(f"Placeholder not found in {filepath}")
