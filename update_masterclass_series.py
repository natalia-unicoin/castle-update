import os

directories = ["."]

for d in directories:
    for filename in os.listdir(d):
        if filename.endswith(".html"):
            filepath = os.path.join(d, filename)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Replaces inside specific text strings:
            content = content.replace("join the Masterclass", "join the MasterClass Series")
            content = content.replace("join the MasterClass", "join the MasterClass Series")
            content = content.replace("participar en la Masterclass", "participar en la MasterClass Series")
            content = content.replace("participar en la MasterClass", "participar en la MasterClass Series")
            content = content.replace("Asistir a la Masterclass", "Asistir a la MasterClass Series") 
            
            # Nav/Footer links (inner text)
            content = content.replace(">MasterClass<", ">MasterClass Series<")
            content = content.replace(">Masterclass<", ">MasterClass Series<")
            
            # English replacements
            content = content.replace("4-day Masterclass", "4-day MasterClass Series")
            content = content.replace("Masterclass sessions", "MasterClass Series sessions")
            content = content.replace("another Masterclass", "another MasterClass Series")
            
            # Spanish replacements
            content = content.replace("4 MasterClasses en Vivo", "4 MasterClass Series en Vivo")
            content = content.replace("MASTERCLASS DE 4 DÍAS", "MASTERCLASS SERIES DE 4 DÍAS")
            content = content.replace("otra Masterclass", "otra MasterClass Series")
            content = content.replace("una masterclass", "una MasterClass Series")
            content = content.replace("MasterClasses Exclusivas", "MasterClass Series Exclusivas")
            content = content.replace("esta Masterclass", "esta MasterClass Series")
            content = content.replace("masterclasses, and experiences", "MasterClass Series, and experiences")
            content = content.replace("contenido, masterclasses y experiencias", "contenido, MasterClass Series y experiencias")
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)

print("Replacement complete.")
