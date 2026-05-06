import glob

def fix_file(filename):
    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()
    
    changed = False
    
    # 1. Remove background box from interests-grid
    old_grid_style = '<div class="interests-grid" style="background: #F9FAFB; padding: 20px; border-radius: 8px; border: 1px solid #E5E7EB;">'
    new_grid_style = '<div class="interests-grid" style="margin-top: 10px; padding: 0;">'
    if old_grid_style in content:
        content = content.replace(old_grid_style, new_grid_style)
        changed = True

    # 2. Fix consent checkbox (pre-selected and flush left)
    old_consent_es = '<input type="checkbox" id="consent" name="CONSENT" required style="width: 18px; height: 18px;">\n                    <label for="consent" style="margin-left: 8px;">Doy mi consentimiento para que Castle me contacte con actualizaciones de la plataforma e invitaciones.</label>'
    new_consent_es = '<input type="checkbox" id="consent" name="CONSENT" required checked style="width: 18px; height: 18px; margin: 0; padding: 0; accent-color: #A03FA3;">\n                    <label for="consent" style="margin-left: 0;">Doy mi consentimiento para que Castle me contacte con actualizaciones de la plataforma e invitaciones.</label>'
    
    if old_consent_es in content:
        content = content.replace(old_consent_es, new_consent_es)
        changed = True

    old_consent_en = '<input type="checkbox" id="consent" name="CONSENT" required style="width: 18px; height: 18px;">\n                    <label for="consent" style="margin-left: 8px;">I consent to Castle contacting me to share updates about the platform, launch information, and Community events.</label>'
    new_consent_en = '<input type="checkbox" id="consent" name="CONSENT" required checked style="width: 18px; height: 18px; margin: 0; padding: 0; accent-color: #A03FA3;">\n                    <label for="consent" style="margin-left: 0;">I consent to Castle contacting me to share updates about the platform, launch information, and Community events.</label>'
    
    if old_consent_en in content:
        content = content.replace(old_consent_en, new_consent_en)
        changed = True
        
    # Also fix the gap between question and options in the grid
    # Wait, the question label has margin-bottom: 15px; I'll leave it or change to 10px? 10px is better.
    # Actually just leaving it at 15px is fine since we removed the 20px padding from the parent.

    if changed:
        with open(filename, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Fixed {filename}")

for file in glob.glob("*.html"):
    fix_file(file)
