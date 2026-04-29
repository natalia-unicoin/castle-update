import re

with open('index_es.html', 'r', encoding='utf-8') as f:
    html = f.read()

replacements = {
    # Bento Grid
    "Women were<br>Taught to Save,<br>not to Build<br>Riqueza.": "A las Mujeres se les<br>Enseñó a Ahorrar,<br>no a Construir<br>Riqueza.",
    "This is not about": "Esto no se trata de",
    "Managing Money": "Gestionar Dinero",
    "This is about": "Esto se trata de",
    "Owning your Future": "Ser Dueña de tu Futuro",

    # Ecosystem Stack
    "Castle <span style=\"font-family: 'Caveat', cursive; font-weight: 700; font-size: 1.4em; line-height: 0.8; display: inline-block; color: #A03FA3; margin: 0 15px;\">Changes</span> that": "Castle <span style=\"font-family: 'Caveat', cursive; font-weight: 700; font-size: 1.4em; line-height: 0.8; display: inline-block; color: #A03FA3; margin: 0 15px;\">Cambia</span> eso",
    "Castle is an AI-first, Web3-powered ecosystem designed to help you think differently, act differently, and build real Riqueza.": "Castle es un ecosistema impulsado por Web3 y enfocado en IA diseñado para ayudarte a pensar diferente, actuar diferente y construir Riqueza real.",

    # Pillars
    "Cohort<br>Learning": "Aprendizaje en<br>Cohortes",
    "Account<br>Aggregation": "Agregación<br>de Cuentas",
    "AI Money &amp;<br>Wealth Coach": "Coach de<br>Riqueza e IA",
    "AI Money &<br>Wealth Coach": "Coach de<br>Riqueza e IA",
    "Investment<br>Marketplace": "Mercado de<br>Inversiones",
    "Social Wealth<br>Building": "Riqueza<br>Social",

    # Partners
    "Your Influence Into Ownership": "Tu Influencia es Propiedad",
    "Join the movement helping Women build Wealth &mdash; and own a piece of the future you help create.": "Unite al movimiento que ayuda a las Mujeres a construir Riqueza &mdash; y sé dueña de una parte del futuro que ayudás a crear.",
    "Influencers<br>&amp; Celebrities": "Influencers y<br>Celebridades",
    "Influencers<br>& Celebrities": "Influencers y<br>Celebridades",
    "Use your voice and audience to inspire Women worldwide while earning tokens, revenue share, and legacy-building impact.": "Usá tu voz y audiencia para inspirar a Mujeres en todo el mundo mientras ganás tokens, participación en los ingresos e impacto que construye legado.",
    "Content<br>Creators": "Creadoras de<br>Contenido",
    "Turn your knowledge into courses, content, masterclasses, and experiences—monetized through tokens and shared growth.": "Convertí tu conocimiento en cursos, contenido, masterclasses y experiencias—monetizadas a través de tokens y crecimiento compartido.",
    "Brands<br>&amp; Companies": "Marcas y<br>Empresas",
    "Brands<br>& Companies": "Marcas y<br>Empresas",
    "Contribute reach, resources, media, products, or sponsorships and participate in a purpose-driven ecosystem with measurable impact.": "Aportá alcance, recursos, medios, productos o patrocinios y participá en un ecosistema impulsado por un propósito con impacto medible.",
    "Women's<br>Organizations": "Organizaciones<br>de Mujeres",
    "Activate your members with tools for Wealth creation while receiving tokens, incentives, and Community upside.": "Activá a tus miembros con herramientas para la creación de Riqueza mientras recibís tokens, incentivos y beneficios de la Comunidad.",
    "Experts<br>&amp; Coaches": "Expertas y<br>Coaches",
    "Experts<br>& Coaches": "Expertas y<br>Coaches",
    "Tokenize your expertise, programs, mentorship, and credibility as part of a global platform empowering Women financially.": "Tokenizá tu experiencia, programas, mentorías y credibilidad como parte de una plataforma global que empodera financieramente a las Mujeres.",
    "Build Impact. Earn Ownership. Grow With Castle.": "Generá Impacto. Ganá Propiedad. Crecé con Castle.",
    "JOIN THE MOVEMENT": "UNITE AL MOVIMIENTO",

    # Blog
    "Castle in the Media": "Castle en los Medios",
    "VIEW ALL MEDIA": "VER TODOS LOS MEDIOS",

    # Footer
    "Explore": "Explorar",
    "Approach": "Enfoque",
    "Network": "Red",
    "We Are Castle": "Somos Castle",
    "We are Castle": "Somos Castle",
    "Blog": "Blog",
    "Legal": "Legal",
    "Privacy Policy": "Política de Privacidad",
    "Terms of Service": "Términos de Servicio",
    "Cookie Policy": "Política de Cookies",
    "All rights reserved.": "Todos los derechos reservados."
}

for old, new in replacements.items():
    html = html.replace(old, new)

with open('index_es.html', 'w', encoding='utf-8') as f:
    f.write(html)
