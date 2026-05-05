import glob

files = glob.glob("*.html")
files = [f for f in files if "backup" not in f]

for f in files:
    with open(f, "r") as file:
        content = file.read()
    
    # We will just inject text-transform: uppercase; right after .waitlist-submit {
    content = content.replace('.waitlist-submit { background-color', '.waitlist-submit { text-transform: uppercase; background-color')
    
    with open(f, "w") as file:
        file.write(content)

print("Added uppercase to waitlist buttons.")
