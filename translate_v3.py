import re

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

replacements = {
    # Title & Meta
    '<title>CASTLE &middot; Own Your <span style="color: #A03FA3;">Wealth.</span> Own Your <span style="color: #A03FA3;">Future.</span></title>': '<title>CASTLE &middot; Sé dueña de tu <span style="color: #A03FA3;">Dinero.</span> Sé dueña de tu <span style="color: #A03FA3;">Futuro.</span></title>',
    'content="CASTLE &middot; Own Your <span style="color: #A03FA3;">Wealth.</span> Own Your <span style="color: #A03FA3;">Future.</span>"': 'content="CASTLE &middot; Sé dueña de tu <span style="color: #A03FA3;">Dinero.</span> Sé dueña de tu <span style="color: #A03FA3;">Futuro.</span>"',
    'content="The AI-powered platform helping Women build Wealth, invest with confidence, and earn rewards for financial progress."': 'content="La plataforma impulsada por IA que ayuda a las Mujeres a construir Riqueza, invertir con confianza y ganar recompensas por el progreso financiero."',

    # Navigation
    '>We are Castle</a>': '>Somos Castle</a>',
    '>MasterClass</a>': '>MasterClass</a>',
    '>Partners</a>': '>Socios</a>',
    '>Contact Us</a>': '>Contáctanos</a>',
    '<!-- Blank for clean look -->': '''<select class="lang-select" onchange="if(this.value) window.location.href=this.value" style="color: #1A1A1A; border: 1px solid #E5E7EB; padding: 4px 8px; border-radius: 4px;">
                <option value="index.html">ENG</option>
                <option value="index_es.html" selected>ESP</option>
            </select>''',

    # Hero
    'Own Your <span style="color: #A03FA3;">Wealth.</span><br>Own Your <span style="color: #A03FA3;">Future.</span>': 'Ser dueña de tu <span style="color: #A03FA3;">dinero,</span><br>es ser dueña de tu <span style="color: #A03FA3;">futuro.</span>',
    'Castle gives you the Training, AI Tools, Intelligence and Community to take Control of your Money and start building Real Wealth.': 'Castle te da la Capacitación, Herramientas de IA, Inteligencia y Comunidad para tomar el Control de tu Dinero y comenzar a construir Riqueza Real.',
    '>JOIN THE WAITLIST</a>': '>ÚNETE A LA LISTA DE ESPERA</a>',

    # Bento 2
    'Women were<br>Taught to Save,<br>not to Build<br>Wealth.': 'A las mujeres<br>se les enseñó a ahorrar,<br>no a construir<br>riqueza.',
    'This is not about': 'Esto no se trata de',
    'Managing Money': 'Administrar Dinero',
    'This is about': 'Esto se trata de',
    'Owning your Future': 'Ser Dueña de tu Futuro',

    # 2.5 Ecosystem
    '>Changes</span> that': '>Cambia</span> eso',
    'Castle is an AI-first, Web3-powered ecosystem designed to help you think differently, act differently, and build real Wealth.': 'Castle es un ecosistema impulsado por IA y Web3 diseñado para ayudarte a pensar diferente, actuar diferente y construir verdadera Riqueza.',

    # What Makes Us Different
    'The Castle way': 'El estilo Castle',
    'Castle is where your Relationship with Money changes&mdash;for Real.': 'Castle es donde tu Relación con el Dinero cambia&mdash;de verdad.',
    'Not another personal finance course. Not another app telling you to budget better. Not another place where finance feels complicated, intimidating, or not made for you.': 'No es otro curso de finanzas personales. No es otra app que te dice que presupuestes mejor. No es otro lugar donde las finanzas se sienten complicadas, intimidantes o no hechas para ti.',
    '>Rewiring</span>': '>Reprogramación</span>',
    '>to break limiting beliefs</span>': '>para romper creencias limitantes</span>',
    '>Coaching</span>': '>Coaching</span>',
    '>to support your decisions</span>': '>para apoyar tus decisiones</span>',
    '>Smart Tools</span>': '>Herramientas Inteligentes</span>',
    '>to grow with confidence</span>': '>para crecer con confianza</span>',
    '>A Powerful Community</span>': '>Una Comunidad Poderosa</span>',
    '>of women rising together</span>': '>de mujeres creciendo juntas</span>',

    # Core Pillars
    'Built To Transform Every Dimension<br>Of Your <span style="color: #A03FA3;">Wealth.</span>': 'Construido para Transformar Cada Dimensión<br>de tu <span style="color: #A03FA3;">Riqueza.</span>',
    'Built on Five Core Pillars, giving you the framework to build real financial independence.': 'Construido sobre Cinco Pilares Fundamentales, dándote el marco para construir independencia financiera real.',
    'With an AI Financial Coach, guided challenges, and a Powerful Community, you don&rsquo;t just Learn about Money &mdash; you Transform your Mindset, Build Confidence, and start Seeing Opportunities where you once Saw Risk.': 'Con un Coach Financiero de IA, retos guiados y una Comunidad Poderosa, no solo Aprendes sobre Dinero &mdash; Transformas tu Mentalidad, Construyes Confianza y comienzas a Ver Oportunidades donde antes Veías Riesgo.',
    'Cohort<br>Learning': 'Aprendizaje<br>en Cohorte',
    'Account<br>Aggregation': 'Agregación<br>de Cuentas',
    'AI Money &<br>Wealth Coach': 'Coach de IA<br>Financiero',
    'Investment<br>Marketplace': 'Mercado de<br>Inversión',
    'Social Wealth<br>Building': 'Construcción de<br>Riqueza Social',

    # Challenge Teaser
    'The Castle Wealth Reset<br>&amp; Rewire Challenge™': 'El Reto Castle de Reseteo<br>&amp; Reprogramación Financiera™',
    'A focused 21 days sprint designed to rewire your financial habits and help you build your first intelligent portfolio alongside thousands of other driven Women.': 'Un sprint enfocado de 21 días diseñado para reprogramar tus hábitos financieros y ayudarte a construir tu primer portafolio inteligente junto a miles de mujeres determinadas.',

    # Partners Top
    'Your Influence Into Ownership': 'Tu Influencia en Propiedad',
    'Join the movement helping Women build Wealth &mdash; and own a piece of the future you help create.': 'Únete al movimiento que ayuda a las Mujeres a construir Riqueza &mdash; y sé dueña de una parte del futuro que ayudas a crear.',
    'Castle is building a new Web3-powered ecosystem where creators, leaders, brands, and Communities can tokenize their expertise, audience, reach, credibility, and resources in exchange for Castle tokens and shared upside.': 'Castle está construyendo un ecosistema impulsado por Web3 donde creadores, líderes, marcas y Comunidades pueden tokenizar su experiencia, audiencia, alcance, credibilidad y recursos a cambio de tokens de Castle y beneficios compartidos.',
    'Castle offers a model of co-creation, co-ownership, and long-term value creation.': 'Castle ofrece un modelo de co-creación, co-propiedad y creación de valor a largo plazo.',
    'Bring what makes you powerful&mdash;your voice, network, platform, or Community&mdash;and grow with us as we scale a global movement for Women and Wealth.': 'Aporta lo que te hace poderosa&mdash;tu voz, red, plataforma o Comunidad&mdash;y crece con nosotras mientras escalamos un movimiento global para las Mujeres y la Riqueza.',

    # Partners Grid
    '>How You Can Partner?</h2>': '>¿Cómo Puedes Asociarte?</h2>',
    'Whether you are a Celebrity, Influencer, Content Creator, Brand, Women&rsquo;s Organization, or Expert &mdash;<br>you can join us to transform how Women experience Wealth<br>and be part of the Women&rsquo;s Wealth Revolution.': 'Ya seas una Celebridad, Influencer, Creadora de Contenido, Marca, Organización o Experta &mdash;<br>puedes unirte a nosotras para transformar cómo las Mujeres experimentan la Riqueza<br>y ser parte de la Revolución de la Riqueza Femenina.',
    'Influencers<br>& Celebrities': 'Influencers<br>& Celebridades',
    'Use your voice and audience to inspire Women worldwide while earning tokens, revenue share, and legacy-building impact.': 'Usa tu voz y audiencia para inspirar a Mujeres de todo el mundo mientras ganas tokens, participación en los ingresos e impacto en la construcción de un legado.',
    'Content<br>Creators': 'Creadoras<br>de Contenido',
    'Turn your knowledge into courses, content, masterclasses, and experiences—monetized through tokens and shared growth.': 'Convierte tus conocimientos en cursos, contenido, masterclasses y experiencias—monetizados mediante tokens y crecimiento compartido.',
    'Brands<br>& Companies': 'Marcas<br>& Compañías',
    'Contribute reach, resources, media, products, or sponsorships and participate in a purpose-driven ecosystem with measurable impact.': 'Aporta alcance, recursos, medios, productos o patrocinios y participa en un ecosistema con un propósito claro e impacto medible.',
    'Women\'s<br>Organizations': 'Organizaciones<br>de Mujeres',
    'Activate your members with tools for Wealth creation while receiving tokens, incentives, and Community upside.': 'Activa a tus miembros con herramientas para la creación de Riqueza mientras recibes tokens, incentivos y beneficios para la Comunidad.',
    'Experts<br>& Coaches': 'Expertas<br>& Coaches',
    'Tokenize your expertise, programs, mentorship, and credibility as part of a global platform empowering Women financially.': 'Tokeniza tu experiencia, programas, mentoría y credibilidad como parte de una plataforma global que empodera financieramente a las Mujeres.',
    'Build Impact. Earn Ownership. Grow With Castle.': 'Crea Impacto. Gana Propiedad. Crece con Castle.',
    '>JOIN THE MOVEMENT</a>': '>ÚNETE AL MOVIMIENTO</a>',

    # Blog
    '>Castle in the Media</h2>': '>Castle en los Medios</h2>',
    'Explore the insights, announcements, and perspectives shaping the Future of Women\'s Wealth.': 'Explora las ideas, anuncios y perspectivas que dan forma al Futuro de la Riqueza de las Mujeres.',
    'Across the world, the story of Castle is unfolding &mdash; redefining Financial Ownership for Women and building a new model for Wealth Creation.': 'En todo el mundo, la historia de Castle se está desarrollando &mdash; redefiniendo la Propiedad Financiera para las Mujeres y construyendo un nuevo modelo para la Creación de Riqueza.',
    '>Global Leadership</span>': '>Liderazgo Global</span>',
    'Build Your Own Castle: Silvina Moschini on Women & Money': 'Construye tu Propio Castillo: Silvina Moschini sobre las Mujeres y el Dinero',
    'Explore how Women are leading the charge in Wealth creation and reshaping the financial ecosystem in the Gulf region.': 'Explora cómo las Mujeres están liderando la creación de Riqueza y remodelando el ecosistema financiero en la región del Golfo.',
    '>Press</span>': '>Prensa</span>',
    'Crypto Is Not The Gap, The Gap Is Education': 'Las Criptomonedas No Son la Brecha, la Brecha es la Educación',
    'Understanding the shifting landscape of cryptocurrency and how education is key to navigating the future.': 'Comprendiendo el panorama cambiante de las criptomonedas y cómo la educación es clave para navegar por el futuro.',
    '>Innovation</span>': '>Innovación</span>',
    'From Entrepreneurs to Investors': 'De Emprendedoras a Inversoras',
    'A deep dive into the technological leap creating new female fortunes in Latin America.': 'Una mirada profunda al salto tecnológico que está creando nuevas fortunas femeninas en América Latina.',
    '>VIEW ALL MEDIA</a>': '>VER TODOS LOS MEDIOS</a>',

    # Newsletter
    '>Subscribe to our Newsletter</h3>': '>Suscríbete a nuestro Boletín</h3>',
    'Join the movement. Get the latest insights on Wealth building and investments sent straight to your inbox.': 'Únete al movimiento. Recibe las últimas perspectivas sobre construcción de Riqueza e inversiones directamente en tu correo.',
    'placeholder="Enter your email"': 'placeholder="Ingresa tu correo"',
    '>SUBSCRIBE</button>': '>SUSCRIBIRSE</button>',
    'alert(\'Subscribed to Newsletter!\');': 'alert(\'¡Suscrito al Boletín!\');',

    # Footer
    'Castle Is The OS Of Women\'s <span style="color: #A03FA3;">Wealth.</span>': 'Castle Es El SO De La <span style="color: #A03FA3;">Riqueza</span> Femenina.',
    '>Explore</h4>': '>Explorar</h4>',
    '>Approach</a>': '>Enfoque</a>',
    '>Network</a>': '>Red</a>',
    '>We are Castle</h4>': '>Somos Castle</h4>',
    '>We Are Castle</a>': '>Somos Castle</a>',
    '>Blog</a>': '>Blog</a>',
    '>Legal</h4>': '>Legal</h4>',
    '>Privacy Policy</a>': '>Política de Privacidad</a>',
    '>Terms of Service</a>': '>Términos de Servicio</a>',
    '>Cookie Policy</a>': '>Política de Cookies</a>',
    'All rights reserved.': 'Todos los derechos reservados.',

    # Waitlist Modal
    '>Join the Waitlist</h2>': '>Únete a la Lista de Espera</h2>',
    'Take control of your financial future. Join the Women-led Wealth revolution.': 'Toma el control de tu futuro financiero. Únete a la revolución de Riqueza liderada por Mujeres.',
    '>Full Name *</label>': '>Nombre Completo *</label>',
    '>Email Address *</label>': '>Correo Electrónico *</label>',
    '>Phone Number</label>': '>Número de Teléfono</label>',
    '>Age</label>': '>Edad</label>',
    '>Country</label>': '>País</label>',
    '>Select your country</option>': '>Selecciona tu país</option>',
    '>United States</option>': '>Estados Unidos</option>',
    '>United Kingdom</option>': '>Reino Unido</option>',
    '>Canada</option>': '>Canadá</option>',
    '>Australia</option>': '>Australia</option>',
    '>Argentina</option>': '>Argentina</option>',
    '>Brazil</option>': '>Brasil</option>',
    '>Chile</option>': '>Chile</option>',
    '>Colombia</option>': '>Colombia</option>',
    '>Mexico</option>': '>México</option>',
    '>Peru</option>': '>Perú</option>',
    '>Spain</option>': '>España</option>',
    '>Other</option>': '>Otro</option>',
    '>LinkedIn URL</label>': '>URL de LinkedIn</label>',
    '>Company / Organization</label>': '>Empresa / Organización</label>',
    '>Your Role / Title</label>': '>Tu Rol / Cargo</label>',
    '>Instagram Handle</label>': '>Usuario de Instagram</label>',
    '>I consent to Castle contacting me to share updates about the platform, launch information, and Community events.</label>': '>Doy mi consentimiento para que Castle me contacte para compartir actualizaciones sobre la plataforma, información de lanzamiento y eventos de la Comunidad.</label>',
    '>Apply for Waitlist</button>': '>Aplicar a la Lista de Espera</button>'
}

for k, v in replacements.items():
    if k not in content:
        print(f"WARNING: Key not found: {k}")
    content = content.replace(k, v)

with open("index_es.html", "w", encoding="utf-8") as f:
    f.write(content)

print("Translation completed. Saved to index_es.html")
