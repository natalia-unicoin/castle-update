import re

files = [
    "/Users/Nati/.gemini/antigravity/scratch/Castle_V3_Standalone/masterclass.html",
    "/Users/Nati/.gemini/antigravity/scratch/Castle_V3_Standalone/masterclass_es.html"
]

def update_hero(content):
    # Change hero background to violet #A03FA3
    content = content.replace('background-color: #1A1A1A; display: flex; align-items: center; padding: 150px 4vw 100px 4vw;',
                              'background-color: #A03FA3; display: flex; align-items: center; padding: 150px 4vw 100px 4vw;')
    content = content.replace('border-bottom: 1px solid #333;', 'border-bottom: 1px solid #A03FA3;')
    
    # Change purple text in hero to white
    content = content.replace('<div style="color: #A03FA3; font-weight: 700; font-size: 16px; letter-spacing: 4px; margin-bottom: 20px; text-transform: uppercase;">',
                              '<div style="color: #FFFFFF; font-weight: 700; font-size: 16px; letter-spacing: 4px; margin-bottom: 20px; text-transform: uppercase;">')
    
    content = content.replace('<span style="color: #A03FA3;">Own Your Wealth.</span>',
                              '<span style="color: #FFFFFF;">Own Your Wealth.</span>')
    content = content.replace('<span style="color: #A03FA3;">Sé dueña de tu riqueza.</span>',
                              '<span style="color: #FFFFFF;">Sé dueña de tu riqueza.</span>')
                              
    # Change Hero button from purple to white
    content = content.replace('class="btn" style="background-color: #A03FA3; border: none; color: #FFFFFF; font-weight: 700; padding: 18px 45px; border-radius: 30px; display: inline-block;">\n                    APPLY NOW',
                              'class="btn" style="background-color: #FFFFFF; border: none; color: #A03FA3; font-weight: 800; padding: 18px 45px; border-radius: 30px; display: inline-block;">\n                    APPLY NOW')
    content = content.replace('class="btn" style="background-color: #A03FA3; border: none; color: #FFFFFF; font-weight: 700; padding: 18px 45px; border-radius: 30px; display: inline-block;">\n                    APLICA AHORA',
                              'class="btn" style="background-color: #FFFFFF; border: none; color: #A03FA3; font-weight: 800; padding: 18px 45px; border-radius: 30px; display: inline-block;">\n                    APLICA AHORA')
    
    return content

def update_the_truth(content):
    # Section 5: The Truth from black to #F8F8FA (light grey) and text to black
    content = content.replace('<!-- 5. The Truth -->\n    <section class="snap-section" style="background-color: #1A1A1A; padding: 120px 4vw; text-align: center; color: white;">',
                              '<!-- 5. The Truth -->\n    <section class="snap-section" style="background-color: #F8F8FA; padding: 120px 4vw; text-align: center; color: #1A1A1A;">')
    # Change text color of "You were always capable..." and "Siempre fuiste capaz..." from implicitly white to dark grey #1A1A1A
    # The h2 doesn't have a color specified, so it inherits the parent's color. This works.
    
    return content

def update_cta_label(content):
    # Section 6: Label
    content = content.replace('background-color: #1A1A1A; color: white;', 'background-color: #A03FA3; color: white;')
    return content

for path in files:
    with open(path, "r") as f:
        c = f.read()
    
    c = update_hero(c)
    c = update_the_truth(c)
    c = update_cta_label(c)
    
    # Update dark placeholders to lighter gray
    c = c.replace('background-color: #2A2A2A;', 'background-color: #E5E7EB;')
    
    with open(path, "w") as f:
        f.write(c)
    
print("Updated all black backgrounds to violet or gray.")
