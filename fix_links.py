import os
import glob
import re

files = glob.glob("/Users/Nati/.gemini/antigravity/scratch/Castle_V3_Standalone/*_es.html")

for file in files:
    with open(file, "r") as f:
        content = f.read()

    # Fix duplicated hrefs
    content = content.replace('href="masterclass_es.html" style="text-transform: none;" href="masterclass_es.html"', 'href="masterclass_es.html" style="text-transform: none;"')
    content = content.replace('href="masterclass_es.html" href="masterclass_es.html"', 'href="masterclass_es.html"')
    
    # Fix legal links
    content = content.replace('<a href="masterclass_es.html">Política de Privacidad</a>', '<a href="#">Política de Privacidad</a>')
    content = content.replace('<a href="masterclass_es.html">Términos de Servicio</a>', '<a href="#">Términos de Servicio</a>')
    content = content.replace('<a href="masterclass_es.html">Política de Cookies</a>', '<a href="#">Política de Cookies</a>')

    with open(file, "w") as f:
        f.write(content)

print("Fixed links in all _es.html files")
