import re

files = [
    "/Users/Nati/.gemini/antigravity/scratch/Castle_V3_Standalone/masterclass.html",
    "/Users/Nati/.gemini/antigravity/scratch/Castle_V3_Standalone/masterclass_es.html"
]

def update_truth_section(filepath):
    with open(filepath, "r") as f:
        content = f.read()

    # The Truth section regex
    regex = r'<!-- 5\. The Truth -->\s*<section class="snap-section".*?</section>'
    
    if re.search(regex, content, re.DOTALL):
        # Extract the current block
        block = re.search(regex, content, re.DOTALL).group(0)
        
        # Make background purple
        block = block.replace('background-color: #F8F8FA;', 'background-color: #A03FA3;')
        
        # Widen the container
        block = block.replace('max-width: 1000px;', 'max-width: 1300px;')
        
        # Change eyebrow color
        block = block.replace('color: #A03FA3;', 'color: rgba(255,255,255,0.8);')
        
        # Change H2 text color from #1A1A1A to #FFFFFF
        block = block.replace('color: #1A1A1A;', 'color: #FFFFFF;')

        # Just to be safe, if H2 text color was defined differently, enforce it:
        # Actually in the original it's `color: #1A1A1A;`
        
        content = re.sub(regex, block, content, flags=re.DOTALL)
        
        with open(filepath, "w") as f:
            f.write(content)
        print(f"Updated The Truth section in {filepath}")
    else:
        print(f"Section not found in {filepath}")

update_truth_section(files[0])
update_truth_section(files[1])
