import glob
import re

new_block = """                <!-- Interests Checkboxes -->
                <div class="form-group" style="margin-bottom: 10px; background: #F9FAFB; padding: 15px; border-radius: 8px; border: 1px solid #E5E7EB;">
                    <label style="font-size: 14px; font-weight: 700; color: #111827; margin-bottom: 12px; display: block; text-transform: uppercase; letter-spacing: 0.5px;">I want to (select all that apply):</label>
                    <div style="display: flex; flex-direction: column; gap: 8px;">
                        <label style="display: flex; align-items: center; gap: 10px; cursor: pointer; font-size: 15px; color: #374151;">
                            <input type="checkbox" id="chk_waitlist" value="Waitlist" style="width:18px; height:18px; margin:0; accent-color: #A03FA3;"> Join the waitlist
                        </label>
                        <label style="display: flex; align-items: center; gap: 10px; cursor: pointer; font-size: 15px; color: #374151;">
                            <input type="checkbox" id="chk_masterclass" value="Masterclass" style="width:18px; height:18px; margin:0; accent-color: #A03FA3;"> Participate in the Masterclass
                        </label>
                        <label style="display: flex; align-items: center; gap: 10px; cursor: pointer; font-size: 15px; color: #374151;">
                            <input type="checkbox" id="chk_partner" value="Partner" style="width:18px; height:18px; margin:0; accent-color: #A03FA3;"> Become a Partner
                        </label>
                        <label style="display: flex; align-items: center; gap: 10px; cursor: pointer; font-size: 15px; color: #374151;">
                            <input type="checkbox" id="chk_contact" value="Contact" style="width:18px; height:18px; margin:0; accent-color: #A03FA3;"> Talk with the team
                        </label>
                        <label style="display: flex; align-items: center; gap: 10px; cursor: pointer; font-size: 15px; color: #374151;">
                            <input type="checkbox" id="chk_newsletter" value="Newsletter" checked style="width:18px; height:18px; margin:0; accent-color: #A03FA3;"> Receive updates
                        </label>
                    </div>
                </div>"""

# Ensure we don't accidentally match something else, so we match exactly what we know is in the english files
pattern = r'<!-- INTERESTS SELECTION -->.*?</div>\s*</div>'

for f in ['index.html', 'about.html', 'partners.html', 'contact.html', 'masterclass.html', 'masterclass_v2.html']:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Let's try matching exactly the old block
    new_content = re.sub(pattern, new_block, content, flags=re.DOTALL)
    
    if new_content != content:
        with open(f, 'w', encoding='utf-8') as file:
            file.write(new_content)
        print(f"Updated checkboxes in {f}")
    else:
        print(f"Could not find exact block to replace in {f}")

