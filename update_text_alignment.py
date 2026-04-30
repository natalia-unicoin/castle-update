import re

files = [
    "/Users/Nati/.gemini/antigravity/scratch/Castle_V3_Standalone/masterclass.html",
    "/Users/Nati/.gemini/antigravity/scratch/Castle_V3_Standalone/masterclass_es.html"
]

for filepath in files:
    with open(filepath, "r") as f:
        content = f.read()

    # Change flex alignment from flex-start to flex-end
    content = content.replace('justify-content: flex-start;', 'justify-content: flex-end;')
    
    # Reverse the gradient so it's dark at the bottom
    content = content.replace('linear-gradient(to bottom, rgba(0,0,0,0.85) 0%, rgba(0,0,0,0) 60%)', 
                              'linear-gradient(to bottom, rgba(0,0,0,0) 0%, rgba(0,0,0,0.85) 100%)')
                              
    with open(filepath, "w") as f:
        f.write(content)
    
    print(f"Updated text alignment to bottom in {filepath}")
