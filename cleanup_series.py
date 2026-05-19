import os

directories = ["."]

for d in directories:
    for filename in os.listdir(d):
        if filename.endswith(".html"):
            filepath = os.path.join(d, filename)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Clean up the double 'Series' mistake
            content = content.replace("MasterClass Series Series", "MasterClass Series")
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)

print("Cleanup complete.")
