import re
import time

files = [
    "/Users/Nati/.gemini/antigravity/scratch/Castle_V3_Standalone/masterclass.html",
    "/Users/Nati/.gemini/antigravity/scratch/Castle_V3_Standalone/masterclass_es.html"
]

def generate_cta_html(is_es, v):
    if is_es:
        eyebrow = "Experiencia solo por aplicación"
        h2 = "Buscamos mujeres listas para crecer, liderar y construir su legado."
        limit = "Cupos limitados. Accede solo por aplicación."
        desc = "Tu futuro financiero empieza ahora.<br>Aplica ahora y asegura tu lugar antes de que se cierren las inscripciones."
        btn = "APLICA AHORA"
    else:
        eyebrow = "Application-only experience"
        h2 = "We are looking for women ready to grow, lead, and build their legacy."
        limit = "Limited seats. Access by application only."
        desc = "Your financial future starts now.<br>Apply now and secure your spot before doors close."
        btn = "APPLY NOW"

    return f'''<!-- 6. Final CTA -->
    <section class="snap-section" style="background: url('./public/images/common/masterclass-finalcta.jpg?v={v}') center/cover no-repeat; position: relative; min-height: 100vh; display: flex; align-items: flex-end; padding: 0 4vw 80px 4vw; text-align: center;">
        <!-- Dark gradient overlay -->
        <div style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; background: linear-gradient(180deg, rgba(0,0,0,0) 0%, rgba(0,0,0,0.85) 100%); z-index: 1;"></div>
        
        <div class="container" style="position: relative; z-index: 2; width: 100%; max-width: 800px; margin: 0 auto; display: flex; flex-direction: column; align-items: center;">
            <div style="display: inline-block; padding: 8px 20px; background-color: rgba(255,255,255,0.1); border: 1px solid rgba(255,255,255,0.3); color: white; font-weight: 700; font-size: 14px; letter-spacing: 1px; border-radius: 30px; margin-bottom: 30px; text-transform: uppercase;">
                {eyebrow}
            </div>
            
            <h2 style="font-size: clamp(36px, 5vw, 56px); font-weight: 800; color: #FFFFFF; line-height: 1.1; letter-spacing: -2px; margin-bottom: 20px; font-family: 'Inter', sans-serif; text-shadow: 0 4px 12px rgba(0,0,0,0.5);">
                {h2}
            </h2>
            
            <p style="font-size: 24px; color: #FFFFFF; font-weight: 700; margin-bottom: 15px;">
                {limit}
            </p>
            
            <p style="font-size: 18px; color: rgba(255,255,255,0.9); margin-bottom: 40px; font-weight: 500;">
                {desc}
            </p>
            
            <a href="javascript:void(0);" onclick="document.getElementById('waitlistModal').style.display='flex';" class="btn" style="background-color: #FFFFFF; border: none; color: #1A1A1A; font-weight: 800; padding: 22px 60px; border-radius: 50px; font-size: 16px; letter-spacing: 2px;">
                {btn}
            </a>
        </div>
    </section>'''

v = str(int(time.time()))

for filepath in files:
    is_es = filepath.endswith("_es.html")
    with open(filepath, "r") as f:
        content = f.read()

    # Regex to find the entire CTA section
    # Starts with <!-- 6. Final CTA -->
    # Ends with </section>
    regex = r'<!-- 6\. Final CTA -->\s*<section class="snap-section".*?</section>'
    
    new_html = generate_cta_html(is_es, v)
    
    if re.search(regex, content, re.DOTALL):
        content = re.sub(regex, new_html, content, flags=re.DOTALL)
        with open(filepath, "w") as f:
            f.write(content)
        print(f"Updated Final CTA in {filepath}")
    else:
        print(f"Could not find Final CTA section in {filepath}")
