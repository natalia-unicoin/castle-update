import re
import os

base_file = "/Users/Nati/.gemini/antigravity/scratch/Castle_V3_Standalone/index_es.html"
with open(base_file, "r") as f:
    content = f.read()

# Extract parts
head_match = re.search(r'(<!DOCTYPE html>.*?<head>.*?</head>)', content, re.DOTALL)
header_match = re.search(r'(<header id="main-header".*?</header>)', content, re.DOTALL)
footer_match = re.search(r'(<footer class="site-footer">.*</footer>)', content, re.DOTALL)
scripts_match = re.search(r'(<script>.*?</script>\s*</body>\s*</html>)', content, re.DOTALL)

head = head_match.group(1) if head_match else ""
header = header_match.group(1) if header_match else ""
footer = footer_match.group(1) if footer_match else ""
scripts = scripts_match.group(1) if scripts_match else "</body></html>"

# Fix navigation links in header and footer
def update_nav(html):
    html = html.replace('href="about.html"', 'href="about_es.html"')
    html = html.replace('href="#"', 'href="masterclass_es.html"') # Note: this might replace multiple '#' if not careful
    html = html.replace('href="partners.html"', 'href="partners_es.html"')
    html = html.replace('href="#contact"', 'href="contact_es.html"')
    # More specific replaces for the masterclass since href="#" is too generic
    html = html.replace('>MasterClass<', ' href="masterclass_es.html">MasterClass<')
    return html

header = update_nav(header)
# In header we have `<a href="#" style="text-transform: none;">MasterClass</a>`
# Let's do it cleaner
header = re.sub(r'<a href="#"([^>]*>MasterClass</a>)', r'<a href="masterclass_es.html"\1', header)

# Same for footer
footer = footer_match.group(1) if footer_match else ""
footer = footer.replace('href="about.html"', 'href="about_es.html"')
footer = footer.replace('href="#contact"', 'href="contact_es.html"')
footer = re.sub(r'<a href="#"([^>]*>MasterClass</a>)', r'<a href="masterclass_es.html"\1', footer)
footer = footer.replace('href="partners.html"', 'href="partners_es.html"')

# Also we need to fix the lang switcher in the header to point back to index.html or the respective English page.
# Actually for placeholders, they can just point to index.html for ENG and the current page for ESP.
def generate_page(filename, title):
    
    # Custom lang switcher for each page
    eng_link = filename.replace('_es.html', '.html')
    if filename == "contact_es.html":
        eng_link = "index.html" # Assuming contact doesn't exist yet
    elif filename == "masterclass_es.html":
        eng_link = "index.html"
    elif filename == "partners_es.html":
        eng_link = "index.html"
    
    custom_header = header
    custom_header = re.sub(r'<option value="index\.html"[^>]*>ENG</option>', f'<option value="{eng_link}">ENG</option>', custom_header)
    custom_header = re.sub(r'<option value="index_es\.html"[^>]*>ESP</option>', f'<option value="{filename}" selected>ESP</option>', custom_header)

    hero_section = f"""
    <body>
    {custom_header}

    <!-- Hero Placeholder -->
    <section class="hero snap-section" style="background-color: #1A1A1A; display: flex; align-items: center; justify-content: center; text-align: center; height: 60vh; border-bottom: 1px solid #333;">
        <div class="container" style="max-width: 1400px; padding: 0 4vw;">
            <h1 class="hero-title color-reveal" style="color: #FFFFFF;">{title}</h1>
        </div>
    </section>

    {footer}
    {scripts}
    """
    
    # put the head back
    full_html = f"{head}\n{hero_section}"
    
    with open(f"/Users/Nati/.gemini/antigravity/scratch/Castle_V3_Standalone/{filename}", "w") as out:
        out.write(full_html)
    print(f"Created {filename}")

generate_page("about_es.html", "Somos Castle")
generate_page("masterclass_es.html", "MasterClass")
generate_page("partners_es.html", "Socios")
generate_page("contact_es.html", "Contáctanos")

# Update index_es.html to have the updated links too
index_es_header_updated = update_nav(header_match.group(1))
index_es_header_updated = re.sub(r'<a href="#"([^>]*>MasterClass</a>)', r'<a href="masterclass_es.html"\1', index_es_header_updated)

content = content.replace(header_match.group(1), index_es_header_updated)

index_es_footer_updated = update_nav(footer_match.group(1))
index_es_footer_updated = re.sub(r'<a href="#"([^>]*>MasterClass</a>)', r'<a href="masterclass_es.html"\1', index_es_footer_updated)
content = content.replace(footer_match.group(1), index_es_footer_updated)

with open(base_file, "w") as f:
    f.write(content)

print("Updated index_es.html links")
