import re

def extract_texts(filepath):
    with open(filepath, "r") as f:
        content = f.read()
    
    # Simple regex to get text inside tags, ignoring scripts and styles
    content = re.sub(r'<script.*?</script>', '', content, flags=re.DOTALL)
    content = re.sub(r'<style.*?</style>', '', content, flags=re.DOTALL)
    
    # We can just match specific sections or use a general approach
    # Let's match typical text tags
    tags = re.findall(r'<h[1-6][^>]*>(.*?)</h[1-6]>|<p[^>]*>(.*?)</p>|<a[^>]*class="btn[^"]*"[^>]*>(.*?)</a>', content, re.DOTALL)
    
    texts = []
    for t in tags:
        # t is a tuple of groups
        text = "".join(t).strip()
        text = re.sub(r'<[^>]+>', '', text) # remove inner tags
        text = re.sub(r'\s+', ' ', text) # normalize spaces
        if len(text) > 2:
            texts.append(text)
    return texts

eng_texts = extract_texts("/Users/Nati/.gemini/antigravity/scratch/Castle_V3_Standalone/index.html")
es_texts = extract_texts("/Users/Nati/.gemini/antigravity/scratch/Castle_V3_Standalone/index_es.html")

md_table = "| Sección / Elemento | Inglés (`index.html`) | Español (`index_es.html`) |\n"
md_table += "|---|---|---|\n"

# Zip them up (might not match exactly if structure differs, but should be close)
min_len = min(len(eng_texts), len(es_texts))
for i in range(min_len):
    if eng_texts[i] != es_texts[i]: # Only show translated ones
        md_table += f"| Texto {i+1} | {eng_texts[i]} | {es_texts[i]} |\n"

with open("/Users/Nati/.gemini/antigravity/scratch/Castle_V3_Standalone/text_comparison.md", "w") as f:
    f.write(md_table)

print(f"Extracted {min_len} text blocks.")
