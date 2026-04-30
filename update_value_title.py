import re

files = [
    "/Users/Nati/.gemini/antigravity/scratch/Castle_V3_Standalone/masterclass.html",
    "/Users/Nati/.gemini/antigravity/scratch/Castle_V3_Standalone/masterclass_es.html"
]

def update_value_title(filepath, is_es):
    with open(filepath, "r") as f:
        content = f.read()

    # Update Section 4 padding
    # Currently: padding: 120px 4vw;
    # Change to: padding: 40px 4vw 120px 4vw;
    # This reduces the top margin/padding after the big image.
    if '<section class="snap-section" style="background-color: #FFFFFF; padding: 120px 4vw;">' in content:
        content = content.replace(
            '<section class="snap-section" style="background-color: #FFFFFF; padding: 120px 4vw;">',
            '<section class="snap-section" style="background-color: #FFFFFF; padding: 40px 4vw 120px 4vw;">'
        )

    # Update Title
    if is_es:
        old_title = "Dentro de la Masterclass de Castle vas a:"
        new_title = "Dentro de las sesiones Masterclass de Castle vas a:"
    else:
        old_title = "Inside the Castle Masterclass you will:"
        new_title = "Inside the Castle Masterclass sessions you will:"

    if old_title in content:
        content = content.replace(old_title, new_title)

    with open(filepath, "w") as f:
        f.write(content)
    print(f"Updated Value section in {filepath}")

update_value_title(files[0], False)
update_value_title(files[1], True)
