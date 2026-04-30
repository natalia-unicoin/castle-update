import re

files = [
    "/Users/Nati/.gemini/antigravity/scratch/Castle_V3_Standalone/masterclass.html",
    "/Users/Nati/.gemini/antigravity/scratch/Castle_V3_Standalone/masterclass_es.html"
]

for filepath in files:
    with open(filepath, "r") as f:
        content = f.read()

    # Extract sections
    hero_match = re.search(r'(<!-- 1\. Hero Section -->.*?</section>)', content, re.DOTALL)
    hook_match = re.search(r'\s*(<!-- 2\. The Hook -->.*?</section>)', content, re.DOTALL)
    myths_match = re.search(r'(<!-- 3\. The Myths -->.*?</section>)', content, re.DOTALL)
    value_match = re.search(r'\s*(<!-- 4\. The Value -->.*?</section>)', content, re.DOTALL)

    if hero_match and hook_match and myths_match and value_match:
        hero_str = hero_match.group(1)
        hook_str = hook_match.group(1)
        value_str = value_match.group(1)

        # 1. Remove The Hook
        content = content.replace(hook_match.group(0), '')
        
        # 2. Remove The Value from its current position
        content = content.replace(value_match.group(0), '')
        
        # 3. Insert The Value right after Hero
        # But wait, Hero is followed by the rest. We can just replace hero_str with hero_str + "\n\n    " + value_str
        content = content.replace(hero_str, hero_str + "\n\n" + value_str)

        with open(filepath, "w") as f:
            f.write(content)
        print(f"Reordered {filepath}")
    else:
        print(f"Could not find sections in {filepath}")
