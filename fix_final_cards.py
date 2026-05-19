import re

def update_cards(filepath, is_es=True):
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    # The entire grid block to replace
    # It currently starts with <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 16px;">
    # and ends right before <!-- CTA Final -->
    
    mc_title = "MasterClass" if is_es else "MasterClass"
    mc_desc = "Aprende los fundamentos para tomar control de tu riqueza." if is_es else "Learn the fundamentals to take control of your wealth."
    
    pt_title = "Partnerships" if is_es else "Partnerships"
    pt_desc = "Únete como creadora, influencer o marca." if is_es else "Join as a creator, influencer, or brand."
    
    ab_title = "Nuestra Historia" if is_es else "Our Story"
    ab_desc = "Conoce la visión de Castle y nuestro futuro." if is_es else "Learn about Castle's vision and our future."
    
    mc_link = "masterclass_es.html" if is_es else "masterclass.html"
    pt_link = "partners_es.html" if is_es else "partners.html"
    ab_link = "about_es.html" if is_es else "about.html"

    new_grid = f'''<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 20px;">
            <!-- Card 1 -->
            <a href="{mc_link}" style="aspect-ratio: 3/4; border-radius: 5px; overflow: hidden; position: relative; display: block; text-decoration: none;">
                <img src="./public/images/common/card-masterclass.jpg?v=4" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; object-fit: cover; z-index: 1;">
                <div style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; background: linear-gradient(to top, rgba(0,0,0,0.9) 0%, rgba(0,0,0,0) 60%); z-index: 2;"></div>
                <div style="position: absolute; bottom: 0; left: 0; width: 100%; padding: 40px 20px; z-index: 3; display: flex; flex-direction: column; align-items: center; text-align: center;">
                    <span style="display: block; font-family: 'Caveat', cursive; font-size: clamp(32px, 4vw, 42px); color: #FFFFFF; font-weight: 700; line-height: 1; margin-bottom: 8px;">{mc_title}</span>
                    <span style="display: block; font-family: 'Inter', sans-serif; font-size: 16px; color: #FFFFFF; font-weight: 500;">{mc_desc}</span>
                </div>
            </a>

            <!-- Card 2 -->
            <a href="{pt_link}" style="aspect-ratio: 3/4; border-radius: 5px; overflow: hidden; position: relative; display: block; text-decoration: none;">
                <img src="./public/images/common/card-partners.jpg?v=4" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; object-fit: cover; z-index: 1;">
                <div style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; background: linear-gradient(to top, rgba(0,0,0,0.9) 0%, rgba(0,0,0,0) 60%); z-index: 2;"></div>
                <div style="position: absolute; bottom: 0; left: 0; width: 100%; padding: 40px 20px; z-index: 3; display: flex; flex-direction: column; align-items: center; text-align: center;">
                    <span style="display: block; font-family: 'Caveat', cursive; font-size: clamp(32px, 4vw, 42px); color: #FFFFFF; font-weight: 700; line-height: 1; margin-bottom: 8px;">{pt_title}</span>
                    <span style="display: block; font-family: 'Inter', sans-serif; font-size: 16px; color: #FFFFFF; font-weight: 500;">{pt_desc}</span>
                </div>
            </a>

            <!-- Card 3 -->
            <a href="{ab_link}" style="aspect-ratio: 3/4; border-radius: 5px; overflow: hidden; position: relative; display: block; text-decoration: none; background-color: #111;">
                <div style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; background: linear-gradient(to top, rgba(0,0,0,0.9) 0%, rgba(0,0,0,0) 60%); z-index: 2;"></div>
                <div style="position: absolute; bottom: 0; left: 0; width: 100%; padding: 40px 20px; z-index: 3; display: flex; flex-direction: column; align-items: center; text-align: center;">
                    <span style="display: block; font-family: 'Caveat', cursive; font-size: clamp(32px, 4vw, 42px); color: #FFFFFF; font-weight: 700; line-height: 1; margin-bottom: 8px;">{ab_title}</span>
                    <span style="display: block; font-family: 'Inter', sans-serif; font-size: 16px; color: #FFFFFF; font-weight: 500;">{ab_desc}</span>
                </div>
            </a>
        </div>'''

    # We need to replace everything from <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 16px;">
    # down to the closing </div> of the grid.
    
    # regex to match the grid block
    pattern = re.compile(r'<div style="display: grid; grid-template-columns: repeat\(auto-fit, minmax\([^)]+\)\); gap: 16px;">.*?</a>\s*</div>', re.DOTALL)
    html = pattern.sub(new_grid, html)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)
        print(f"Updated {filepath}")

update_cards('contact_es.html', is_es=True)
update_cards('contact.html', is_es=False)

