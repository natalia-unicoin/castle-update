import re

with open('masterclass_v2.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Align logo better
# Old: Powered by <img src="./public/images/common/fundacion-light.png" alt="Unicoin Foundation" style="height: 28px; object-fit: contain; opacity: 0.9;">
# New: <span style="display: flex; align-items: center; transform: translateY(-2px);">Powered by</span> <img src="./public/images/common/fundacion-light.png" alt="Unicoin Foundation" style="height: 28px; object-fit: contain; opacity: 0.9;">
content = content.replace(
    'Powered by <img src="./public/images/common/fundacion-light.png"',
    '<span style="display: flex; align-items: center; transform: translateY(-3px);">Powered by</span> <img src="./public/images/common/fundacion-light.png"'
)

# 2. Add 30px gap between bajada and boxes
# Old: <div class="mobile-scroll-row" id="subhero-scroll" style="display: grid; grid-template-columns: repeat(6, 1fr); gap: 10px; text-align: left;">
# New: <div class="mobile-scroll-row" id="subhero-scroll" style="display: grid; grid-template-columns: repeat(6, 1fr); gap: 10px; text-align: left; margin-top: 30px;">
content = content.replace(
    '<div class="mobile-scroll-row" id="subhero-scroll" style="display: grid; grid-template-columns: repeat(6, 1fr); gap: 10px; text-align: left;">',
    '<div class="mobile-scroll-row" id="subhero-scroll" style="display: grid; grid-template-columns: repeat(6, 1fr); gap: 10px; text-align: left; margin-top: 30px;">'
)

# 3. Make the boxes 80/100px taller. 
# Current: aspect-ratio: 2/3;
# Change to: aspect-ratio: 5/9; (taller)
content = content.replace(
    'aspect-ratio: 2/3;',
    'aspect-ratio: 5/9;'
)

with open('masterclass_v2.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updates applied to masterclass_v2.html")
