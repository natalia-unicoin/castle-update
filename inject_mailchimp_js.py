import glob
import re

files = glob.glob("*.html")
files = [f for f in files if "backup" not in f]

for f in files:
    with open(f, "r") as file:
        html = file.read()

    # check if already injected
    if 'src="./js/mailchimp.js"' in html:
        continue

    # insert right before </body>
    if '</body>' in html:
        html = html.replace('</body>', '    <script src="./js/mailchimp.js"></script>\n</body>')
    else:
        # fallback if no body tag
        html += '\n<script src="./js/mailchimp.js"></script>\n'
        
    with open(f, "w") as file:
        file.write(html)

print("Injected mailchimp.js script into all HTML files.")
