import re

with open('partners_es.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace language attributes
content = content.replace('lang="es"', 'lang="en"')
content = content.replace('<title>Partners - Castle</title>', '<title>Partners - Castle</title>')

# Menu Links
content = content.replace('href="index_es.html"', 'href="index.html"')
content = content.replace('href="about_es.html"', 'href="about.html"')
content = content.replace('href="masterclass_es.html"', 'href="masterclass.html"')
content = content.replace('href="partners_es.html"', 'href="partners.html"')

# Translate header navigation text if needed (Wait, in Spanish it says MasterClass, Partners, Somos Castle, Waitlist. In English it's MasterClass, Partners, About Us, Waitlist)
content = content.replace('>Somos Castle</a>', '>About Us</a>')

# Hero
content = content.replace('Convierte tu Pasión e Influencia en Inversión.', 'Turn Your Passion and Influence into Investment.')
content = content.replace('Únete al <strong style="color: #FFFFFF; font-weight: 700;">Movimiento</strong> que ayuda a las Mujeres a construir <strong style="color: #FFFFFF; font-weight: 700;">Riqueza</strong> y participar del Futuro que están creando.', 'Join the <strong style="color: #FFFFFF; font-weight: 700;">Movement</strong> helping Women build <strong style="color: #FFFFFF; font-weight: 700;">Wealth</strong> and participate in the Future they are creating.')

# Influence Section
content = content.replace('Castle está construyendo un <strong style="font-weight: 800; color: #FFFFFF;">nuevo ecosistema impulsado por Web3</strong>, donde creadoras, líderes, marcas y comunidades pueden <strong style="font-weight: 800; color: #FFFFFF;">convertir en valor</strong> su <strong style="font-weight: 800; color: #FFFFFF;">experiencia, audiencia, alcance, credibilidad y recursos</strong>, a cambio de <strong style="font-weight: 800; color: #FFFFFF;">tokens de Castle</strong> y <strong style="font-weight: 800; color: #FFFFFF;">crecimiento compartido</strong>.', 'Castle is building a <strong style="font-weight: 800; color: #FFFFFF;">new Web3-powered ecosystem</strong>, where creators, leaders, brands, and communities can <strong style="font-weight: 800; color: #FFFFFF;">turn into value</strong> their <strong style="font-weight: 800; color: #FFFFFF;">expertise, audience, reach, credibility, and resources</strong>, in exchange for <strong style="font-weight: 800; color: #FFFFFF;">Castle tokens</strong> and <strong style="font-weight: 800; color: #FFFFFF;">shared growth</strong>.')
content = content.replace('Trae lo que te hace poderosa', 'Bring what makes you powerful')
content = content.replace('&mdash; tu voz, tu red, tu plataforma o tu comunidad &mdash; y crece con nosotros mientras escalamos un movimiento global para mujeres y riqueza.', '&mdash; your voice, your network, your platform, or your community &mdash; and grow with us as we scale a global movement for women and wealth.')

# Cards section
content = content.replace('¿Cómo Puedes ser Parte?', 'How Can You Partner?')
content = content.replace('Con Castle estamos construyendo una nueva economía impulsada por Web3, donde creadoras, líderes, marcas y comunidades pueden co-crear, invertir y crecer juntas a través de un modelo basado en colaboración, ownership y valor a largo plazo.', 'With Castle, we are building a new Web3-driven economy where creators, leaders, brands, and communities can co-create, invest, and grow together through a model based on collaboration, ownership, and long-term value.')
content = content.replace('Si eres celebridad, influencer, creadora de contenido, marca, organización de mujeres o experta, puedes unirte para transformar la forma en que las mujeres viven la riqueza y ser parte de la revolución de la riqueza femenina.', 'Whether you are a celebrity, influencer, content creator, brand, women\'s organization, or expert, you can join to transform how women experience wealth and be part of the female wealth revolution.')

content = content.replace('Influencers & Celebridades', 'Influencers & Celebrities')
content = content.replace('Creadoras de Contenido', 'Content Creators')
content = content.replace('Marcas & Compañías', 'Brands & Companies')
content = content.replace('Organizaciones de Mujeres', 'Women\'s Organizations')
content = content.replace('Expertas & Coaches', 'Experts & Coaches')

# Bottom text
content = content.replace('Multiplica tu riqueza. Construye tu Castillo.', 'Multiply your wealth. Build your Castle.')
content = content.replace('>ÚNETE</a>', '>JOIN US</a>')

# Newsletter
content = content.replace('Suscríbete a nuestro Newsletter', 'Subscribe to our Newsletter')
content = content.replace('Construye riqueza con intención. Empieza recibiendo las conversaciones que sí importan.', 'Build wealth with intention. Start by receiving the conversations that truly matter.')
content = content.replace('Tu correo electrónico', 'Your email address')
content = content.replace('>SUSCRÍBETE</button>', '>SUBSCRIBE</button>')

# The header needs to link Spanish (ESP) to partners_es.html and English (ENG) to partners.html.
# In partners_es.html, the lang-menu is:
# <a href="#" class="active">ESP</a> | <a href="index.html">ENG</a>
# We'll replace it to:
content = content.replace('<a href="#" class="active">ESP</a> | <a href="index.html">ENG</a>', '<a href="partners_es.html">ESP</a> | <a href="#" class="active">ENG</a>')
# Also handle the mobile lang menu
content = content.replace('<a href="#" class="active">Español</a>\n                <a href="index.html">English</a>', '<a href="partners_es.html">Español</a>\n                <a href="#" class="active">English</a>')

# Footer: let's replace footer strings
content = content.replace('Castle es el Sistema Operativo para que las Mujeres Gestionen su', 'Castle is the Operating System for Women to Manage their')
content = content.replace('Riqueza', 'Wealth')
content = content.replace('Explorar', 'Explore')
content = content.replace('Compañía', 'Company')
content = content.replace('Términos de Servicio', 'Terms of Service')
content = content.replace('Política de Privacidad', 'Privacy Policy')
content = content.replace('Todos los derechos reservados.', 'All rights reserved.')

# Make sure the modal texts are in English
content = content.replace('Únete a la Lista de Espera', 'Join the Waitlist')
content = content.replace('Sé de las primeras en acceder a Castle y tomar control de tu riqueza.', 'Be among the first to access Castle and take control of your wealth.')
content = content.replace('Nombre Completo', 'Full Name')
content = content.replace('Tu Nombre', 'Your Name')
content = content.replace('Tu Correo Electrónico', 'Your Email Address')
content = content.replace('¿Por qué quieres unirte a Castle?', 'Why do you want to join Castle?')
content = content.replace('Aprender a invertir', 'Learn to invest')
content = content.replace('Ser Partner', 'Become a Partner')
content = content.replace('Contacto / Prensa', 'Contact / Press')
content = content.replace('Suscribirme al Newsletter', 'Subscribe to Newsletter')
content = content.replace('Acepto los <a href="#" style="color: #A03FA3;">Términos</a> y <a href="#" style="color: #A03FA3;">Privacidad</a>.', 'I accept the <a href="#" style="color: #A03FA3;">Terms</a> and <a href="#" style="color: #A03FA3;">Privacy Policy</a>.')
content = content.replace('CERRAR', 'CLOSE')
content = content.replace('ENVIAR', 'SUBMIT')

with open('partners.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Created partners.html")
