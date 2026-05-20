import re
import glob

def process_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # English version
    en_pattern = r'<div style="display: flex; gap: 10px; max-width: 500px; margin: 0 auto; width: 100%; flex-wrap: wrap; justify-content: center;">\s*<input type="email" id="inline_newsletter_email"[^>]*>\s*<button onclick="submitInlineNewsletter\(\)"[^>]*>SUBSCRIBE</button>\s*</div>'
    en_repl = r'<button onclick="openUnifiedModal(\'newsletter\')" style="background-color: #A03FA3; color: #FFFFFF; font-weight: 800; letter-spacing: 1.5px; padding: 16px 40px; border-radius: 50px; border: none; font-size: 14px; cursor: pointer; transition: background 0.2s, transform 0.2s; box-shadow: 0 4px 15px rgba(160,63,163,0.3); font-family: \'Inter Tight\', sans-serif; text-transform: uppercase;">SUBSCRIBE</button>'
    
    # Spanish version
    es_pattern = r'<div style="display: flex; gap: 10px; max-width: 500px; margin: 0 auto; width: 100%; flex-wrap: wrap; justify-content: center;">\s*<input type="email" id="inline_newsletter_email"[^>]*>\s*<button onclick="submitInlineNewsletter\(\)"[^>]*>SUSCRÍBETE</button>\s*</div>'
    es_repl = r'<button onclick="openUnifiedModal(\'newsletter\')" style="background-color: #A03FA3; color: #FFFFFF; font-weight: 800; letter-spacing: 1.5px; padding: 16px 40px; border-radius: 50px; border: none; font-size: 14px; cursor: pointer; transition: background 0.2s, transform 0.2s; box-shadow: 0 4px 15px rgba(160,63,163,0.3); font-family: \'Inter Tight\', sans-serif; text-transform: uppercase;">SUSCRÍBETE</button>'

    new_content = re.sub(en_pattern, en_repl, content)
    new_content = re.sub(es_pattern, es_repl, new_content)

    if new_content != content:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {filename}")

for file in glob.glob("*.html"):
    process_file(file)
