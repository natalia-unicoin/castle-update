import re

def fix_styles(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Fix padding on the hero section to match home page hero (e.g. 15vh top padding)
    content = content.replace('padding: calc(150px + 4vw) 4vw 80px 4vw;', 'padding: 150px 4vw 80px 4vw;')
    
    # 2. Fix the Hero Title
    # Old: style="color: #1A1A1A; font-size: clamp(48px, 6vw, 72px); letter-spacing: -2px; margin-bottom: 24px; line-height: 1;"
    # New: style="color: #1A1A1A; font-size: clamp(64px, 10vw, 130px); font-weight: 700; line-height: 0.95; letter-spacing: -4px; margin-bottom: 24px; font-family: 'Inter', sans-serif;"
    content = re.sub(
        r'style="color: #1A1A1A; font-size: clamp\(48px, 6vw, 72px\); letter-spacing: -2px; margin-bottom: 24px; line-height: 1;"',
        r'style="color: #1A1A1A; font-size: clamp(64px, 10vw, 130px); font-weight: 700; line-height: 0.95; letter-spacing: -4px; margin-bottom: 24px; font-family: \'Inter\', sans-serif;"',
        content
    )

    # 3. Fix the Hero Subtitle
    # Old: style="color: #4B5563; font-size: clamp(18px, 2vw, 22px); line-height: 1.6; max-width: 600px; margin-bottom: 40px;"
    # New: style="color: #4B5563; font-size: clamp(20px, 2.5vw, 28px); line-height: 1.25; max-width: 650px; font-weight: 400; font-family: 'Inter', sans-serif; margin-bottom: 40px;"
    content = re.sub(
        r'style="color: #4B5563; font-size: clamp\(18px, 2vw, 22px\); line-height: 1\.6; max-width: 600px; margin-bottom: 40px;"',
        r'style="color: #4B5563; font-size: clamp(20px, 2.5vw, 28px); line-height: 1.25; max-width: 650px; font-weight: 400; font-family: \'Inter\', sans-serif; margin-bottom: 40px;"',
        content
    )

    # 4. Fix Ecosystem Title to match .section-title
    # Old: style="color: #FFFFFF; font-size: clamp(24px, 4vw, 36px); font-weight: 700; margin-bottom: 40px; padding: 0 20px;"
    # New: class="section-title" style="color: #FFFFFF; padding: 0 20px; margin-bottom: 40px;"
    content = re.sub(
        r'<h2 style="color: #FFFFFF; font-size: clamp\(24px, 4vw, 36px\); font-weight: 700; margin-bottom: 40px; padding: 0 20px;">',
        r'<h2 class="section-title" style="color: #FFFFFF; padding: 0 20px; margin-bottom: 40px;">',
        content
    )

    # 5. Fix margins and padding (change var(--section-pad-large) to var(--section-pad-y) to match Home)
    content = content.replace('padding: var(--section-pad-large)', 'padding: var(--section-pad-y)')
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
        print(f"Updated styles in {file_path}")

fix_styles('contact_es.html')
fix_styles('contact.html')

