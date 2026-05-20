import re

def update_file(filename):
    with open(filename, 'r') as f:
        content = f.read()

    # The string to replace is usually: url('./public/images/common/ecosystem-bg.jpg?v=1')
    # or url('./public/images/common/ecosystem-bg.jpg')
    new_content = re.sub(r'url\([^)]+ecosystem-bg\.jpg(\?v=1)?\)', r"url('./public/images/common/ecosystem-sunset.png')", content)
    
    if new_content != content:
        with open(filename, 'w') as f:
            f.write(new_content)
        print(f"Updated {filename}")
    else:
        print(f"No changes in {filename}")

update_file('contact.html')
update_file('contact_es.html')
