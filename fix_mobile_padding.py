import glob
import re

files = glob.glob("*.html")
files = [f for f in files if "backup" not in f]
for f in files:
    with open(f, "r") as file:
        content = file.read()
    
    # 1. Update lateral padding for .container and section > div
    content = re.sub(r'padding-left:\s*20px\s*!important;', 'padding-left: 10px !important;', content)
    content = re.sub(r'padding-right:\s*20px\s*!important;', 'padding-right: 10px !important;', content)
    
    # 2. Update .hero-container padding
    content = re.sub(r'padding:\s*0\s*20px\s*40px\s*20px;', 'padding: 0 10px 20px 10px;', content)
    
    # 3. Update padding-top for .hero-content
    content = re.sub(r'padding-top:\s*45vh;', 'padding-top: 55vh;', content)
    
    # 4. Update font-size clamp for hero title
    content = re.sub(r'clamp\(45px,', 'clamp(38px,', content)
    
    with open(f, "w") as file:
        file.write(content)

print("Updated all files.")
