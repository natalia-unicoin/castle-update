import re

files = [
    "/Users/Nati/.gemini/antigravity/scratch/Castle_V3_Standalone/masterclass.html",
    "/Users/Nati/.gemini/antigravity/scratch/Castle_V3_Standalone/masterclass_es.html"
]

def update_hero_layout(filepath, is_es):
    with open(filepath, "r") as f:
        content = f.read()

    # Find the entire Hero section
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
    <section class="hero snap-section" style="background: #A03FA3 url('./public/images/common/masterclass-hero.png') center/cover no-repeat; display: flex; align-items: center; padding: 150px 4vw 100px 4vw; min-height: 100vh; border-bottom: 1px solid #A03FA3; position: relative;">
        <!-- Mobile Overlay to ensure readability -->
        <div style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; background: linear-gradient(to right, rgba(160,63,163,0.3) 0%, rgba(160,63,163,0.8) 100%); z-index: 1;"></div>
        
        <div class="container" style="max-width: 1400px; margin: 0 auto; display: flex; justify-content: flex-end; align-items: center; position: relative; z-index: 2;">
            <div style="text-align: left; max-width: 600px;">
                <div style="color: #FFFFFF; font-weight: 700; font-size: 16px; letter-spacing: 4px; margin-bottom: 20px; text-transform: uppercase;">{eyebrow}</div>
                <h1 class="hero-title" style="color: #FFFFFF; font-size: clamp(50px, 6vw, 80px); line-height: 1; letter-spacing: -2px; margin-bottom: 30px; text-shadow: 0 4px 12px rgba(0,0,0,0.1);">
                    {title}
                </h1>
                <p style="color: rgba(255,255,255,0.9); font-size: clamp(16px, 2vw, 20px); line-height: 1.6; margin-bottom: 40px; font-weight: 500;">
                    {date_text}
                </p>
                <a href="javascript:void(0);" onclick="document.getElementById('waitlistModal').style.display='flex';" class="btn" style="background-color: #FFFFFF; border: none; color: #A03FA3; font-weight: 800; padding: 18px 45px; border-radius: 30px; display: inline-block;">
                    {btn_text}
                </a>
            </div>
        </div>
    </section>"""

    if re.search(regex, content, re.DOTALL):
        content = re.sub(regex, new_html, content, flags=re.DOTALL)
        with open(filepath, "w") as f:
            f.write(content)
        print(f"Updated Hero layout in {filepath}")
    else:
        print(f"Hero section not found in {filepath}")

update_hero_layout(files[0], False)
update_hero_layout(files[1], True)
