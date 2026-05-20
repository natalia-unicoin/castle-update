import glob

files = glob.glob('*_es.html')
for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    content = content.replace('</body>', '<!-- Unified CTA Modal -->\n</body>')
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)
