import re

with open('masterclass_v2.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Box 1
content = content.replace(
    "url('./public/images/common/break-bg.jpg') center/cover",
    "url('./public/images/common/break-bg.jpg') center 0% / auto 160%"
)
# Box 2
content = content.replace(
    "url('./public/images/common/overcome-bg.jpg') center/cover",
    "url('./public/images/common/overcome-bg.jpg') center 0% / auto 160%"
)
# Box 3
content = content.replace(
    "url('./public/images/common/understand-bg.png') 65% center/cover",
    "url('./public/images/common/understand-bg.png') 65% 0% / auto 125%"
)
# Box 4
content = content.replace(
    "url('./public/images/common/rewire-bg.png') center/cover",
    "url('./public/images/common/rewire-bg.png') center 0% / auto 125%"
)
# Box 5
content = content.replace(
    "url('./public/images/common/step5.jpg') center/cover",
    "url('./public/images/common/step5.jpg') center 100% / auto 125%"
)
# Box 6
content = content.replace(
    "url('./public/images/common/roadmap-bg.png') center/cover",
    "url('./public/images/common/roadmap-bg.png') center 100% / auto 150%"
)

with open('masterclass_v2.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Alignment applied to masterclass_v2.html")
