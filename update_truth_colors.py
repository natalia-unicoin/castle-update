import re

files = [
    "/Users/Nati/.gemini/antigravity/scratch/Castle_V3_Standalone/masterclass.html",
    "/Users/Nati/.gemini/antigravity/scratch/Castle_V3_Standalone/masterclass_es.html"
]

def generate_truth_html(is_es):
    if is_es:
        small_text = "Porque la verdad es simple:"
        h2 = 'Siempre fuiste capaz de <span style="color: #A03FA3;">construir riqueza.</span><br>Ahora tendrás las <span style="color: #A03FA3;">herramientas</span> para demostrarlo.'
    else:
        small_text = "Because the truth is simple:"
        h2 = 'You were always capable of <span style="color: #A03FA3;">building wealth.</span><br>Now you will have the <span style="color: #A03FA3;">tools</span> to prove it.'

    return f'''<!-- 5. The Truth -->
    <section class="snap-section" style="background-color: #FFFFFF; padding: 120px 4vw; text-align: center;">
        <div class="container" style="max-width: 1300px; margin: 0 auto; display: flex; flex-direction: column; align-items: center; justify-content: center;">
            
            <p style="font-size: clamp(20px, 2.5vw, 26px); font-weight: 500; margin-bottom: 20px; color: #666666;">{small_text}</p>
            
            <h2 style="font-size: clamp(28px, 4vw, 52px); font-weight: 800; color: #1A1A1A; line-height: 1.2; letter-spacing: -1px; margin-bottom: 0; font-family: 'Inter', sans-serif;">
                {h2}
            </h2>
            
        </div>
    </section>'''

for filepath in files:
    is_es = filepath.endswith("_es.html")
    with open(filepath, "r") as f:
        content = f.read()

    # Find the Truth section using regex
    regex = r'<!-- 5\. The Truth -->\s*<section class="snap-section".*?</section>'
    
    new_html = generate_truth_html(is_es)
    
    if re.search(regex, content, re.DOTALL):
        content = re.sub(regex, new_html, content, flags=re.DOTALL)
        with open(filepath, "w") as f:
            f.write(content)
        print(f"Updated Truth colors in {filepath}")
    else:
        print(f"Could not find Truth section in {filepath}")
