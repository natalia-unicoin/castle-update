import re

with open('contact.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update Hero Subtitle
old_hero_p = "Take control of your financial future. Join the Women-led Wealth revolution."
new_hero_p = "Have a question, partnership idea, or just want to say hello? Drop us a message below and our team will get back to you."
content = content.replace(old_hero_p, new_hero_p)

# 2. Update Form Container Style
old_container_style = '<div class="container" style="max-width: 700px; width: 100%; background: #FFFFFF; border-radius: 8px; padding: 60px 40px; box-shadow: 0 40px 100px rgba(0,0,0,0.1); border: 1px solid #E5E7EB; text-align: left;">'
new_container_style = '<div class="container" style="max-width: 700px; width: 100%; text-align: left; padding: 0;">'
content = content.replace(old_container_style, new_container_style)

# 3. Remove Form Title & Paragraph
form_header_regex = re.compile(r'\s*<div style="text-align: center; margin-bottom: 40px;">\s*<h2[^>]*>Contact Us</h2>\s*<p[^>]*>\s*Have a question, partnership idea, or just want to say hello\? Drop us a message below and our team will get back to you\.\s*</p>\s*</div>', re.DOTALL)
content = form_header_regex.sub('', content)

with open('contact.html', 'w', encoding='utf-8') as f:
    f.write(content)
