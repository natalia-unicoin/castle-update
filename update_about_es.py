import re

with open('about_es.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Font import update
old_font = "@import url('https://fonts.googleapis.com/css2?family=Caveat&family=Inter:wght@400;500;600;700;800;900&family=DM+Sans:wght@400;500;600;700;800;900&display=swap');"
new_font = "@import url('https://fonts.googleapis.com/css2?family=Caveat:wght@400;500;600;700&family=Inter:wght@400;500;600;700;800;900&family=DM+Sans:wght@400;500;600;700;800;900&display=swap');"
if "Caveat:wght" not in content:
    content = content.replace(old_font, new_font)

# 2. Manifesto Intro
manifesto_intro_es = """    <section class="snap-section" style="background-color: #FFFFFF; padding: 100px 4vw 80px 4vw; text-align: center;">
        <div class="container" style="max-width: 1000px; margin: 0 auto;">
            <p style="font-size: 14px; font-weight: 700; letter-spacing: 2px; color: #A03FA3; text-transform: uppercase; margin-bottom: 24px;">Nuestro Manifiesto</p>
            <h2 style="font-size: clamp(36px, 5vw, 56px); font-weight: 800; color: #1A1A1A; line-height: 1.2; letter-spacing: -2px; margin-bottom: 40px; font-family: 'Inter', sans-serif;">
                Por generaciones se nos dijo que fuéramos <span style="font-family: 'Caveat', cursive; font-size: 1.2em; color: #A03FA3; font-weight: 700;">cuidadosas.</span><br>
            </h2>
            <p style="font-size: clamp(18px, 2.5vw, 24px); color: #4B5563; line-height: 1.6; max-width: 800px; margin: 0 auto; font-family: 'Inter', sans-serif; font-weight: 400;">
                Sé modesta con el dinero. Deja que alguien más lo maneje.<br>Pero todo está cambiando.
            </p>
        </div>
    </section>"""
# Replace reality-section with manifesto_intro_es.
# Need to find the existing reality-section block.
reality_match = re.search(r'    <!-- 2\. The Reality -->\s*<section class="reality-section snap-section">.*?</section>', content, re.DOTALL)
if reality_match:
    content = content.replace(reality_match.group(0), "    <!-- 2. The Reality -->\n" + manifesto_intro_es)

# 3. Manifesto Block 2
manifesto_block2_es = """    <!-- Manifesto Block 2 (Hero Style) -->
    <section class="snap-section" style="background-color: #F8F8FA; display: flex; align-items: center; justify-content: center; padding: 20px 4vw; min-height: 100vh; border-bottom: 1px solid #E5E7EB;">
        <div class="container" style="max-width: 1200px; text-align: center;">
            <p style="font-size: clamp(24px, 3.5vw, 40px); font-weight: 600; color: #1A1A1A; line-height: 1.4; margin-bottom: 16px; font-family: 'Inter', sans-serif;">
                En las próximas dos décadas, las mujeres controlarán más de
            </p>
            <h2 style="font-size: clamp(60px, 10vw, 140px); font-weight: 800; color: #A03FA3; letter-spacing: -4px; line-height: 1; margin: 20px 0;">
                $124 billones
            </h2>
            <p style="font-size: clamp(24px, 3.5vw, 40px); font-weight: 600; color: #1A1A1A; line-height: 1.4; margin-bottom: 40px; font-family: 'Inter', sans-serif;">
                más que nunca antes.
            </p>
            
            <div style="max-width: 800px; margin: 0 auto; border-top: 2px solid rgba(160,63,163,0.2); padding-top: 40px;">
                <p style="font-size: clamp(20px, 2.5vw, 28px); color: #4B5563; line-height: 1.6; margin-bottom: 24px; font-weight: 500;">
                    La pregunta no es si las mujeres tendrán dinero.<br>
                    <strong style="color: #1A1A1A;">La pregunta es si serán dueñas de él.</strong>
                </p>
                <p style="font-size: clamp(20px, 2.5vw, 28px); color: #1A1A1A; line-height: 1.6; font-weight: 700; margin-bottom: 10px;">
                    Castle existe para ayudar a las mujeres a construir riqueza.
                </p>
                <p style="font-family: 'Caveat', cursive; font-size: clamp(48px, 6vw, 72px); color: #A03FA3; font-weight: 700; margin: 0;">
                    Juntas.
                </p>
            </div>
        </div>
    </section>"""
# Find existing manifesto-block-2
block2_match = re.search(r'    <!-- Manifesto Block 2 -->.*?</section>', content, re.DOTALL)
if block2_match:
    content = content.replace(block2_match.group(0), manifesto_block2_es)
else:
    # Look for the old version of it
    block2_match = re.search(r'    <section class="snap-section" style="background-color: #A03FA3;.*?</section>', content, re.DOTALL)
    if block2_match:
         content = content.replace(block2_match.group(0), manifesto_block2_es)

# 4. Final CTA (Newsletter) replacing the old "Resources & Contact Section"
final_cta_es = """    <!-- 5. Final CTA / Newsletter -->
    <section class="snap-section" style="background: url('./public/images/common/newsletter-bg.jpg') center/cover no-repeat; position: relative; min-height: 80vh; display: flex; align-items: center; justify-content: center; padding: 80px 4vw;">
        <!-- Dark gradient overlay -->
        <div style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; background: linear-gradient(180deg, rgba(0,0,0,0.2) 0%, rgba(0,0,0,0.8) 100%); z-index: 1;"></div>
        
        <div class="container" style="position: relative; z-index: 2; width: 100%; max-width: 800px; margin: 0 auto; text-align: center;">
            <h2 style="font-size: clamp(36px, 5vw, 56px); font-weight: 800; color: #FFFFFF; line-height: 1.1; letter-spacing: -2px; margin-bottom: 20px; font-family: 'Inter', sans-serif; text-shadow: 0 4px 12px rgba(0,0,0,0.3);">
                Únete al Movimiento.
            </h2>
            <p style="font-size: 20px; color: rgba(255,255,255,0.9); margin-bottom: 40px; font-weight: 500;">
                Suscríbete a nuestro newsletter para recibir perspectivas exclusivas sobre cómo construir riqueza, próximas Masterclasses e invitaciones a eventos.
            </p>
            
            <form action="#" method="POST" style="display: flex; gap: 12px; width: 100%; max-width: 500px; margin: 0 auto; flex-direction: column; @media(min-width: 600px) { flex-direction: row; }">
                <input type="email" placeholder="Ingresa tu correo" required style="flex: 1; padding: 18px 24px; border-radius: 50px; border: none; font-size: 16px; font-family: 'Inter', sans-serif; outline: none; box-shadow: 0 4px 12px rgba(0,0,0,0.1);">
                <button type="submit" style="background-color: #A03FA3; color: #FFFFFF; font-weight: 800; letter-spacing: 2px; padding: 18px 40px; border-radius: 50px; font-size: 14px; border: none; cursor: pointer; text-transform: uppercase; transition: transform 0.2s, background-color 0.2s;">
                    Suscribirse
                </button>
            </form>
        </div>
    </section>"""
contact_match = re.search(r'    <!-- Resources & Contact Section -->.*?</section>', content, re.DOTALL)
if contact_match:
    content = content.replace(contact_match.group(0), final_cta_es)

with open('about_es.html', 'w', encoding='utf-8') as f:
    f.write(content)

