def extract_modal(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    start_str = "<!-- INJECTED UNIFIED MODAL START -->"
    end_str = "<!-- INJECTED UNIFIED MODAL END -->"
    
    start_idx = content.find(start_str)
    end_idx = content.find(end_str)
    
    if start_idx == -1 or end_idx == -1:
        print(f"Could not find injected modal in {filename}")
        return ""
        
    return content[start_idx : end_idx + len(end_str)]

en_modal = extract_modal('masterclass.html')
es_modal = extract_modal('masterclass_es.html')

def update_file(filename, new_modal):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Remove old modal. It starts with <div id="waitlistModal" or <!-- INJECTED...
    import re
    # If it has INJECTED markers
    if "<!-- INJECTED UNIFIED MODAL START -->" in content:
        content = re.sub(r'<!-- INJECTED UNIFIED MODAL START -->.*?<!-- INJECTED UNIFIED MODAL END -->', '', content, flags=re.DOTALL)
    
    # If it has old waitlistModal manually added
    if '<div id="waitlistModal"' in content:
        content = re.sub(r'<div id="waitlistModal".*?</script>\s*</div>\s*</div>\s*<script src="\./js/mailchimp\.js"></script>\s*<script>.*?</script>', '', content, flags=re.DOTALL)
        # Fallback if there are multiple script tags or it didn't match perfectly
        content = re.sub(r'<div id="waitlistModal".*?</body>', '</body>', content, flags=re.DOTALL)
        
    # Also remove any leftover <script src="./js/mailchimp.js"></script>
    content = content.replace('<script src="./js/mailchimp.js"></script>', '')
    
    # Insert new modal before </body>
    content = content.replace('</body>', new_modal + '\n</body>')
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {filename}")

if en_modal:
    update_file('masterclass_v2.html', en_modal)
if es_modal:
    update_file('masterclass_v2_es.html', es_modal)

