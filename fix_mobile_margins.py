import glob
import re

files = glob.glob("*.html")
files = [f for f in files if "backup" not in f]

for f in files:
    with open(f, "r") as file:
        content = file.read()
    
    # Inject CSS variables
    if ":root { --section-pad-y:" not in content:
        injection = """
        :root { --section-pad-y: 80px; --section-pad-large: 100px; }
        @media (max-width: 768px) { :root { --section-pad-y: 30px; --section-pad-large: 30px; } }
        """
        content = content.replace("/* Full Site Layout Styles */", injection + "\n        /* Full Site Layout Styles */")

    # Replace hardcoded paddings
    content = re.sub(r'padding:\s*80px\s*0;', 'padding: var(--section-pad-y) 0;', content)
    content = re.sub(r'padding:\s*100px\s*4vw;', 'padding: var(--section-pad-large) 4vw;', content)
    content = re.sub(r'padding:\s*80px\s*4vw\s*0\s*4vw;', 'padding: var(--section-pad-y) 4vw 0 4vw;', content)
    content = re.sub(r'padding:\s*40px\s*4vw\s*80px\s*4vw;', 'padding: 40px 4vw var(--section-pad-y) 4vw;', content)
    
    # Also fix 80px top padding without horizontal
    content = re.sub(r'padding:\s*80px\s*4vw;', 'padding: var(--section-pad-y) 4vw;', content)
    
    # Bento Section 2 has padding: 80px 4vw 0 4vw; which is covered above.
    # We should also handle padding: 60px 5vw; if we want to tighten it.
    content = re.sub(r'padding:\s*60px\s*5vw;', 'padding: var(--section-pad-y) 5vw;', content)
    
    with open(f, "w") as file:
        file.write(content)

print("Updated section margins.")
