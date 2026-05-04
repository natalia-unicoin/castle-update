import os

files_to_update = [
    'about.html', 'about_es.html', 
    'contact.html', 'contact_es.html', 
    'partners.html', 'partners_es.html'
]

old_hero_start = """<section class="hero snap-section" style="background: url('./public/images/common/masterclass-hero.png') center/cover no-repeat; display: flex; align-items: flex-end; padding: 150px 4vw 80px 4vw; min-height: 100vh; position: relative;">"""

new_hero_start = """<section class="hero snap-section" style="background-color: #E5E7EB; display: flex; align-items: flex-end; padding: 150px 4vw 80px 4vw; min-height: 100vh; position: relative;">
        <!-- Placeholder Text -->
        <div style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; display: flex; align-items: center; justify-content: center; color: #9CA3AF; font-size: clamp(30px, 5vw, 60px); font-weight: 800; letter-spacing: 4px; text-transform: uppercase; z-index: 0; font-family: 'Inter', sans-serif; text-align: center;">Image Placeholder</div>"""

for fname in files_to_update:
    if os.path.exists(fname):
        with open(fname, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if old_hero_start in content:
            content = content.replace(old_hero_start, new_hero_start)
            with open(fname, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Updated {fname}")
        else:
            print(f"Hero section string not found in {fname}")
    else:
        print(f"File {fname} not found.")

