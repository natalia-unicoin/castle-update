import re

files = [
    "/Users/Nati/.gemini/antigravity/scratch/Castle_V3_Standalone/masterclass.html",
    "/Users/Nati/.gemini/antigravity/scratch/Castle_V3_Standalone/masterclass_es.html"
]

for filepath in files:
    with open(filepath, "r") as f:
        content = f.read()

    # Find the Truth section using regex and delete it
    regex = r'\s*<!-- 5\. The Truth -->\s*<section class="snap-section".*?</section>'
    
    if re.search(regex, content, re.DOTALL):
        content = re.sub(regex, '', content, flags=re.DOTALL)
        with open(filepath, "w") as f:
            f.write(content)
        print(f"Deleted Truth section in {filepath}")
    else:
        print(f"Could not find Truth section in {filepath}")
