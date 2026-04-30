import re

file_path = "/Users/Nati/.gemini/antigravity/scratch/Castle_V3_Standalone/index_es.html"
with open(file_path, "r") as f:
    content = f.read()

old_section_regex = r'<!-- Challenge Teaser -->\s*<section style="position: relative;.*?Tu futuro financiero<br>empieza con una decisión\..*?ACCEDE A LA MASTERCLASS.*?</a>\s*</div>\s*</section>'

new_section = """<!-- MasterClass Section -->
    <section class="snap-section" style="background-color: #F8F8FA; padding: 100px 4vw;">
        <div class="container" style="max-width: 1200px; margin: 0 auto; text-align: center;">
            
            <h2 class="section-heading color-reveal" style="color: #1A1A1A !important; font-size: clamp(40px, 5vw, 64px) !important; letter-spacing: -2px !important; line-height: 1.1 !important; margin-bottom: 60px;">
                Tu futuro financiero<br>
                <span style="font-family: 'Caveat', cursive; color: #A03FA3; font-weight: 700; font-size: 1.4em; display: inline-block; margin-right: 15px; margin-top: -10px;">Comienza</span> con una decisión.
            </h2>

            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 60px; text-align: left; align-items: center; max-width: 1000px; margin: 0 auto;">
                
                <div style="position: relative; border-radius: 5px; overflow: hidden; aspect-ratio: 4/3; box-shadow: 0 20px 40px rgba(0,0,0,0.1);">
                    <img src="./public/images/common/challenge.png" style="width: 100%; height: 100%; object-fit: cover;" alt="MasterClass">
                </div>

                <div style="padding: 20px 0;">
                    <h3 class="color-reveal" style="font-size: clamp(24px, 3vw, 32px); font-weight: 800; color: #1A1A1A; margin-bottom: 20px; font-family: 'Inter', sans-serif;">Reset Your Money Brain:</h3>
                    <p class="color-reveal" style="font-size: clamp(18px, 2vw, 24px); color: #1A1A1A; font-weight: 600; line-height: 1.4; margin-bottom: 15px; font-family: 'Inter', sans-serif;">Una MasterClass que reprograma tu identidad financiera.</p>
                    <p class="color-reveal" style="font-size: clamp(18px, 2vw, 22px); color: #2A2A2A; line-height: 1.5; margin-bottom: 40px; font-family: 'Inter', sans-serif;">Porque el problema nunca fue el dinero, fue lo que te enseñaron a creer sobre él.</p>
                    
                    <a href="javascript:void(0);" onclick="document.getElementById('waitlistModal').style.display='flex';" class="btn" style="background-color: #A03FA3; border: none; color: #FFFFFF; font-weight: 700; padding: 18px 45px; border-radius: 30px; display: inline-block;">
                        ACCEDE A LA MASTERCLASS
                    </a>
                </div>
            </div>
        </div>
    </section>"""

# Using re.sub to replace
if re.search(old_section_regex, content, re.DOTALL):
    content = re.sub(old_section_regex, new_section, content, flags=re.DOTALL)
    with open(file_path, "w") as f:
        f.write(content)
    print("Replaced successfully")
else:
    print("Regex failed to match")
