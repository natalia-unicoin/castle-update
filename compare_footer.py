import re

with open('index_es.html', 'r', encoding='utf-8') as f:
    es_content = f.read()

with open('index.html', 'r', encoding='utf-8') as f:
    en_content = f.read()

def get_footer(html):
    m = re.search(r'<footer.*?</footer>', html, re.DOTALL)
    return m.group(0) if m else "No footer"

es_footer = get_footer(es_content)
en_footer = get_footer(en_content)

print("ES FOOTER LEN:", len(es_footer))
print("EN FOOTER LEN:", len(en_footer))
if len(es_footer) != len(en_footer):
    print("Different lengths!")
