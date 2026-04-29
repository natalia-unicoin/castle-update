import re
import os

base_file = "/Users/Nati/.gemini/antigravity/scratch/Castle_V3_Standalone/index.html"
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
    html = html.replace('href="#"', 'href="masterclass.html"') 
    html = html.replace('href="#contact"', 'href="contact.html"')
    # about.html and partners.html are already linked correctly in the English index.html 
    # but let's make sure
    return html

header = update_nav(header)
# Fix masterclass specifically to avoid replacing # in href="#" if there are other #
header = re.sub(r'<a href="[^"]*"([^>]*>MasterClass</a>)', r'<a href="masterclass.html"\1', header)

# Same for footer
footer = update_nav(footer)
footer = re.sub(r'<a href="[^"]*"([^>]*>MasterClass</a>)', r'<a href="masterclass.html"\1', footer)
# Revert legal links back to #
footer = footer.replace('<a href="masterclass.html">Privacy Policy</a>', '<a href="#">Privacy Policy</a>')
footer = footer.replace('<a href="masterclass.html">Terms of Service</a>', '<a href="#">Terms of Service</a>')
footer = footer.replace('<a href="masterclass.html">Cookie Policy</a>', '<a href="#">Cookie Policy</a>')


def generate_page(filename, title):
    es_link = filename.replace('.html', '_es.html')
    
    custom_header = header
    custom_header = re.sub(r'<option value="index\.html"[^>]*>ENG</option>', f'<option value="{filename}" selected>ENG</option>', custom_header)
    custom_header = re.sub(r'<option value="index_es\.html"[^>]*>ESP</option>', f'<option value="{es_link}">ESP</option>', custom_header)
    
    # Remove selected attribute from options that shouldn't have it
    custom_header = custom_header.replace('selected', '')
    custom_header = custom_header.replace(f'<option value="{filename}">ENG</option>', f'<option value="{filename}" selected>ENG</option>')

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

generate_page("about.html", "We Are Castle")
generate_page("masterclass.html", "MasterClass")
generate_page("partners.html", "Partners")
generate_page("contact.html", "Contact Us")

# Update index.html to have the updated links too
index_header_updated = update_nav(header_match.group(1))
index_header_updated = re.sub(r'<a href="[^"]*"([^>]*>MasterClass</a>)', r'<a href="masterclass.html"\1', index_header_updated)

content = content.replace(header_match.group(1), index_header_updated)

index_footer_updated = update_nav(footer_match.group(1))
index_footer_updated = re.sub(r'<a href="[^"]*"([^>]*>MasterClass</a>)', r'<a href="masterclass.html"\1', index_footer_updated)
index_footer_updated = index_footer_updated.replace('<a href="masterclass.html">Privacy Policy</a>', '<a href="#">Privacy Policy</a>')
index_footer_updated = index_footer_updated.replace('<a href="masterclass.html">Terms of Service</a>', '<a href="#">Terms of Service</a>')
index_footer_updated = index_footer_updated.replace('<a href="masterclass.html">Cookie Policy</a>', '<a href="#">Cookie Policy</a>')

content = content.replace(footer_match.group(1), index_footer_updated)

with open(base_file, "w") as f:
    f.write(content)

print("Done generating English pages.")
