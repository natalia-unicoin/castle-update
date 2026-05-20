import re

files = [
    'partners_es.html',
    'partners.html',
    'about_es.html',
    'about.html',
    'masterclass_es.html',
    'masterclass.html'
]

SECTION_STYLE = "display: flex; align-items: flex-end; padding: 150px 4vw 80px 4vw; min-height: 100vh; position: relative;"
H1_STYLE = "color: #FFFFFF; font-size: clamp(50px, 7vw, 90px); letter-spacing: -2px; margin-bottom: 24px; text-shadow: 0 4px 12px rgba(0,0,0,0.5); font-family: 'Inter', sans-serif; font-weight: 700;"
P_STYLE = "color: rgba(255,255,255,0.95); font-size: clamp(18px, 2vw, 24px); line-height: 1.5; max-width: 700px; margin: 0 auto; font-family: 'Inter', sans-serif;"

for f in files:
    with open(f, 'r') as file:
        content = file.read()
    
    # We will modify the hero section manually by finding it and using regex.
    # To be very precise, we can use a callback in re.sub
    
    def process_hero(match):
        hero_html = match.group(0)
        
        # 1. Update section style
        # Find the section style
        style_match = re.search(r'<section[^>]+style="([^"]+)"', hero_html)
        if style_match:
            old_style = style_match.group(1)
            # Remove conflicting properties
            new_style = re.sub(r'display:\s*[^;]+;', '', old_style)
            new_style = re.sub(r'align-items:\s*[^;]+;', '', new_style)
            new_style = re.sub(r'padding:\s*[^;]+;', '', new_style)
            new_style = re.sub(r'min-height:\s*[^;]+;', '', new_style)
            new_style = re.sub(r'position:\s*[^;]+;', '', new_style)
            new_style = re.sub(r'padding-bottom:\s*[^;]+;', '', new_style)
            new_style = re.sub(r'justify-content:\s*[^;]+;', '', new_style)
            new_style = re.sub(r'height:\s*[^;]+;', '', new_style)
            
            new_style = new_style.strip() + " " + SECTION_STYLE
            hero_html = hero_html[:style_match.start(1)] + new_style + hero_html[style_match.end(1):]
        else:
            hero_html = re.sub(r'<section class="hero[^"]*"', r'\g<0> style="' + SECTION_STYLE + '"', hero_html, count=1)
            
        # 2. Update padding-top: 40vh in masterclass container
        hero_html = re.sub(r'padding-top:\s*40vh;', '', hero_html)
        
        # 3. Update h1 style
        h1_style_match = re.search(r'<h1[^>]+class="hero-title[^"]*"[^>]*style="([^"]+)"', hero_html)
        if h1_style_match:
            hero_html = hero_html[:h1_style_match.start(1)] + H1_STYLE + hero_html[h1_style_match.end(1):]
        else:
            hero_html = re.sub(r'(<h1[^>]+class="hero-title[^"]*")', r'\1 style="' + H1_STYLE + '"', hero_html, count=1)
            
        # 4. Update subtitle (p) style
        # Find the first paragraph after h1 that acts as subtitle
        # This is tricky because it might not have hero-subtitle class
        # Let's target the paragraph right after h1
        # In partners, it's just <p style="...">
        p_match = re.search(r'</h1>\s*<p([^>]*)style="([^"]+)"', hero_html)
        if p_match:
            hero_html = hero_html[:p_match.start(2)] + P_STYLE + hero_html[p_match.end(2):]
        else:
            # Maybe it doesn't have a style attribute yet
            p_match_no_style = re.search(r'</h1>\s*<p([^>]*)>', hero_html)
            if p_match_no_style:
                hero_html = hero_html[:p_match_no_style.end(1)] + ' style="' + P_STYLE + '">' + hero_html[p_match_no_style.end():]
            
        # Masterclass has an extra <p> in masterclass.html (description)
        hero_html = re.sub(r'<p class="hero-description[^"]*"[^>]*style="([^"]+)"', r'<p class="hero-subtitle color-reveal" style="' + P_STYLE + '"', hero_html)

        return hero_html

    # We need to find the hero section boundaries.
    # It starts with <section class="hero ...
    # And ends with </section>
    new_content = re.sub(r'<section class="hero snap-section".*?</section>', process_hero, content, flags=re.DOTALL, count=1)
    
    with open(f, 'w') as file:
        file.write(new_content)
        
print("Updated heroes!")
