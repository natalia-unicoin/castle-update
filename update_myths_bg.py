import re

files = [
    "/Users/Nati/.gemini/antigravity/scratch/Castle_V3_Standalone/masterclass.html",
    "/Users/Nati/.gemini/antigravity/scratch/Castle_V3_Standalone/masterclass_es.html"
]

def update_myths(filepath):
    with open(filepath, "r") as f:
        content = f.read()

    # Find Section 3
    # Look for <!-- 3. The Myths -->
    # Original section starts with <section class="snap-section" style="background-color: #F8F8FA; padding: 120px 4vw; text-align: center;">
    
    # We will replace the entire section.
    regex = r'<!-- 3\. The Myths -->.*?</section>'

    is_es = "es.html" in filepath
    if is_es:
        eyebrow = "Durante demasiado tiempo te dijeron:"
        title1 = "“No estás lista.”"
        title2 = "“Es demasiado complicado.”"
        title3 = "“La riqueza no es para ti.”"
        caveat = "Eso termina aquí."
    else:
        eyebrow = "For too long, you’ve been told:"
        title1 = "“You’re not ready.”"
        title2 = "“It’s too complicated.”"
        title3 = "“Wealth isn’t for you.”"
        caveat = "That ends here."

    new_html = f"""<!-- 3. The Myths -->
    <section class="snap-section" style="background: url('./public/images/common/masterclass-myths-bg.jpg') center/cover no-repeat; position: relative; min-height: 100vh; display: flex; align-items: flex-end; padding: 0 4vw 80px 4vw; text-align: center;">
        <!-- Gradient overlay for readability -->
        <div style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; background: linear-gradient(to top, rgba(0,0,0,0.85) 0%, rgba(0,0,0,0.4) 40%, rgba(0,0,0,0) 100%); z-index: 1;"></div>
        
        <div class="container" style="max-width: 900px; margin: 0 auto; position: relative; z-index: 2;">
            <p style="font-size: clamp(20px, 2vw, 26px); color: rgba(255,255,255,0.9); font-weight: 500; margin-bottom: 30px;">{eyebrow}</p>
            
            <h2 style="font-size: clamp(36px, 5vw, 56px); font-weight: 800; color: #FFFFFF; line-height: 1.2; letter-spacing: -2px; margin-bottom: 40px; font-family: 'Inter', sans-serif;">
                {title1}<br>
                {title2}<br>
                {title3}
            </h2>
            
            <div style="font-family: 'Caveat', cursive; font-size: clamp(60px, 8vw, 90px); font-weight: 700; color: #EABFFF; line-height: 1; margin-top: 20px; text-shadow: 0 4px 20px rgba(0,0,0,0.3);">
                {caveat}
            </div>
        </div>
    </section>"""

    if re.search(regex, content, re.DOTALL):
        content = re.sub(regex, new_html, content, flags=re.DOTALL)
        with open(filepath, "w") as f:
            f.write(content)
        print(f"Updated Myths in {filepath}")
    else:
        print(f"Section not found in {filepath}")

update_myths(files[0])
update_myths(files[1])
