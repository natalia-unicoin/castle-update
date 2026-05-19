import re

with open('index_es.html', 'r', encoding='utf-8') as f:
    es_content = f.read()

with open('index.html', 'r', encoding='utf-8') as f:
    en_content = f.read()

# Extract the main <style> block from the head
style_pattern = re.compile(r'<style>.*?</style>', re.DOTALL)
es_style_match = style_pattern.search(es_content)

if es_style_match:
    es_style = es_style_match.group(0)
    en_content = style_pattern.sub(lambda m: es_style, en_content, count=1)
    
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(en_content)
    print("Style synced!")
else:
    print("Could not find style block")
