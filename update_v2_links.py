import os

for filename in ['masterclass_v2.html', 'masterclass_v2_es.html']:
    filepath = f"/Users/Naty/.gemini/antigravity/scratch/castle-update/{filename}"
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        content = content.replace('masterclass.html', 'masterclass_v2.html')
        content = content.replace('masterclass_es.html', 'masterclass_v2_es.html')
        
        # fix double v2 in case some were already correct or just in case
        content = content.replace('masterclass_v2_v2', 'masterclass_v2')
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
print("Updated links in v2 files.")
