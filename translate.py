import re

with open('index_es.html', 'r', encoding='utf-8') as f:
    html = f.read()

replacements = {
    # Fixes from previous run
    "Suscribirse to our Newsletter": "Suscribite a nuestro Newsletter",
    "Suscribirsed to Newsletter!": "¡Suscrito al Newsletter!",
    ">SUBSCRIBE<": ">SUSCRIBIRSE<",
    "Women and Riqueza": "Mujeres y la Riqueza",
    "Future of Women's Riqueza": "Futuro de la Riqueza Femenina",
    "Castle Is The OS Of Women's <span style=\"color: #A03FA3;\">Riqueza.</span>": "Castle Es El SO De La <span style=\"color: #A03FA3;\">Riqueza Femenina.</span>",
    "Join the movement. Get the latest insights on Wealth building and investments sent straight to your inbox.": "Unite al movimiento. Recibí las últimas novedades sobre construcción de Riqueza e inversiones directo en tu bandeja de entrada.",
    "Explore the insights, announcements, and perspectives shaping the": "Explorá los conocimientos, anuncios y perspectivas que dan forma al",
    "Across the world, the story of Castle is unfolding &mdash; redefining Financial Ownership for Women and building a new model for Wealth Creation.": "En todo el mundo, la historia de Castle se está desarrollando &mdash; redefiniendo la Propiedad Financiera para las Mujeres y construyendo un nuevo modelo para la Creación de Riqueza.",
    "Whether you are a Celebrity, Influencer, Content Creator, Brand, Women&rsquo;s Organization, or Expert": "Ya seas una Celebridad, Influencer, Creadora de Contenido, Marca, Organización de Mujeres o Experta",
    "you can join us to transform how Women experience Wealth<br>and be part of the Women&rsquo;s Wealth Revolution.": "podés unirte a nosotras para transformar cómo las Mujeres experimentan la Riqueza<br>y ser parte de la Revolución de la Riqueza Femenina.",
    "Take control of your financial future. Join the Women-led Wealth revolution.": "Tomá el control de tu futuro financiero. Unite a la revolución de Riqueza liderada por Mujeres.",
    ">Sign In<": ">Iniciar Sesión<",
    ">Join the Waitlist<": ">Unite a la Lista de Espera<",
    "Apply for Creator Program": "Aplicar al Programa de Creadoras",
    "Partner with us": "Asociate con nosotras",
    "Castle gives you the Training, AI Tools, Intelligence and Community to take Control of your Money and start building Real Wealth.": "Castle te brinda el Entrenamiento, Herramientas de IA, Inteligencia y Comunidad para tomar el Control de tu Dinero y comenzar a construir Riqueza Real."
}

for old, new in replacements.items():
    html = html.replace(old, new)

with open('index_es.html', 'w', encoding='utf-8') as f:
    f.write(html)
