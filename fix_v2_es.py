with open('masterclass_v2_es.html', 'r', encoding='utf-8') as f:
    content = f.read()

with open('masterclass_es.html', 'r', encoding='utf-8') as f:
    es_content = f.read()

# Extract modal from masterclass_es.html
# It starts around <!-- Unified CTA Modal --> or <link rel="stylesheet"...
start_idx = es_content.find('<!-- Unified CTA Modal -->')
if start_idx == -1:
    start_idx = es_content.find('<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/intl-tel-input')

clean_modal = es_content[start_idx : es_content.rfind('</body>')]

# Replace in masterclass_v2_es.html
start_v2 = content.find('<!-- Unified CTA Modal -->')
if start_v2 != -1:
    # slice up to start_v2
    new_content = content[:start_v2] + clean_modal + '\n</body>\n</html>\n'
    with open('masterclass_v2_es.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Fixed masterclass_v2_es.html")
else:
    print("Could not find start in masterclass_v2_es.html")
