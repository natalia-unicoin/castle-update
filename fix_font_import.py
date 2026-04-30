import re

files = [
    "/Users/Nati/.gemini/antigravity/scratch/Castle_V3_Standalone/masterclass.html",
    "/Users/Nati/.gemini/antigravity/scratch/Castle_V3_Standalone/masterclass_es.html"
]

def fix_imports(filepath):
    with open(filepath, "r") as f:
        content = f.read()

    # The existing import is:
    # @import url('https://fonts.googleapis.com/css2?family=Caveat&family=Inter:wght@400;500;600;700;800;900&family=DM+Sans:wght@400;500;600;700;800;900&display=swap');
    # We will replace family=Caveat with family=Caveat:wght@400;500;600;700
    old_import = r"family=Caveat&"
    new_import = "family=Caveat:wght@400;500;600;700&"
    
    if old_import in content:
        content = content.replace(old_import, new_import)
        
    # Just in case, let's also check if it's missing entirely
    if "family=Caveat" not in content:
        # replace Inter with Caveat+Inter
        content = content.replace("family=Inter", "family=Caveat:wght@400;500;600;700&family=Inter")

    with open(filepath, "w") as f:
        f.write(content)
    print(f"Fixed fonts in {filepath}")

fix_imports(files[0])
fix_imports(files[1])
