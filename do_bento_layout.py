import re

html_path = '/Users/Nati/.gemini/antigravity/scratch/Castle_V3_Standalone/index.html'

with open(html_path, 'r') as f:
    content = f.read()

# Replace block 2
old_bento_regex = r"<!-- Bento Grid Section 2 -->\s*<section class=\"bento-section\">.*?</section>"

new_bento_html = """<!-- Bento Grid Section 2 -->
    <section class="bento-section" style="padding: 100px 4vw; background-color: #FFFFFF;">
        <div class="bento-container color-reveal" style="max-width: 1400px; margin: 0 auto; display: grid; grid-template-columns: 1fr; gap: 8px;">
            <style>
                @media (min-width: 1024px) {
                    .bento-container {
                        grid-template-columns: 1fr 1fr !important;
                    }
                }
            </style>
            
            <!-- Left Large Card -->
            <div style="background-color: #9A319A; padding: clamp(40px, 6vw, 80px) clamp(30px, 5vw, 60px); color: #FFFFFF; display: flex; flex-direction: column; justify-content: center; min-height: 60vh;">
                <h2 style="font-size: clamp(36px, 5vw, 64px); font-weight: 900; line-height: 1.1; margin-bottom: 25px; letter-spacing: -2px; font-family: 'Inter Tight', sans-serif; color: #FFFFFF; text-wrap: balance;">
                    Women were<br>Taught to Save,<br>not to Build<br>Wealth.
                </h2>
                <div style="margin: 20px 0 40px 0; display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap;">
                    <span style="font-family: 'Caveat', cursive; font-size: clamp(38px, 5vw, 55px); font-weight: 700; color: #FFFFFF; opacity: 0.95;">Castle</span>
                    <span style="font-family: 'Caveat', cursive; font-size: clamp(65px, 9vw, 110px); font-weight: 700; color: #FFFFFF; line-height: 0.7; transform: translateY(5px);">Changes</span>
                    <span style="font-family: 'Caveat', cursive; font-size: clamp(38px, 5vw, 55px); font-weight: 700; color: #FFFFFF; opacity: 0.95;">that.</span>
                </div>
                <p style="font-size: clamp(18px, 2vw, 24px); color: #FFFFFF; font-weight: 400; max-width: 95%; line-height: 1.5; font-family: 'Inter Tight', sans-serif; text-wrap: balance;">
                    <b>Castle</b> is a <b>New Financial</b> Ecosystem where Intelligence Meets Community, and Women Build Real Wealth and Create a Long-Lasting Legacy.
                </p>
            </div>
            
            <!-- Right Column -->
            <div style="display: flex; flex-direction: column; gap: 8px;">
                <!-- Top Right Card -->
                <div style="position: relative; flex: 1; min-height: 35vh; display: flex; flex-direction: column; justify-content: flex-end; align-items: flex-start; padding: clamp(30px, 4vw, 50px); background-color: #1A1A1A; overflow: hidden;">
                    <img src="./public/images/common/step4.jpg" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; object-fit: cover; z-index: 1; opacity: 0.75; transition: transform 0.6s ease;" onmouseover="this.style.transform='scale(1.05)'" onmouseout="this.style.transform='scale(1)'" alt="">
                    <div style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; background: linear-gradient(to top, rgba(0,0,0,0.85) 0%, rgba(0,0,0,0.1) 60%); z-index: 2; pointer-events: none;"></div>
                    <div style="position: relative; z-index: 3;">
                        <div style="font-size: clamp(16px, 1.8vw, 20px); color: #FFFFFF; font-weight: 400; margin-bottom: 2px; font-family: 'Inter Tight', sans-serif;">This is not about</div>
                        <div style="font-size: clamp(28px, 3.5vw, 42px); color: #FFFFFF; font-weight: 800; line-height: 1.1; font-family: 'Inter Tight', sans-serif;">
                            Managing Money <img src="./public/images/common/diamond-white.png" style="height: 0.8em; vertical-align: baseline; margin-left: 2px; opacity: 0.8; filter: hue-rotate(270deg) saturate(200%) brightness(150%);" alt="💎">
                        </div>
                    </div>
                </div>
                <!-- Bottom Right Card -->
                <div style="position: relative; flex: 1; min-height: 35vh; display: flex; flex-direction: column; justify-content: flex-end; align-items: flex-start; padding: clamp(30px, 4vw, 50px); background-color: #1A1A1A; overflow: hidden;">
                    <img src="./public/images/common/step5.jpg" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; object-fit: cover; z-index: 1; opacity: 0.75; transition: transform 0.6s ease;" onmouseover="this.style.transform='scale(1.05)'" onmouseout="this.style.transform='scale(1)'" alt="">
                    <div style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; background: linear-gradient(to top, rgba(0,0,0,0.85) 0%, rgba(0,0,0,0.1) 60%); z-index: 2; pointer-events: none;"></div>
                    <div style="position: relative; z-index: 3;">
                        <div style="font-size: clamp(16px, 1.8vw, 20px); color: #FFFFFF; font-weight: 400; margin-bottom: 2px; font-family: 'Inter Tight', sans-serif;">This is not about</div>
                        <div style="font-size: clamp(28px, 3.5vw, 42px); color: #FFFFFF; font-weight: 800; line-height: 1.1; font-family: 'Inter Tight', sans-serif;">
                            Owning your Future
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>"""

content = re.sub(old_bento_regex, new_bento_html, content, flags=re.DOTALL)

with open(html_path, 'w') as f:
    f.write(content)
print("Updated Block 2 schema")
