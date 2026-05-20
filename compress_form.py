with open('inject_dynamic_form_es.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Title font size
content = content.replace('font-size: clamp(28px, 4vw, 36px);', 'font-size: clamp(26px, 4vw, 34px);')
# Subtitle color to black
content = content.replace('color: #4B5563; margin-bottom: 25px;', 'color: #111827; margin-bottom: 20px;')
# Reduce modal vertical padding
content = content.replace('padding: 40px 40px;', 'padding: 35px 40px;')
# Reduce bottom margin of checkboxes
content = content.replace('margin-bottom: 25px; background: #F9FAFB;', 'margin-bottom: 15px; background: #F9FAFB;')
# Reduce all margin-top: 15px; to margin-top: 12px;
content = content.replace('margin-top: 15px;', 'margin-top: 12px;')
# Reduce subscription margin-top: 25px; to 15px;
content = content.replace('margin-top: 25px; background: #F3F4F6;', 'margin-top: 15px; background: #F3F4F6;')

with open('inject_dynamic_form_es.py', 'w', encoding='utf-8') as f:
    f.write(content)
