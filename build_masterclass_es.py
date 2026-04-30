import re

file_path = "/Users/Nati/.gemini/antigravity/scratch/Castle_V3_Standalone/masterclass_es.html"
with open(file_path, "r") as f:
    content = f.read()

# Locate the Hero Placeholder
old_regex = r'<!-- Hero Placeholder -->.*?</section>'

new_html = """
    <!-- 1. Hero Section -->
    <section class="hero snap-section" style="background-color: #1A1A1A; display: flex; align-items: center; padding: 150px 4vw 100px 4vw; min-height: 100vh; border-bottom: 1px solid #333; position: relative;">
        <div class="container" style="max-width: 1400px; margin: 0 auto; display: grid; grid-template-columns: repeat(auto-fit, minmax(400px, 1fr)); gap: 60px; align-items: center;">
            <div style="text-align: left;">
                <div style="color: #A03FA3; font-weight: 700; font-size: 16px; letter-spacing: 4px; margin-bottom: 20px; text-transform: uppercase;">Masterclass de 4 días</div>
                <h1 class="hero-title" style="color: #FFFFFF; font-size: clamp(50px, 6vw, 80px); line-height: 1; letter-spacing: -2px; margin-bottom: 30px;">
                    Construye tu Castle.<br><span style="color: #A03FA3;">Sé dueña de tu riqueza.</span>
                </h1>
                <p style="color: rgba(255,255,255,0.8); font-size: clamp(16px, 2vw, 20px); line-height: 1.6; margin-bottom: 40px; font-weight: 500;">
                    1–4 de junio | Organizado por Castle | Impulsado por Unicoin Foundation
                </p>
                <a href="javascript:void(0);" onclick="document.getElementById('waitlistModal').style.display='flex';" class="btn" style="background-color: #A03FA3; border: none; color: #FFFFFF; font-weight: 700; padding: 18px 45px; border-radius: 30px; display: inline-block;">
                    APLICA AHORA
                </a>
            </div>
            <div class="image-placeholder" style="background-color: #2A2A2A; border-radius: 5px; aspect-ratio: 4/3; width: 100%;">
                <span style="color: #555;">[Hero Image / Video]</span>
            </div>
        </div>
    </section>

    <!-- 2. The Hook -->
    <section class="snap-section" style="background-color: #FFFFFF; padding: 120px 4vw;">
        <div class="container" style="max-width: 1200px; margin: 0 auto; display: grid; grid-template-columns: repeat(auto-fit, minmax(400px, 1fr)); gap: 80px; align-items: center;">
            <div class="image-placeholder" style="background-color: #E5E7EB; border-radius: 5px; aspect-ratio: 3/4; width: 100%;">
                <span style="color: #9CA3AF;">[Hook Image]</span>
            </div>
            <div>
                <h2 style="font-size: clamp(36px, 4vw, 56px); font-weight: 800; color: #1A1A1A; line-height: 1.1; margin-bottom: 30px; letter-spacing: -1px; font-family: 'Inter', sans-serif;">
                    ¿Qué pasaría si todo lo que te enseñaron sobre el dinero… <span style="color: #A03FA3;">te estuviera limitando?</span>
                </h2>
                <p style="font-size: clamp(20px, 2.5vw, 26px); color: #2A2A2A; line-height: 1.5; font-weight: 600; margin-bottom: 20px;">
                    Esto no es otra masterclass.
                </p>
                <p style="font-size: clamp(18px, 2vw, 22px); color: #2A2A2A; line-height: 1.6;">
                    Es una transformación de 4 días diseñada para mujeres listas para romper creencias limitantes, tomar el control de sus finanzas y dar el paso hacia la verdadera riqueza.
                </p>
            </div>
        </div>
    </section>

    <!-- 3. The Myths -->
    <section class="snap-section" style="background-color: #F8F8FA; padding: 120px 4vw; text-align: center;">
        <div class="container" style="max-width: 900px; margin: 0 auto;">
            <p style="font-size: clamp(20px, 2vw, 26px); color: #1A1A1A; font-weight: 500; margin-bottom: 40px;">Durante demasiado tiempo te dijeron:</p>
            
            <h2 style="font-size: clamp(40px, 6vw, 70px); font-weight: 800; color: #1A1A1A; line-height: 1.2; letter-spacing: -2px; margin-bottom: 50px; font-family: 'Inter', sans-serif;">
                “No estás lista.”<br>
                “Es demasiado complicado.”<br>
                “La riqueza no es para ti.”
            </h2>
            
            <div style="font-size: clamp(30px, 4vw, 48px); font-weight: 900; color: #A03FA3; letter-spacing: -1px;">
                Eso termina aquí.
            </div>
        </div>
    </section>

    <!-- 4. The Value -->
    <section class="snap-section" style="background-color: #FFFFFF; padding: 120px 4vw;">
        <div class="container" style="max-width: 1400px; margin: 0 auto; display: grid; grid-template-columns: repeat(auto-fit, minmax(400px, 1fr)); gap: 80px; align-items: center;">
            <div>
                <h2 style="font-size: clamp(36px, 4vw, 56px); font-weight: 800; color: #1A1A1A; line-height: 1.1; margin-bottom: 40px; letter-spacing: -1px; font-family: 'Inter', sans-serif;">
                    Dentro de la Masterclass de Castle vas a:
                </h2>
                
                <div style="display: flex; flex-direction: column; gap: 24px;">
                    <div style="display: flex; align-items: flex-start; gap: 20px;">
                        <div style="width: 32px; height: 32px; border-radius: 50%; background-color: #A03FA3; color: white; display: flex; align-items: center; justify-content: center; font-weight: 700; flex-shrink: 0;">1</div>
                        <p style="font-size: 20px; font-weight: 600; color: #1A1A1A; margin: 0; line-height: 1.4;">Reprogramar tu mentalidad sobre el dinero y la abundancia.</p>
                    </div>
                    <div style="display: flex; align-items: flex-start; gap: 20px;">
                        <div style="width: 32px; height: 32px; border-radius: 50%; background-color: #A03FA3; color: white; display: flex; align-items: center; justify-content: center; font-weight: 700; flex-shrink: 0;">2</div>
                        <p style="font-size: 20px; font-weight: 600; color: #1A1A1A; margin: 0; line-height: 1.4;">Construir una confianza financiera inquebrantable.</p>
                    </div>
                    <div style="display: flex; align-items: flex-start; gap: 20px;">
                        <div style="width: 32px; height: 32px; border-radius: 50%; background-color: #A03FA3; color: white; display: flex; align-items: center; justify-content: center; font-weight: 700; flex-shrink: 0;">3</div>
                        <p style="font-size: 20px; font-weight: 600; color: #1A1A1A; margin: 0; line-height: 1.4;">Aprender a identificar y actuar sobre oportunidades de creación de riqueza.</p>
                    </div>
                    <div style="display: flex; align-items: flex-start; gap: 20px;">
                        <div style="width: 32px; height: 32px; border-radius: 50%; background-color: #A03FA3; color: white; display: flex; align-items: center; justify-content: center; font-weight: 700; flex-shrink: 0;">4</div>
                        <p style="font-size: 20px; font-weight: 600; color: #1A1A1A; margin: 0; line-height: 1.4;">Convertirte en la versión financiera poderosa que siempre estuviste destinada a ser.</p>
                    </div>
                </div>
            </div>
            
            <div class="image-placeholder" style="background-color: #E5E7EB; border-radius: 5px; aspect-ratio: 4/3; width: 100%;">
                <span style="color: #9CA3AF;">[Value Image]</span>
            </div>
        </div>
    </section>

    <!-- 5. The Truth -->
    <section class="snap-section" style="background-color: #1A1A1A; padding: 120px 4vw; text-align: center; color: white;">
        <div class="container" style="max-width: 1000px; margin: 0 auto;">
            <p style="font-size: clamp(20px, 2.5vw, 26px); font-weight: 500; margin-bottom: 20px; color: #A03FA3;">Porque la verdad es simple:</p>
            <h2 style="font-size: clamp(36px, 5vw, 64px); font-weight: 800; line-height: 1.2; letter-spacing: -1px; margin-bottom: 0; font-family: 'Inter', sans-serif;">
                Siempre fuiste capaz de construir riqueza.<br>
                Ahora tendrás las herramientas para demostrarlo.
            </h2>
        </div>
    </section>

    <!-- 6. Final CTA -->
    <section class="snap-section" style="background-color: #F8F8FA; padding: 120px 4vw; text-align: center;">
        <div class="container" style="max-width: 800px; margin: 0 auto; display: flex; flex-direction: column; align-items: center;">
            <div style="display: inline-block; padding: 8px 20px; background-color: #1A1A1A; color: white; font-weight: 700; font-size: 14px; letter-spacing: 1px; border-radius: 30px; margin-bottom: 40px; text-transform: uppercase;">
                Experiencia solo por aplicación
            </div>
            
            <h2 style="font-size: clamp(40px, 6vw, 70px); font-weight: 800; color: #1A1A1A; line-height: 1.1; letter-spacing: -2px; margin-bottom: 30px; font-family: 'Inter', sans-serif;">
                Buscamos mujeres listas para crecer, liderar y construir su legado.
            </h2>
            
            <p style="font-size: 24px; color: #A03FA3; font-weight: 700; margin-bottom: 20px;">
                Cupos limitados.
            </p>
            
            <p style="font-size: 20px; color: #2A2A2A; margin-bottom: 50px;">
                Tu futuro financiero no empieza algún día. Empieza ahora.<br>
                Aplica ahora para asegurar tu lugar antes de que se cierren las inscripciones.
            </p>
            
            <a href="javascript:void(0);" onclick="document.getElementById('waitlistModal').style.display='flex';" class="btn" style="background-color: #A03FA3; border: none; color: #FFFFFF; font-weight: 800; padding: 22px 60px; border-radius: 50px; font-size: 16px; letter-spacing: 2px;">
                APLICA AHORA
            </a>
        </div>
    </section>
"""

if re.search(old_regex, content, re.DOTALL):
    content = re.sub(old_regex, new_html, content, flags=re.DOTALL)
    with open(file_path, "w") as f:
        f.write(content)
    print(f"Updated {file_path}")
else:
    print(f"Failed to find placeholder in {file_path}")

