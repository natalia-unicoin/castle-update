import re

def process_file(filename):
    with open(filename, 'r') as f:
        content = f.read()

    # Find sections
    # 1. Form Section
    form_sec_match = re.search(r'<!-- 2\. Form Section -->\s*<section id="contact-form-section".*?</section>', content, re.DOTALL)
    if not form_sec_match:
        print(f"Missing Form Section in {filename}")
        return
        
    # 2. Social Proof
    # In contact.html, Social Proof is followed by </div></section>
    # So we need to match it cleanly.
    social_sec_match = re.search(r'(<!-- Social Proof / Ecosystem -->\s*<section.*?</section>\s*</div>\s*</section>)', content, re.DOTALL)
    if not social_sec_match:
        social_sec_match = re.search(r'(<!-- Social Proof / Ecosystem -->\s*<section.*?</section>)', content, re.DOTALL)
        
    if not social_sec_match:
        print("Missing Social Proof")
        return
        
    # 3. Quick Resources
    resources_sec_match = re.search(r'(<!-- Quick Resources -->\s*<section.*?Explore Castle.*?</section>)', content, re.DOTALL)
    if not resources_sec_match:
        print("Missing Quick Resources")
        return
    
    # We will remove them from the original content
    form_html = form_sec_match.group(0)
    social_html = social_sec_match.group(0)
    res_html = resources_sec_match.group(0)
    
    content = content.replace(form_html, "")
    
    # Let's extract exactly the social block up to <!-- Quick Resources --> if it's there
    social_full_match = re.search(r'<!-- Social Proof / Ecosystem -->.*?(?=<!-- Quick Resources|$)', content, re.DOTALL)
    if social_full_match:
        social_html_to_remove = social_full_match.group(0)
        content = content.replace(social_html_to_remove, "")
        
        # Clean up social_html
        social_clean_match = re.search(r'<!-- Social Proof / Ecosystem -->.*?Join the Ecosystem.*?</section>', social_html_to_remove, re.DOTALL)
        if social_clean_match:
             social_html = social_clean_match.group(0)

    content = content.replace(res_html, "")

    # Inject button into Quick Resources
    btn_html = '<a href="javascript:void(0);" onclick="openUnifiedModal(\'contact\')" class="btn-large" style="display: inline-block; background-color: #A03FA3; color: #FFFFFF; font-weight: 800; letter-spacing: 2px; padding: 22px 60px; border-radius: 50px; font-size: 16px; text-decoration: none; box-shadow: 0 10px 30px rgba(160, 63, 163, 0.4); transition: transform 0.2s ease;">CONTACT THE TEAM</a>'
    
    subtitle_match = re.search(r'(<p class="section-subtitle"[^>]*>.*?</p>)', res_html)
    if subtitle_match:
        new_res_html = res_html[:subtitle_match.end(1)] + f'\n        <div style="text-align: center; margin-top: 30px; margin-bottom: 50px;">\n            {btn_html}\n        </div>' + res_html[subtitle_match.end(1):]
    else:
        new_res_html = res_html
        
    # Ensure snap-section is added
    if 'class="snap-section"' not in new_res_html and 'class=' in new_res_html:
        new_res_html = new_res_html.replace('<section style="', '<section class="snap-section" style="')
    elif 'class=' not in new_res_html:
        new_res_html = new_res_html.replace('<section style="', '<section class="snap-section" style="')
        
    if 'class="snap-section"' not in social_html and 'class=' in social_html:
        social_html = social_html.replace('<section style="', '<section class="snap-section" style="')
    elif 'class=' not in social_html:
        social_html = social_html.replace('<section style="', '<section class="snap-section" style="')

    # Find Hero end
    hero_end = re.search(r'<!-- 1\. Hero Section -->.*?</section>', content, re.DOTALL)
    if hero_end:
        insert_pos = hero_end.end(0)
        new_content = content[:insert_pos] + "\n\n" + new_res_html + "\n\n" + social_html + "\n\n" + content[insert_pos:]
        
        with open(filename, 'w') as f:
            f.write(new_content)
        print(f"Successfully processed {filename}")
    else:
        print(f"Could not find hero end in {filename}")

process_file('contact.html')
