import glob

files = glob.glob("*.html")
files = [f for f in files if "backup" not in f]

for f in files:
    with open(f, "r") as file:
        content = file.read()
    
    # Remove the f_id parameter from the URL
    content = content.replace('&amp;f_id=0079ece5f0', '')
    
    with open(f, "w") as file:
        file.write(content)

print("Removed f_id from Mailchimp URLs.")
