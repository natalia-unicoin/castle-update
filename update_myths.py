import re

files = [
    "/Users/Nati/.gemini/antigravity/scratch/Castle_V3_Standalone/masterclass.html",
    "/Users/Nati/.gemini/antigravity/scratch/Castle_V3_Standalone/masterclass_es.html"
]

def generate_myths_html(is_es):
    if is_es:
        small_text = "Durante demasiado tiempo te dijeron:"
        h2 = "“No estás lista.”<br>\n                “Es demasiado complicado.”<br>\n                “La riqueza no es para ti.”"
        caveat_text = "Eso termina aquí."
    else:
        small_text = "For too long you were told:"
        h2 = "“You are not ready.”<br>\n                “It’s too complicated.”<br>\n                “Wealth is not for you.”"
        caveat_text = "That ends here."

    return f'''<!-- 3. The Myths -->
    <section class="snap-section" style="background-color: #FFFFFF; padding: 40px 4vw 80px 4vw; text-align: center;">
        <div class="container" style="max-width: 900px; margin: 0 auto;">
            <p style="font-size: clamp(20px, 2vw, 26px); color: #4A4A4A; font-weight: 500; margin-bottom: 30px;">{small_text}</p>
            
            <h2 style="font-size: clamp(36px, 5vw, 56px); font-weight: 800; color: #1A1A1A; line-height: 1.2; letter-spacing: -2px; margin-bottom: 40px; font-family: 'Inter', sans-serif;">
                {h2}
            </h2>
            
            <p style="font-family: 'Caveat', cursive; font-size: clamp(48px, 6vw, 72px); color: #A03FA3; margin-top: 20px; transform: rotate(-2deg); display: inline-block;">
                {caveat_text}
            </p>
        </div>
    </section>'''

for filepath in files:
    is_es = filepath.endswith("_es.html")
    with open(filepath, "r") as f:
        content = f.read()

    # Find the Myths section using regex
    regex = r'<!-- 3\. The Myths -->\s*<section class="snap-section".*?</section>'
    
    new_html = generate_myths_html(is_es)
    
    if re.search(regex, content, re.DOTALL):
        content = re.sub(regex, new_html, content, flags=re.DOTALL)
        with open(filepath, "w") as f:
            f.write(content)
        print(f"Updated Myths section in {filepath}")
    else:
        print(f"Could not find Myths section in {filepath}")
