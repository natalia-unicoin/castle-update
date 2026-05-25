import re

with open('masterclass_v2.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update gradient to start lower (from 0% to 50%)
# Old: background: linear-gradient(to bottom, rgba(0,0,0,0) 0%, rgba(0,0,0,0.85) 100%)
# New: background: linear-gradient(to bottom, rgba(0,0,0,0) 50%, rgba(0,0,0,0.9) 100%)
content = content.replace(
    'linear-gradient(to bottom, rgba(0,0,0,0) 0%, rgba(0,0,0,0.85) 100%)',
    'linear-gradient(to bottom, rgba(0,0,0,0) 50%, rgba(0,0,0,0.9) 100%)'
)

# 2. Update the 'Understand' background position
# Find the specific div for understand-bg and change `center/cover` to `65% center/cover`
content = content.replace(
    "url('./public/images/common/understand-bg.png') center/cover",
    "url('./public/images/common/understand-bg.png') 65% center/cover"
)

# 3. Increase font size by 2 points for the inter text
# Old: font-size: clamp(12px, 1.1vw, 14px); color: #FFFFFF; font-weight: 400; line-height: 1.3;">limiting money beliefs
# Let's replace the common style part for all 6 boxes
content = content.replace(
    "font-size: clamp(12px, 1.1vw, 14px);",
    "font-size: clamp(14px, 1.3vw, 16px);"
)

with open('masterclass_v2.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updates applied to masterclass_v2.html")
