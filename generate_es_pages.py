import re
import os

base_file = "/Users/Nati/.gemini/antigravity/scratch/Castle_V3_Standalone/index_es.html"
with open(base_file, "r") as f:
    content = f.read()

# Extract parts
head_match = re.search(r'(<!DOCTYPE html>.*?<head>.*?</head>)', content, re.DOTALL)
header_match = re.search(r'(<header id="main-header".*?</header>)', content, re.DOTALL)
footer_match = re.search(r'(<footer class="site-footer">.*?</footer>)', content, re.DOTALL)

# Everything after </footer>
scripts = content[footer_match.end():] if footer_match else "</body></html>"

head = head_match.group(1) if head_match else ""
header = header_match.group(1) if header_match else ""
footer = footer_match.group(1) if footer_match else ""

# Fix navigation links in header and footer
def update_nav(html):
    html = html.replace('href="about.html"', 'href="about_es.html"')
    html = html.replace('href="#"', 'href="masterclass_es.html"') 
    html = html.replace('href="partners.html"', 'href="partners_es.html"')
    html = html.replace('href="#contact"', 'href="contact_es.html"')
    return html

header = update_nav(header)
# Specific fix
header = re.sub(r'<a href="[^"]*"([^>]*>MasterClass</a>)', r'<a href="masterclass_es.html"\1', header)

# Same for footer
footer = update_nav(footer)
footer = re.sub(r'<a href="[^"]*"([^>]*>MasterClass</a>)', r'<a href="masterclass_es.html"\1', footer)
# Revert legal links back to #
footer = footer.replace('<a href="masterclass_es.html">Política de Privacidad</a>', '<a href="#">Política de Privacidad</a>')
footer = footer.replace('<a href="masterclass_es.html">Términos de Servicio</a>', '<a href="#">Términos de Servicio</a>')
footer = footer.replace('<a href="masterclass_es.html">Política de Cookies</a>', '<a href="#">Política de Cookies</a>')


def generate_page(filename, title):
    eng_link = filename.replace('_es.html', '.html')
    if filename in ["contact_es.html", "masterclass_es.html", "partners_es.html"]:
        eng_link = "index.html" 
    
    custom_header = header
    custom_header = re.sub(r'<option value="index\.html"[^>]*>ENG</option>', f'<option value="{eng_link}">ENG</option>', custom_header)
    custom_header = re.sub(r'<option value="index_es\.html"[^>]*>ESP</option>', f'<option value="{filename}" selected>ESP</option>', custom_header)
    
    # Remove selected attribute from options that shouldn't have it
    custom_header = custom_header.replace('selected', '')
    custom_header = custom_header.replace(f'<option value="{filename}">ESP</option>', f'<option value="{filename}" selected>ESP</option>')

    hero_section = f"""
    <body>
    {custom_header}

    <!-- Hero Placeholder -->
    <section class="hero snap-section" style="background-color: #1A1A1A; display: flex; align-items: center; justify-content: center; text-align: center; height: 100vh; border-bottom: 1px solid #333; background-image: none;">
        <div class="container" style="max-width: 1400px; padding: 0 4vw;">
            <h1 class="hero-title color-reveal" style="color: #FFFFFF; font-size: clamp(60px, 8vw, 100px); letter-spacing: -2px;">{title}</h1>
        </div>
    </section>

    {footer}
    {scripts}
    """
    
    full_html = f"{head}\n{hero_section}"
    
    with open(f"/Users/Nati/.gemini/antigravity/scratch/Castle_V3_Standalone/{filename}", "w") as out:
        out.write(full_html)
    print(f"Created {filename}")

generate_page("about_es.html", "Somos Castle")
generate_page("masterclass_es.html", "MasterClass")
generate_page("partners_es.html", "Socios")
generate_page("contact_es.html", "Contáctanos")

print("Done generating pages.")
