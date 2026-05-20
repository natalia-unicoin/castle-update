import os
import glob

files = glob.glob('*_es.html')
for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    start = content.find('<!-- Unified CTA Modal -->')
    if start != -1:
        end = content.find('</body>')
        content = content[:start] + '\n</body>\n</html>\n'
        with open(f, 'w', encoding='utf-8') as file:
            file.write(content)
