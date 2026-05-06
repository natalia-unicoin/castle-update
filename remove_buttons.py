import re

def remove_buttons(filename):
    with open(filename, "r") as f:
        html = f.read()
    
    # We want to remove the block that looks like:
    # <div style="display: flex; gap: 16px; justify-content: center; flex-wrap: wrap;">
    #     <a href="https://www.instagram.com/buildyourcastle_ai/" target="_blank" class="waitlist-submit"...>
    #     <a href="https://www.linkedin.com/company/buildyourcastle/about/" target="_blank" class="waitlist-submit"...>
    # </div>
    
    # Let's use regex to find and remove this div
    pattern = r'<div style="display: flex; gap: 16px; justify-content: center; flex-wrap: wrap;">(.*?)</div>'
    
    # Wait, the string matching might be tricky because of multiline. Let's use DOTALL.
    html = re.sub(pattern, '', html, flags=re.DOTALL)
    
    with open(filename, "w") as f:
        f.write(html)

remove_buttons("gracias.html")
remove_buttons("thank-you.html")
print("Removed buttons.")
