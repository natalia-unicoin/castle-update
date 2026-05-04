import re

with open('contact.html', 'r', encoding='utf-8') as f:
    en_content = f.read()

with open('contact_es.html', 'r', encoding='utf-8') as f:
    es_content = f.read()

# Extract Hero and Form from English
hero_pattern = re.compile(r'(<section class="hero snap-section".*?</section>)', re.DOTALL)
form_pattern = re.compile(r'(<!-- Contact Form Section \(Waitlist Style\) -->.*?</section>)', re.DOTALL)

en_hero = hero_pattern.search(en_content).group(1)
en_form = form_pattern.search(en_content).group(1)

# Translate Hero
es_hero = en_hero.replace("Contact Us", "Contáctanos")
es_hero = es_hero.replace(
    "Have a question, partnership idea, or just want to say hello? Drop us a message below and our team will get back to you.",
    "¿Tienes alguna pregunta, idea para asociarnos o simplemente quieres saludar? Déjanos un mensaje abajo y nuestro equipo te responderá."
)

# Translate Form
es_form = en_form.replace("Contact Us", "Contáctanos")
es_form = es_form.replace("Full Name *", "Nombre Completo *")
es_form = es_form.replace("Email Address *", "Correo Electrónico *")
es_form = es_form.replace("Phone Number", "Número de Teléfono")
es_form = es_form.replace("Age", "Edad")
es_form = es_form.replace("Country", "País")
es_form = es_form.replace("LinkedIn URL", "URL de LinkedIn")
es_form = es_form.replace("Company / Organization", "Empresa / Organización")
es_form = es_form.replace("Your Role / Title", "Tu Rol / Cargo")
es_form = es_form.replace("Instagram Handle", "Usuario de Instagram")
es_form = es_form.replace("Tell us *", "Cuéntanos *")
es_form = es_form.replace("Jane Doe", "Juana Pérez")
es_form = es_form.replace("jane@example.com", "juana@ejemplo.com")
es_form = es_form.replace("Select your country", "Selecciona tu país")
es_form = es_form.replace("Select age range", "Selecciona rango de edad")
es_form = es_form.replace("Acme Corp", "Empresa Ejemplo")
es_form = es_form.replace("Founder", "Fundadora")
es_form = es_form.replace("@janedoe", "@juanaperez")
es_form = es_form.replace("Why are you contacting us?", "¿Por qué nos contactas?")
es_form = es_form.replace("I consent to Castle contacting me to share updates about the platform, launch information, and Community events.", "Acepto que Castle me contacte para compartir actualizaciones sobre la plataforma, información de lanzamiento y eventos de la Comunidad.")

# In contact_es.html, replace the old hero and whatever is between it and the footer
# Wait, contact_es.html might not have the embedded form yet.
# It has <section class="hero ...">...</section> and then <footer class="site-footer">
# We can just replace the old Hero with the new Hero + new Form

es_hero_to_replace = hero_pattern.search(es_content).group(1)

# Check if there is already an embedded form in contact_es.html
if form_pattern.search(es_content):
    es_form_to_replace = form_pattern.search(es_content).group(1)
    es_content = es_content.replace(es_hero_to_replace, es_hero)
    es_content = es_content.replace(es_form_to_replace, es_form)
else:
    # No embedded form yet. Replace old hero with new hero + form
    es_content = es_content.replace(es_hero_to_replace, es_hero + "\n\n" + es_form)

with open('contact_es.html', 'w', encoding='utf-8') as f:
    f.write(es_content)

print("Contact ES translated successfully.")

