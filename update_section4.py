import re

def update_section4(filepath, is_es):
    with open(filepath, "r") as f:
        content = f.read()

    # Old regex to find Section 4
    regex = r'<!-- 4\. The Value -->.*?</section>'
    
    if is_es:
        title = "Dentro de la Masterclass de Castle vas a:"
        t1 = "Reprogramar tu mentalidad<br><span style='font-size: 16px; font-weight: 400;'>sobre el dinero y la abundancia.</span>"
        t2 = "Construir una confianza<br><span style='font-size: 16px; font-weight: 400;'>financiera inquebrantable.</span>"
        t3 = "Aprender a identificar<br><span style='font-size: 16px; font-weight: 400;'>y actuar sobre oportunidades.</span>"
        t4 = "Convertirte en la versión<br><span style='font-size: 16px; font-weight: 400;'>financiera poderosa que mereces ser.</span>"
    else:
        title = "Inside the Castle Masterclass, you will:"
        t1 = "Rewire your mindset<br><span style='font-size: 16px; font-weight: 400;'>around money and abundance.</span>"
        t2 = "Build unshakable<br><span style='font-size: 16px; font-weight: 400;'>financial confidence.</span>"
        t3 = "Learn to identify<br><span style='font-size: 16px; font-weight: 400;'>and act on wealth opportunities.</span>"
        t4 = "Step into the powerful<br><span style='font-size: 16px; font-weight: 400;'>financial identity you were meant to have.</span>"

    new_html = f"""<!-- 4. The Value -->
    <section class="snap-section" style="background-color: #FFFFFF; padding: 120px 4vw;">
        <div class="color-reveal" style="width: 100%; max-width: 1400px; margin: 0 auto; text-align: center;">
            
            <h2 class="section-heading color-reveal" style="font-size: clamp(36px, 4vw, 56px); margin-bottom: 50px;">
                {title}
            </h2>
            
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 10px; margin-bottom: 0;">
                <!-- Box 1 -->
                <div style="aspect-ratio: 3/4; position: relative; border-radius: 5px; overflow: hidden; background-color: #E5E7EB; display: flex; flex-direction: column; justify-content: flex-start; padding: 30px 20px; transition: transform 0.3s;">
                    <div style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; background: linear-gradient(to bottom, rgba(0,0,0,0.85) 0%, rgba(0,0,0,0) 60%); z-index: 1;"></div>
                    <div style="position: relative; z-index: 2; text-align: center; color: #FFFFFF;">
                        <span style="display: block; font-family: 'Inter', sans-serif; font-size: clamp(20px, 2.5vw, 24px); font-weight: 700; line-height: 1.3; margin-bottom: 8px;">{t1}</span>
                    </div>
                    <div style="position: absolute; bottom: 10px; left: 10px; z-index: 1; color: #9CA3AF;">[Image 1]</div>
                </div>
                
                <!-- Box 2 -->
                <div style="aspect-ratio: 3/4; position: relative; border-radius: 5px; overflow: hidden; background-color: #E5E7EB; display: flex; flex-direction: column; justify-content: flex-start; padding: 30px 20px; transition: transform 0.3s;">
                    <div style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; background: linear-gradient(to bottom, rgba(0,0,0,0.85) 0%, rgba(0,0,0,0) 60%); z-index: 1;"></div>
                    <div style="position: relative; z-index: 2; text-align: center; color: #FFFFFF;">
                        <span style="display: block; font-family: 'Inter', sans-serif; font-size: clamp(20px, 2.5vw, 24px); font-weight: 700; line-height: 1.3; margin-bottom: 8px;">{t2}</span>
                    </div>
                    <div style="position: absolute; bottom: 10px; left: 10px; z-index: 1; color: #9CA3AF;">[Image 2]</div>
                </div>
                
                <!-- Box 3 -->
                <div style="aspect-ratio: 3/4; position: relative; border-radius: 5px; overflow: hidden; background-color: #E5E7EB; display: flex; flex-direction: column; justify-content: flex-start; padding: 30px 20px; transition: transform 0.3s;">
                    <div style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; background: linear-gradient(to bottom, rgba(0,0,0,0.85) 0%, rgba(0,0,0,0) 60%); z-index: 1;"></div>
                    <div style="position: relative; z-index: 2; text-align: center; color: #FFFFFF;">
                        <span style="display: block; font-family: 'Inter', sans-serif; font-size: clamp(20px, 2.5vw, 24px); font-weight: 700; line-height: 1.3; margin-bottom: 8px;">{t3}</span>
                    </div>
                    <div style="position: absolute; bottom: 10px; left: 10px; z-index: 1; color: #9CA3AF;">[Image 3]</div>
                </div>
                
                <!-- Box 4 -->
                <div style="aspect-ratio: 3/4; position: relative; border-radius: 5px; overflow: hidden; background-color: #E5E7EB; display: flex; flex-direction: column; justify-content: flex-start; padding: 30px 20px; transition: transform 0.3s;">
                    <div style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; background: linear-gradient(to bottom, rgba(0,0,0,0.85) 0%, rgba(0,0,0,0) 60%); z-index: 1;"></div>
                    <div style="position: relative; z-index: 2; text-align: center; color: #FFFFFF;">
                        <span style="display: block; font-family: 'Inter', sans-serif; font-size: clamp(20px, 2.5vw, 24px); font-weight: 700; line-height: 1.3; margin-bottom: 8px;">{t4}</span>
                    </div>
                    <div style="position: absolute; bottom: 10px; left: 10px; z-index: 1; color: #9CA3AF;">[Image 4]</div>
                </div>
            </div>
        </div>
    </section>"""

    if re.search(regex, content, re.DOTALL):
        content = re.sub(regex, new_html, content, flags=re.DOTALL)
        with open(filepath, "w") as f:
            f.write(content)
        print(f"Updated Section 4 in {filepath}")
    else:
        print(f"Regex failed for {filepath}")

update_section4("/Users/Nati/.gemini/antigravity/scratch/Castle_V3_Standalone/masterclass_es.html", True)
update_section4("/Users/Nati/.gemini/antigravity/scratch/Castle_V3_Standalone/masterclass.html", False)
