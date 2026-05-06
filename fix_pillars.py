import re

with open("index_es.html", "r") as f:
    html = f.read()

# The current div is: <div style="position: relative; z-index: 3;">
# I will replace it within the pillar cards.
# Wait, let's just use string replacement.
old_div = '<div style="position: relative; z-index: 3;">'
new_div = '<div style="position: relative; z-index: 3; min-height: 240px; display: flex; flex-direction: column; justify-content: flex-start;">'

html = html.replace(old_div, new_div)

with open("index_es.html", "w") as f:
    f.write(html)
