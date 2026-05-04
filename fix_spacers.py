import glob
import re

files = glob.glob("*.html")
files = [f for f in files if "backup" not in f]

for f in files:
    with open(f, "r") as file:
        content = file.read()
    
    # Inject CSS variables if not already there
    if "--spacer-80" not in content:
        # We find the :root block from our previous change and expand it
        old_root = ":root { --section-pad-y: 80px; --section-pad-large: 100px; }"
        new_root = ":root { --section-pad-y: 80px; --section-pad-large: 100px; --spacer-80: 80px; --spacer-60: 60px; --spacer-50: 50px; --spacer-40: 40px; --spacer-30: 30px; }"
        old_media = "@media (max-width: 768px) { :root { --section-pad-y: 30px; --section-pad-large: 30px; } }"
        new_media = "@media (max-width: 768px) { :root { --section-pad-y: 30px; --section-pad-large: 30px; --spacer-80: 40px; --spacer-60: 30px; --spacer-50: 25px; --spacer-40: 20px; --spacer-30: 15px; } }"
        
        content = content.replace(old_root, new_root)
        content = content.replace(old_media, new_media)
    
    # Define replacements
    replacements = {
        r'margin-top:\s*80px;': 'margin-top: var(--spacer-80);',
        r'margin-bottom:\s*80px;': 'margin-bottom: var(--spacer-80);',
        r'margin-top:\s*60px;': 'margin-top: var(--spacer-60);',
        r'margin-bottom:\s*60px;': 'margin-bottom: var(--spacer-60);',
        r'margin-top:\s*50px;': 'margin-top: var(--spacer-50);',
        r'margin-bottom:\s*50px;': 'margin-bottom: var(--spacer-50);',
        r'margin-top:\s*40px;': 'margin-top: var(--spacer-40);',
        r'margin-bottom:\s*40px;': 'margin-bottom: var(--spacer-40);',
        r'margin-top:\s*30px;': 'margin-top: var(--spacer-30);',
        r'margin-bottom:\s*30px;': 'margin-bottom: var(--spacer-30);',
        r'margin:\s*0\s*auto\s*80px\s*auto;': 'margin: 0 auto var(--spacer-80) auto;',
        r'margin:\s*0\s*auto\s*60px\s*auto;': 'margin: 0 auto var(--spacer-60) auto;',
        r'margin:\s*0\s*auto\s*50px\s*auto;': 'margin: 0 auto var(--spacer-50) auto;',
        r'margin:\s*0\s*auto\s*40px\s*auto;': 'margin: 0 auto var(--spacer-40) auto;',
        r'margin:\s*0\s*auto\s*30px\s*auto;': 'margin: 0 auto var(--spacer-30) auto;',
    }
    
    for pattern, replacement in replacements.items():
        content = re.sub(pattern, replacement, content)
        
    with open(f, "w") as file:
        file.write(content)

print("Applied responsive spacers.")
