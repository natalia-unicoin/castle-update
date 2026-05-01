import re

files_to_update = {
    'about.html': {
        'title': 'Own your Wealth.<br>Own your Future.',
        'subtitle': '<p class="hero-subtitle color-reveal" style="color: rgba(255,255,255,0.95); font-size: clamp(18px, 2vw, 24px); line-height: 1.5; max-width: 700px; margin: 0 auto;">Castle is where your relationship with money changes—for real.</p>'
    },
    'about_es.html': {
        'title': 'Somos Castle',
        'subtitle': ''
    },
    'partners.html': {
        'title': 'Partners',
        'subtitle': ''
    },
    'partners_es.html': {
        'title': 'Socios',
        'subtitle': ''
    },
    'contact.html': {
        'title': 'Contact Us',
        'subtitle': ''
    },
    'contact_es.html': {
        'title': 'Contáctanos',
        'subtitle': ''
    }
}

style_block = """    <!-- 1. Hero Section -->
    <style>
        /* Force white header on this page */
        #main-header { background: rgba(255, 255, 255, 0.98) !important; backdrop-filter: blur(12px) !important; border-bottom: 1px solid #E5E7EB !important; padding: 16px clamp(30px, 5vw, 100px) !important; }
        #main-header .logo-light { display: none !important; }
        #main-header .logo-dark { display: block !important; }
        #main-header .nav-links a { color: #1A1A1A !important; }
        #main-header .nav-links a:hover { color: #A03FA3 !important; }
        #main-header .lang-select { color: #1A1A1A !important; border-color: #E5E7EB !important; background-image: url('data:image/svg+xml;utf8,<svg fill="%231A1A1A" height="24" viewBox="0 0 24 24" width="24" xmlns="http://www.w3.org/2000/svg"><path d="M7 10l5 5 5-5z"/><path d="M0 0h24v24H0z" fill="none"/></svg>') !important; }
        .mobile-menu-toggle { color: #1A1A1A !important; }
    </style>"""

for fname, data in files_to_update.items():
    with open(fname, 'r', encoding='utf-8') as f:
        content = f.read()
        
    hero_template = f"""{style_block}
    <section class="hero snap-section" style="background: url('./public/images/common/masterclass-hero.png') center/cover no-repeat; display: flex; align-items: flex-end; padding: 150px 4vw 80px 4vw; min-height: 100vh; position: relative;">
        <!-- Black Gradient Overlay -->
        <div style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; background: linear-gradient(180deg, rgba(0,0,0,0) 0%, rgba(0,0,0,0.85) 100%); z-index: 1;"></div>
        
        <div class="container" style="max-width: 1000px; margin: 0 auto; display: flex; justify-content: center; align-items: center; position: relative; z-index: 2;">
            <div style="text-align: center; width: 100%;">
                <h1 class="hero-title color-reveal" style="color: #FFFFFF; font-size: clamp(50px, 7vw, 90px); letter-spacing: -2px; margin-bottom: 24px; text-shadow: 0 4px 12px rgba(0,0,0,0.5);">{data['title']}</h1>
                {data['subtitle']}
            </div>
        </div>
    </section>"""

    # First, let's remove any existing "Force white header" style blocks to avoid duplication
    content = re.sub(r'    <!-- 1\. Hero Section -->\s*<style>\s*/\* Force white header.*?</style>', '', content, flags=re.DOTALL)
    
    # Replace the existing Hero section block
    # It might be labelled "Hero Section" or "Hero Placeholder"
    hero_regex = r'(?:    <!-- Hero Section -->|    <!-- Hero Placeholder -->)\s*<section class="hero snap-section"[^>]*>.*?</section>'
    
    if re.search(hero_regex, content, re.DOTALL):
        content = re.sub(hero_regex, hero_template, content, flags=re.DOTALL)
        with open(fname, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {fname}")
    else:
        print(f"Hero section not found in {fname}")

