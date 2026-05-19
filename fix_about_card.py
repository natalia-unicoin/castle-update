import re

def update_about(filepath, is_es=True):
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    old_title = "Nuestra Historia" if is_es else "Our Story"
    new_title = "Somos Castle" if is_es else "We Are Castle"
    
    # Replace the title
    html = html.replace(old_title, new_title)
    
    # Add the image tag to the third card. The third card doesn't have an img tag right now.
    # We look for the </a> block for about_es.html or about.html
    link_href = "about_es.html" if is_es else "about.html"
    
    # Find the a tag for the third card
    # <a href="about_es.html" style="aspect-ratio: 3/4; border-radius: 5px; overflow: hidden; position: relative; display: block; text-decoration: none; background-color: #111;">
    #     <div style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; background: linear-gradient(to top, rgba(0,0,0,0.9) 0%, rgba(0,0,0,0) 60%); z-index: 2;"></div>
    
    old_a_tag = f'<a href="{link_href}" style="aspect-ratio: 3/4; border-radius: 5px; overflow: hidden; position: relative; display: block; text-decoration: none; background-color: #111;">\n                <div style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; background: linear-gradient(to top, rgba(0,0,0,0.9) 0%, rgba(0,0,0,0) 60%); z-index: 2;"></div>'
    
    new_a_tag = f'<a href="{link_href}" style="aspect-ratio: 3/4; border-radius: 5px; overflow: hidden; position: relative; display: block; text-decoration: none; background-color: #111;">\n                <img src="./public/images/common/card-about.jpg?v=1" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; object-fit: cover; object-position: center; z-index: 1;">\n                <div style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; background: linear-gradient(to top, rgba(0,0,0,0.9) 0%, rgba(0,0,0,0) 60%); z-index: 2;"></div>'
    
    html = html.replace(old_a_tag, new_a_tag)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)
        print(f"Updated {filepath}")

update_about('contact_es.html', is_es=True)
update_about('contact.html', is_es=False)

