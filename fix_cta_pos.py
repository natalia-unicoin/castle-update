import re

def fix_file(filename, btn_text):
    with open(filename, 'r') as f:
        content = f.read()

    # Find the Explore Castle section
    if 'Explora Castle' in content:
        title = 'Explora Castle'
        subtitle_text = 'Descubre todo lo que nuestro ecosistema tiene para ofrecerte.'
    else:
        title = 'Explore Castle'
        subtitle_text = 'Discover everything our ecosystem has to offer.'

    # Find the top block
    top_block_pattern = r'(<div style="text-align: center; margin-bottom: 30px;">\s*<h2 class="section-title"[^>]*>'+title+r'</h2>\s*<p class="section-subtitle[^>]*>'+subtitle_text+r'</p>\s*<div style="text-align: center; margin-top: 30px; margin-bottom: 50px;">\s*<a[^>]*>'+btn_text+r'</a>\s*</div>\s*</div>)'
    
    top_block_match = re.search(top_block_pattern, content)
    
    if not top_block_match:
        print(f"Could not find top block in {filename}")
        return
        
    original_top = top_block_match.group(1)
    
    new_top = f'''        <div style="text-align: center; margin-bottom: 50px;">
            <h2 class="section-title" style="margin-bottom: 16px; padding: 0; color: #1A1A1A;">{title}</h2>
            <p class="section-subtitle-1" style="max-width: 1000px; width: 100%; margin: 0 auto; text-align: center;">{subtitle_text}</p>
        </div>'''
        
    content = content.replace(original_top, new_top)
    
    # Find the bottom of the section to insert CTA
    bottom_pattern = r'(            </a>\s*</div>\s*)(</div>\s*</section>)'
    bottom_match = re.search(bottom_pattern, content)
    
    if not bottom_match:
        print(f"Could not find bottom in {filename}")
        return
        
    btn_html = f'''        <div style="text-align: center; margin-top: 50px; margin-bottom: 20px;">
            <a href="javascript:void(0);" onclick="openUnifiedModal('contact')" class="btn-large" style="display: inline-block; background-color: #A03FA3; color: #FFFFFF; font-weight: 800; letter-spacing: 2px; padding: 22px 60px; border-radius: 50px; font-size: 16px; text-decoration: none; box-shadow: 0 10px 30px rgba(160, 63, 163, 0.4); transition: transform 0.2s ease;">{btn_text}</a>
        </div>
    '''
    
    new_bottom = bottom_match.group(1) + btn_html + bottom_match.group(2)
    
    content = content.replace(bottom_match.group(0), new_bottom)
    
    with open(filename, 'w') as f:
        f.write(content)
    print(f"Successfully fixed {filename}")

fix_file('contact_es.html', 'CONTACTAR AL EQUIPO')
fix_file('contact.html', 'CONTACT THE TEAM')
