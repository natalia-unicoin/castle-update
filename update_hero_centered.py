import re

files = [
    "/Users/Nati/.gemini/antigravity/scratch/Castle_V3_Standalone/masterclass.html",
    "/Users/Nati/.gemini/antigravity/scratch/Castle_V3_Standalone/masterclass_es.html"
]

def update_hero_centered(filepath, is_es):
    with open(filepath, "r") as f:
        content = f.read()

    # 1. Update the Hero Section
    regex = r'<!-- 1\. Hero Section -->.*?</section>'
    
    if is_es:
        eyebrow = "Masterclass de 4 días"
        title = "Construye tu Castle.<br><span style=\"color: #FFFFFF;\">Sé dueña de tu riqueza.</span>"
        date_text = "1–4 de junio | Organizado por Castle | Impulsado por Unicoin Foundation"
        btn_text = "APLICA AHORA"
    else:
        eyebrow = "4-day Masterclass"
        title = "Build Your Castle.<br><span style=\"color: #FFFFFF;\">Own Your Wealth.</span>"
        date_text = "June 1–4 | Hosted by Castle | Powered by Unicoin Foundation"
        btn_text = "APPLY NOW"

    new_html = f"""<!-- 1. Hero Section -->
    <style>
        /* Force white header on this page */
        #main-header {{ background: rgba(255, 255, 255, 0.98) !important; backdrop-filter: blur(12px) !important; border-bottom: 1px solid #E5E7EB !important; padding: 16px clamp(30px, 5vw, 100px) !important; }}
        #main-header .logo-light {{ display: none !important; }}
        #main-header .logo-dark {{ display: block !important; }}
        #main-header .nav-links a {{ color: #1A1A1A !important; }}
        #main-header .nav-links a:hover {{ color: #A03FA3 !important; }}
        #main-header .lang-select {{ color: #1A1A1A !important; border-color: #E5E7EB !important; background-image: url('data:image/svg+xml;utf8,<svg fill="%231A1A1A" height="24" viewBox="0 0 24 24" width="24" xmlns="http://www.w3.org/2000/svg"><path d="M7 10l5 5 5-5z"/><path d="M0 0h24v24H0z" fill="none"/></svg>') !important; }}
        .mobile-menu-toggle {{ color: #1A1A1A !important; }}
    </style>
    <section class="hero snap-section" style="background: url('./public/images/common/masterclass-hero.png') center/cover no-repeat; display: flex; align-items: flex-end; padding: 150px 4vw 80px 4vw; min-height: 100vh; position: relative;">
        <!-- Black Gradient Overlay -->
        <div style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; background: linear-gradient(180deg, rgba(0,0,0,0) 0%, rgba(0,0,0,0.85) 100%); z-index: 1;"></div>
        
        <div class="container" style="max-width: 1000px; margin: 0 auto; display: flex; justify-content: center; align-items: center; position: relative; z-index: 2;">
            <div style="text-align: center; width: 100%;">
                <div style="color: #FFFFFF; font-weight: 700; font-size: 16px; letter-spacing: 4px; margin-bottom: 20px; text-transform: uppercase;">{eyebrow}</div>
                <h1 class="hero-title" style="color: #FFFFFF; font-size: clamp(50px, 6vw, 80px); line-height: 1.1; letter-spacing: -2px; margin-bottom: 30px; text-shadow: 0 4px 12px rgba(0,0,0,0.5);">
                    {title}
                </h1>
                <p style="color: rgba(255,255,255,0.95); font-size: clamp(16px, 2vw, 20px); line-height: 1.6; margin-bottom: 40px; font-weight: 500;">
                    {date_text}
                </p>
                <a href="javascript:void(0);" onclick="document.getElementById('waitlistModal').style.display='flex';" class="btn" style="background-color: #FFFFFF; border: none; color: #1A1A1A; font-weight: 800; padding: 18px 45px; border-radius: 30px; display: inline-block;">
                    {btn_text}
                </a>
            </div>
        </div>
    </section>"""

    if re.search(regex, content, re.DOTALL):
        content = re.sub(regex, new_html, content, flags=re.DOTALL)
        with open(filepath, "w") as f:
            f.write(content)
        print(f"Updated Hero centered layout in {filepath}")
    else:
        print(f"Hero section not found in {filepath}")

update_hero_centered(files[0], False)
update_hero_centered(files[1], True)
