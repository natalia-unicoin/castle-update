import re

def rewrite_resources(filepath, is_spanish):
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    if is_spanish:
        title = "Explora Castle"
        subtitle = "Descubre todo lo que nuestro ecosistema tiene para ofrecerte."
        btn1 = "VER AHORA →"
        btn2 = "SER PARTNER →"
        btn3 = "LEER MÁS →"
        desc1 = "Aprende los fundamentos para tomar control de tu riqueza y construir tu portafolio."
        desc2 = "Únete como creadora, influencer o marca para co-crear valor en la Web3."
        desc3 = "Conoce la visión de Castle y por qué estamos construyendo el futuro de la riqueza."
        hist_title = "Nuestra Historia"
    else:
        title = "Explore Castle"
        subtitle = "Discover everything our ecosystem has to offer."
        btn1 = "WATCH NOW →"
        btn2 = "BECOME PARTNER →"
        btn3 = "READ MORE →"
        desc1 = "Learn the fundamentals to take control of your wealth and build your portfolio."
        desc2 = "Join as a creator, influencer, or brand to co-create value in Web3."
        desc3 = "Learn about Castle's vision and why we are building the future of wealth."
        hist_title = "Our Story"

    new_section = f"""<!-- Quick Resources -->
<section style="background-color: #1A1A1A; padding: var(--section-pad-y) 4vw;">
    <div class="container" style="max-width: 1400px; margin: 0 auto;">
        <div style="text-align: center; margin-bottom: 60px;">
            <h2 class="section-title" style="margin-bottom: 10px; padding: 0; color: #FFFFFF;">{title}</h2>
            <p class="section-subtitle" style="padding: 0; max-width: 600px; margin: 0 auto; color: rgba(255,255,255,0.8);">{subtitle}</p>
        </div>

        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 16px;">
            <!-- Card 1 -->
            <a href="masterclass{'_es' if is_spanish else ''}.html" class="pillar-card" style="text-decoration: none; display: block; position: relative; overflow: hidden; border-radius: 8px; transition: transform 0.3s; box-shadow: 0 4px 20px rgba(0,0,0,0.2);">
                <img src="./public/images/common/hero-silvina.jpg" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; object-fit: cover; z-index: 1;">
                <div style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; background: linear-gradient(to top, rgba(0,0,0,0.95) 0%, rgba(0,0,0,0.2) 60%); z-index: 2;"></div>
                <div style="position: relative; z-index: 3; height: 100%; display: flex; flex-direction: column; justify-content: flex-end; padding: 30px;">
                    <div style="width: 48px; height: 48px; border-radius: 8px; background: rgba(160,63,163,0.3); color: #FFFFFF; display: flex; align-items: center; justify-content: center; margin-bottom: 24px; backdrop-filter: blur(5px);">
                        <svg width="24" height="24" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M14.752 11.168l-3.197-2.132A1 1 0 0010 9.87v4.263a1 1 0 001.555.832l3.197-2.132a1 1 0 000-1.664z"></path><path stroke-linecap="round" stroke-linejoin="round" d="M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
                    </div>
                    <h3 style="font-size: 24px; font-weight: 800; color: #FFFFFF; margin-bottom: 12px; line-height: 1.2;">MasterClass</h3>
                    <p style="font-size: 16px; color: rgba(255,255,255,0.85); line-height: 1.5; margin-bottom: 24px;">{desc1}</p>
                    <span style="font-size: 14px; font-weight: 700; color: #FFFFFF; text-transform: uppercase; letter-spacing: 1px;">{btn1}</span>
                </div>
            </a>

            <!-- Card 2 -->
            <a href="partners{'_es' if is_spanish else ''}.html" class="pillar-card" style="text-decoration: none; display: block; position: relative; overflow: hidden; border-radius: 8px; transition: transform 0.3s; box-shadow: 0 4px 20px rgba(0,0,0,0.2);">
                <img src="./public/images/common/partners.jpg" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; object-fit: cover; z-index: 1;">
                <div style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; background: linear-gradient(to top, rgba(0,0,0,0.95) 0%, rgba(0,0,0,0.2) 60%); z-index: 2;"></div>
                <div style="position: relative; z-index: 3; height: 100%; display: flex; flex-direction: column; justify-content: flex-end; padding: 30px;">
                    <div style="width: 48px; height: 48px; border-radius: 8px; background: rgba(160,63,163,0.3); color: #FFFFFF; display: flex; align-items: center; justify-content: center; margin-bottom: 24px; backdrop-filter: blur(5px);">
                        <svg width="24" height="24" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M12 4v16m8-8H4"></path></svg>
                    </div>
                    <h3 style="font-size: 24px; font-weight: 800; color: #FFFFFF; margin-bottom: 12px; line-height: 1.2;">Partnerships</h3>
                    <p style="font-size: 16px; color: rgba(255,255,255,0.85); line-height: 1.5; margin-bottom: 24px;">{desc2}</p>
                    <span style="font-size: 14px; font-weight: 700; color: #FFFFFF; text-transform: uppercase; letter-spacing: 1px;">{btn2}</span>
                </div>
            </a>

            <!-- Card 3 -->
            <a href="about{'_es' if is_spanish else ''}.html" class="pillar-card" style="text-decoration: none; display: block; position: relative; overflow: hidden; border-radius: 8px; transition: transform 0.3s; box-shadow: 0 4px 20px rgba(0,0,0,0.2);">
                <img src="./public/images/common/mc-bg2.jpg" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; object-fit: cover; z-index: 1;">
                <div style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; background: linear-gradient(to top, rgba(0,0,0,0.95) 0%, rgba(0,0,0,0.2) 60%); z-index: 2;"></div>
                <div style="position: relative; z-index: 3; height: 100%; display: flex; flex-direction: column; justify-content: flex-end; padding: 30px;">
                    <div style="width: 48px; height: 48px; border-radius: 8px; background: rgba(160,63,163,0.3); color: #FFFFFF; display: flex; align-items: center; justify-content: center; margin-bottom: 24px; backdrop-filter: blur(5px);">
                        <svg width="24" height="24" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
                    </div>
                    <h3 style="font-size: 24px; font-weight: 800; color: #FFFFFF; margin-bottom: 12px; line-height: 1.2;">{hist_title}</h3>
                    <p style="font-size: 16px; color: rgba(255,255,255,0.85); line-height: 1.5; margin-bottom: 24px;">{desc3}</p>
                    <span style="font-size: 14px; font-weight: 700; color: #FFFFFF; text-transform: uppercase; letter-spacing: 1px;">{btn3}</span>
                </div>
            </a>
        </div>
    </div>
</section>"""

    # We need to replace the old section.
    # The old section started with <!-- Quick Resources --> and ended before <!-- Newsletter Callout -->
    pattern = re.compile(r'<!-- Quick Resources -->.*?</section>', re.DOTALL)
    
    html = pattern.sub(new_section, html)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)
        print(f"Updated {filepath}")

rewrite_resources('contact_es.html', True)
rewrite_resources('contact.html', False)

