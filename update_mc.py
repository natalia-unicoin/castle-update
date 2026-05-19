import re

with open('masterclass_es.html', 'r', encoding='utf-8') as f:
    content = f.read()

replacement = """<!-- Dynamic Content Sections -->
    <!-- Intro Section -->
    <section class="snap-section content-section" style="background-color: #FFFFFF; text-align: center;">
        <div class="container" style="max-width: 1000px; margin: 0 auto;">
            <p style="font-size: clamp(24px, 3vw, 32px); color: #1A1A1A; line-height: 1.6; font-weight: 500;">
                <strong>Castle no es educación financiera tradicional.</strong> Es una transformación de mentalidad, identidad y acción.
            </p>
            <p style="font-size: clamp(20px, 2.5vw, 26px); color: #2A2A2A; line-height: 1.6; margin-top: var(--spacer-40);">
                A través de sesiones en vivo, herramientas de AI, estrategias de inversión y una comunidad de mujeres que están jugando en grande, descubrirás cómo empezar a construir riqueza con más claridad, confianza y visión de largo plazo.
            </p>
        </div>
    </section>

    <!-- What You Will Experience -->
    <section class="snap-section content-section" style="background-color: #F8F8FA; text-align: center;">
        <div class="container" style="max-width: 1400px; margin: 0 auto;">
            <h2 class="section-heading">¿Qué vas a experimentar?</h2>
            
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 20px; margin-top: var(--spacer-50); text-align: left;">
                
                <div style="background: #FFFFFF; padding: 40px 30px; border-radius: 5px; box-shadow: 0 4px 20px rgba(0,0,0,0.03);">
                    <div style="font-size: 24px; color: #A03FA3; margin-bottom: 15px; font-weight: 800; font-family: 'Inter', sans-serif;">01</div>
                    <p style="font-size: 18px; color: #1A1A1A; font-weight: 600; line-height: 1.5; margin: 0;">Cómo dejar atrás la mentalidad de escasez y empezar a pensar como inversionista</p>
                </div>

                <div style="background: #FFFFFF; padding: 40px 30px; border-radius: 5px; box-shadow: 0 4px 20px rgba(0,0,0,0.03);">
                    <div style="font-size: 24px; color: #A03FA3; margin-bottom: 15px; font-weight: 800; font-family: 'Inter', sans-serif;">02</div>
                    <p style="font-size: 18px; color: #1A1A1A; font-weight: 600; line-height: 1.5; margin: 0;">Las nuevas reglas de la riqueza en la era de AI, Web3 y activos digitales</p>
                </div>

                <div style="background: #FFFFFF; padding: 40px 30px; border-radius: 5px; box-shadow: 0 4px 20px rgba(0,0,0,0.03);">
                    <div style="font-size: 24px; color: #A03FA3; margin-bottom: 15px; font-weight: 800; font-family: 'Inter', sans-serif;">03</div>
                    <p style="font-size: 18px; color: #1A1A1A; font-weight: 600; line-height: 1.5; margin: 0;">Cómo transformar tu conocimiento, red y talento en activos con valor</p>
                </div>

                <div style="background: #FFFFFF; padding: 40px 30px; border-radius: 5px; box-shadow: 0 4px 20px rgba(0,0,0,0.03);">
                    <div style="font-size: 24px; color: #A03FA3; margin-bottom: 15px; font-weight: 800; font-family: 'Inter', sans-serif;">04</div>
                    <p style="font-size: 18px; color: #1A1A1A; font-weight: 600; line-height: 1.5; margin: 0;">Estrategias reales para empezar a invertir con intención</p>
                </div>

                <div style="background: #FFFFFF; padding: 40px 30px; border-radius: 5px; box-shadow: 0 4px 20px rgba(0,0,0,0.03);">
                    <div style="font-size: 24px; color: #A03FA3; margin-bottom: 15px; font-weight: 800; font-family: 'Inter', sans-serif;">05</div>
                    <p style="font-size: 18px; color: #1A1A1A; font-weight: 600; line-height: 1.5; margin: 0;">Cómo construir independencia financiera sin hacerlo sola</p>
                </div>

                <div style="background: #FFFFFF; padding: 40px 30px; border-radius: 5px; box-shadow: 0 4px 20px rgba(0,0,0,0.03);">
                    <div style="font-size: 24px; color: #A03FA3; margin-bottom: 15px; font-weight: 800; font-family: 'Inter', sans-serif;">06</div>
                    <p style="font-size: 18px; color: #1A1A1A; font-weight: 600; line-height: 1.5; margin: 0;">El poder de las redes, cohortes y comunidades para acelerar crecimiento y oportunidades</p>
                </div>

            </div>
        </div>
    </section>

    <!-- Who Is This For -->
    <section class="snap-section content-section" style="background-color: #FFFFFF; text-align: center;">
        <div class="container" style="max-width: 900px; margin: 0 auto;">
            <h2 class="section-heading">¿Para quién es esta Masterclass?</h2>
            <p class="section-subtitle" style="margin-bottom: var(--spacer-40);">Para mujeres ambiciosas, curiosas y listas para elevar su juego financiero.</p>
            
            <div style="display: flex; flex-wrap: wrap; justify-content: center; gap: 15px; margin-bottom: var(--spacer-50);">
                <span style="font-size: 18px; font-weight: 800; color: #1A1A1A; background: #F3F4F6; padding: 12px 24px; border-radius: 30px; font-family: 'Inter', sans-serif;">Fundadoras</span>
                <span style="font-size: 18px; font-weight: 800; color: #1A1A1A; background: #F3F4F6; padding: 12px 24px; border-radius: 30px; font-family: 'Inter', sans-serif;">Ejecutivas</span>
                <span style="font-size: 18px; font-weight: 800; color: #1A1A1A; background: #F3F4F6; padding: 12px 24px; border-radius: 30px; font-family: 'Inter', sans-serif;">Creadoras</span>
                <span style="font-size: 18px; font-weight: 800; color: #1A1A1A; background: #F3F4F6; padding: 12px 24px; border-radius: 30px; font-family: 'Inter', sans-serif;">Profesionales</span>
                <span style="font-size: 18px; font-weight: 800; color: #1A1A1A; background: #F3F4F6; padding: 12px 24px; border-radius: 30px; font-family: 'Inter', sans-serif;">Inversionistas</span>
            </div>
            
            <p style="font-size: 20px; color: #A03FA3; font-weight: 700; margin-bottom: var(--spacer-50);">
                O simplemente mujeres que saben que quieren más para su futuro.
            </p>

            <div style="background-color: #FAFAFA; border: 1px solid #E5E7EB; border-radius: 5px; padding: 40px; margin-bottom: var(--spacer-40); text-align: left;">
                <p style="font-size: 18px; color: #1A1A1A; line-height: 1.6; margin-bottom: 20px;"><strong>No necesitas experiencia previa en inversiones.</strong> Solo la decisión de dejar de pensar en pequeño.</p>
                <p style="font-size: 18px; color: #1A1A1A; line-height: 1.6; margin-bottom: 20px;"><strong>Esta no es una masterclass masiva.</strong> Los cupos son limitados y el acceso es únicamente por aplicación.</p>
                <p style="font-size: 18px; color: #1A1A1A; line-height: 1.6; margin-bottom: 0;">Queremos construir una comunidad de mujeres comprometidas con crecer, invertir y construir riqueza juntas.</p>
            </div>
            
            <div style="padding-top: 20px; border-top: 1px solid #F3F4F6;">
                <p style="font-size: 14px; color: #6B7280; line-height: 1.6; margin: 0; max-width: 800px; margin-left: auto; margin-right: auto;">
                    Apoyada por <strong>Unicoin Foundation</strong>, una organización comprometida con democratizar el acceso a la innovación financiera, Web3 y nuevas oportunidades de creación de riqueza para mujeres alrededor del mundo.
                </p>
            </div>
        </div>
    </section>

    <!-- Final CTA -->
    <section class="snap-section" style="position: relative; display: flex; align-items: flex-end; justify-content: center; padding: 0 4vw 8vh 4vw; min-height: 100vh; background-image: url('./public/images/common/mc-bg2.jpg'); background-size: cover; background-position: center top; background-attachment: fixed; background-repeat: no-repeat; margin-top: 0; overflow: hidden;">
        <!-- Gradient Overlay -->
        <div style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; background: linear-gradient(to bottom, rgba(0,0,0,0) 40%, rgba(0,0,0,0.5) 75%, rgba(0,0,0,0.95) 100%); z-index: 1;"></div>
        
        <div style="width: 100%; max-width: 1400px; margin: 0 auto; position: relative; z-index: 2; text-align: center; padding-top: 40vh;">
            <div style="display: inline-block; padding: 8px 20px; background-color: rgba(255,255,255,0.1); border: 1px solid rgba(255,255,255,0.3); color: white; font-weight: 700; font-size: 14px; letter-spacing: 1px; border-radius: 30px; margin-bottom: var(--spacer-30); text-transform: uppercase;">
                Experiencia solo por aplicación
            </div>

            <h2 class="section-heading color-reveal" style="font-size: clamp(32px, 5vw, 64px) !important; letter-spacing: -2px !important; line-height: 0.9 !important; margin-bottom: 20px; color: #FFFFFF !important; text-shadow: 0 4px 30px rgba(0,0,0,0.8), 0 2px 10px rgba(0,0,0,0.6);">
                <span style="display: inline-block; font-family: 'Inter', sans-serif; color: #FFFFFF;">El futuro financiero de las mujeres ya empezó.</span>
            </h2>
            
            <p style="font-size: 24px; color: #FFFFFF; font-weight: 700; margin-bottom: 15px;">
                La pregunta es: ¿vas a observarlo… o vas a construirlo?
            </p>
            
            <p style="font-size: 18px; color: rgba(255,255,255,0.9); margin-bottom: var(--spacer-40); font-weight: 500;">
                Sumate a la generación que redefinirá la riqueza femenina.
            </p>
            
            <a href="javascript:void(0);" onclick="openUnifiedModal('waitlist');" class="btn" style="background-color: #FFFFFF; border: none; color: #1A1A1A; font-weight: 800; padding: 22px 60px; border-radius: 50px; font-size: 16px; letter-spacing: 2px;">
                APLICA
            </a>
        </div>
    </section>
"""

# The sections we want to replace start at "<!-- 4. The Value -->" and go just before "<footer class=\"site-footer\">"
new_content = re.sub(
    r'<!-- 4\. The Value -->.*?(?=<footer class="site-footer">)', 
    replacement + '\n\n    ', 
    content, 
    flags=re.DOTALL
)

with open('masterclass_es.html', 'w', encoding='utf-8') as f:
    f.write(new_content)
