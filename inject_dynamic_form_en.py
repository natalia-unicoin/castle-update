import re
import glob

def process_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Remove existing modal if any
    content = re.sub(r'<div id="waitlistModal".*?<!-- Unified CTA Modal End -->\s*', '', content, flags=re.DOTALL)
    # Or if it doesn't have the End comment but has script src mailchimp
    content = re.sub(r'<div id="waitlistModal".*?</script>\s*</div>\s*</div>\s*<script src="\./js/mailchimp\.js"></script>\s*', '', content, flags=re.DOTALL)
    # Just to be safe, a generic regex for the modal and script
    content = re.sub(r'<!-- Unified CTA Modal -->.*?<script src="\./js/mailchimp\.js"></script>\s*(<script>.*?</script>)?\s*', '', content, flags=re.DOTALL)
    # Sometimes it's just <div id="waitlistModal" ... down to </div></div> <script src...
    modal_start = content.find('<div id="waitlistModal"')
    if modal_start != -1:
        # We need a robust removal since previous injections might vary
        pass

    # A more robust regex for removing old script blocks that were injected
    content = re.sub(r'<!-- INJECTED UNIFIED MODAL START -->.*?<!-- INJECTED UNIFIED MODAL END -->\s*', '', content, flags=re.DOTALL)
    
    # We will inject our new block right before </body>
    
    new_js = """
    <!-- INJECTED UNIFIED MODAL START -->
    <!-- Intl-tel-input CSS -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/intl-tel-input@18.2.1/build/css/intlTelInput.css">
    
    <div id="waitlistModal" style="display: none; position: fixed; top: 0; left: 0; width: 100%; height: 100%; z-index: 99999; background: rgba(17,17,17,0.85); align-items: center; justify-content: center; backdrop-filter: blur(8px); font-family: 'Inter', sans-serif;">
        <div style="background: #FFFFFF; padding: 40px; border-radius: 8px; max-width: 600px; width: 90%; position: relative; max-height: 90vh; overflow-y: auto; text-align: left; box-shadow: 0 40px 100px rgba(0,0,0,0.4);">
            <button type="button" onclick="document.getElementById('waitlistModal').style.display='none';" style="position: absolute; top: 15px; right: 20px; background: none; border: none; font-size: 30px; cursor: pointer; color: #2A2A2A; line-height: 1; padding: 0;">&times;</button>
            
            <h2 class="section-heading color-reveal" style="margin-top: 10px; margin-bottom: 20px; text-align: center; font-size: clamp(22px, 5vw, 36px); letter-spacing: -1px; color: #1A1A1A;">Discover more about Castle</h2>
            
            <div id="form_message" style="display:none; padding: 15px; margin-bottom: 20px; border-radius: 6px; font-weight: 600; text-align: center; font-size: 14px;"></div>

            <form id="unifiedForm" class="waitlist-form" onsubmit="event.preventDefault(); submitMailchimpJSONP(this);" style="display: flex; flex-direction: column; gap: 16px;">
                <input type="hidden" name="SOURCE" id="unifiedSource" value="Unified Form">
                
                <!-- INTERESTS SELECTION -->
                <div class="form-group" style="margin-bottom: 10px;">
                    <label style="font-size: 15px; font-weight: 700; color: #1A1A1A; margin-bottom: 12px; display: block;">What would you like to do at Castle? <span style="font-size: 13px; font-weight: 400; color: #4B5563; margin-left: 6px;">(you can select more than one)</span></label>
                    <div style="display: grid; gap: 10px; grid-template-columns: 1fr;">
                        <label style="display: flex; align-items: center; gap: 10px; cursor: pointer; font-size: 14px; font-weight: 500; color: #2A2A2A;"><input type="checkbox" id="chk_masterclass" style="width:18px; height:18px; margin:0; accent-color: #A03FA3;"> I want to join the MasterClass Series</label>
                        <label style="display: flex; align-items: center; gap: 10px; cursor: pointer; font-size: 14px; font-weight: 500; color: #2A2A2A;"><input type="checkbox" id="chk_partner" style="width:18px; height:18px; margin:0; accent-color: #A03FA3;"> I want to collaborate as a Partner</label>
                        <label style="display: flex; align-items: center; gap: 10px; cursor: pointer; font-size: 14px; font-weight: 500; color: #2A2A2A;"><input type="checkbox" id="chk_contact" style="width:18px; height:18px; margin:0; accent-color: #A03FA3;"> I want to connect with the team</label>
                        <label style="display: flex; align-items: center; gap: 10px; cursor: pointer; font-size: 14px; font-weight: 500; color: #2A2A2A;"><input type="checkbox" id="chk_waitlist" style="width:18px; height:18px; margin:0; accent-color: #A03FA3; display:none;"><span style="display:none;">Waitlist</span></label>
                        <label style="display: flex; align-items: center; gap: 10px; cursor: pointer; font-size: 14px; font-weight: 500; color: #2A2A2A;"><input type="checkbox" id="chk_newsletter" style="width:18px; height:18px; margin:0; accent-color: #A03FA3; display:none;"><span style="display:none;">Newsletter</span></label>
                    </div>
                </div>

                <!-- 1. PERSONAL BASIC INFO -->
                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px;">
                    <div class="form-group" style="display: flex; flex-direction: column; gap: 6px;">
                        <label style="font-size: 13px; font-weight: 600; color: #1A1A1A;">Full Name *</label>
                        <input type="text" name="FNAME" required placeholder="e.g. Jane Doe" style="padding: 12px 14px; border: 1px solid #D1D5DB; border-radius: 5px; font-family: 'Inter', sans-serif; font-size: 14px; background: #F9FAFB;">
                    </div>
                    <div class="form-group" style="display: flex; flex-direction: column; gap: 6px;">
                        <label style="font-size: 13px; font-weight: 600; color: #1A1A1A;">Email Address *</label>
                        <input type="email" name="EMAIL" required placeholder="jane@example.com" style="padding: 12px 14px; border: 1px solid #D1D5DB; border-radius: 5px; font-family: 'Inter', sans-serif; font-size: 14px; background: #F9FAFB;">
                    </div>
                </div>

                <!-- 2. GEO & PHONE -->
                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px;">
                    <div class="form-group" style="display: flex; flex-direction: column; gap: 6px;">
                        <label style="font-size: 13px; font-weight: 600; color: #1A1A1A;">Country of residence</label>
                        <select name="COUNTRY" style="padding: 12px 14px; border: 1px solid #D1D5DB; border-radius: 5px; font-family: 'Inter', sans-serif; font-size: 14px; background: #F9FAFB; appearance: none; background-image: url('data:image/svg+xml;charset=US-ASCII,<svg width=\"12\" height=\"12\" viewBox=\"0 0 16 16\" fill=\"%23111\"><path d=\"M4.293 5.293a1 1 0 0 1 1.414 0L8 8.586l2.293-2.293a1 1 0 1 1 1.414 1.414l-3 3a1 1 0 0 1-1.414 0l-3-3a1 1 0 0 1 0-1.414z\"/></svg>'); background-repeat: no-repeat; background-position: right 14px center;">
                            <option value="" disabled selected>Select your country</option>
                            <option value="United States">United States</option>
                            <option value="United Kingdom">United Kingdom</option>
                            <option value="Canada">Canada</option>
                            <option value="Australia">Australia</option>
                            <option value="Spain">Spain</option>
                            <option value="Argentina">Argentina</option>
                            <option value="Mexico">Mexico</option>
                            <option value="Colombia">Colombia</option>
                            <option value="Chile">Chile</option>
                            <option value="Peru">Peru</option>
                            <option value="Other">Other</option>
                        </select>
                    </div>
                    <div class="form-group" style="display: flex; flex-direction: column; gap: 6px;">
                        <label style="font-size: 13px; font-weight: 600; color: #1A1A1A;">Phone Number</label>
                        <input type="tel" id="phone_intl" placeholder="" style="padding: 12px 14px; border: 1px solid #D1D5DB; border-radius: 5px; font-family: 'Inter', sans-serif; font-size: 14px; background: #F9FAFB; width: 100%;">
                    </div>
                </div>

                <!-- 3. DYNAMIC: B2B FIELDS (Partner / Contact) -->
                <div id="dyn_b2b" style="display: none; grid-template-columns: 1fr 1fr; gap: 16px;">
                    <div class="form-group" style="display: flex; flex-direction: column; gap: 6px;">
                        <label style="font-size: 13px; font-weight: 600; color: #1A1A1A;">Company / Organization</label>
                        <input type="text" name="COMPANY" placeholder="e.g. Castle Inc." style="padding: 12px 14px; border: 1px solid #D1D5DB; border-radius: 5px; font-family: 'Inter', sans-serif; font-size: 14px; background: #F9FAFB;">
                    </div>
                    <div class="form-group" style="display: flex; flex-direction: column; gap: 6px;">
                        <label style="font-size: 13px; font-weight: 600; color: #1A1A1A;">Your Role / Title</label>
                        <input type="text" name="ROLE" placeholder="e.g. Founder / CEO" style="padding: 12px 14px; border: 1px solid #D1D5DB; border-radius: 5px; font-family: 'Inter', sans-serif; font-size: 14px; background: #F9FAFB;">
                    </div>
                </div>

                <!-- DYNAMIC: PARTNER ONLY -->
                <div id="dyn_partner" style="display: none;">
                    <div class="form-group" style="display: flex; flex-direction: column; gap: 6px; margin-bottom: 16px;">
                        <label style="font-size: 13px; font-weight: 600; color: #1A1A1A;">Type of Partnership *</label>
                        <select id="partnertype" name="PARTNERTYP" style="padding: 12px 14px; border: 1px solid #D1D5DB; border-radius: 5px; font-family: 'Inter', sans-serif; font-size: 14px; background: #F9FAFB; appearance: none; background-image: url('data:image/svg+xml;charset=US-ASCII,<svg width=\"12\" height=\"12\" viewBox=\"0 0 16 16\" fill=\"%23111\"><path d=\"M4.293 5.293a1 1 0 0 1 1.414 0L8 8.586l2.293-2.293a1 1 0 1 1 1.414 1.414l-3 3a1 1 0 0 1-1.414 0l-3-3a1 1 0 0 1 0-1.414z\"/></svg>'); background-repeat: no-repeat; background-position: right 14px center;">
                            <option value="" disabled selected>Select a type</option>
                            <option value="Content Creator / Influencer">Content Creator / Influencer</option>
                            <option value="Expert (finance, legal, wellness, etc.)">Expert (finance, legal, wellness, etc.)</option>
                            <option value="Brand / Company Representative">Brand / Company Representative</option>
                            <option value="Women's Community Representative">Women's Community Representative</option>
                            <option value="Other">Other</option>
                        </select>
                    </div>
                    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px;">
                        <div class="form-group" style="display: flex; flex-direction: column; gap: 6px;">
                            <label style="font-size: 13px; font-weight: 600; color: #1A1A1A;">LinkedIn Profile</label>
                            <input type="url" name="LINKEDIN" placeholder="https://linkedin.com/in/janedoe" style="padding: 12px 14px; border: 1px solid #D1D5DB; border-radius: 5px; font-family: 'Inter', sans-serif; font-size: 14px; background: #F9FAFB;">
                        </div>
                        <div class="form-group" style="display: flex; flex-direction: column; gap: 6px;">
                            <label style="font-size: 13px; font-weight: 600; color: #1A1A1A;">Instagram Profile</label>
                            <input type="text" name="INSTAGRAM" placeholder="@janedoe" style="padding: 12px 14px; border: 1px solid #D1D5DB; border-radius: 5px; font-family: 'Inter', sans-serif; font-size: 14px; background: #F9FAFB;">
                        </div>
                    </div>
                </div>

                <!-- DYNAMIC: CONTACT/MESSAGE -->
                <div id="dyn_contact" style="display: none;">
                    <div class="form-group" style="display: flex; flex-direction: column; gap: 6px;">
                        <label style="font-size: 13px; font-weight: 600; color: #1A1A1A;">Message or inquiry *</label>
                        <textarea id="message" name="MESSAGE" rows="3" placeholder="How can we help you?" style="padding: 12px 14px; border: 1px solid #D1D5DB; border-radius: 5px; font-family: 'Inter', sans-serif; font-size: 14px; background: #F9FAFB; resize: vertical;"></textarea>
                    </div>
                </div>
                
                <!-- DYNAMIC: MASTERCLASS/WAITLIST -->
                <div id="dyn_invest" style="display: none; grid-template-columns: 1fr; gap: 16px;">
                    <div class="form-group" style="display: flex; flex-direction: column; gap: 6px;">
                        <label style="font-size: 13px; font-weight: 600; color: #1A1A1A;">Age Range</label>
                        <select name="AGE" style="padding: 12px 14px; border: 1px solid #D1D5DB; border-radius: 5px; font-family: 'Inter', sans-serif; font-size: 14px; background: #F9FAFB; appearance: none; background-image: url('data:image/svg+xml;charset=US-ASCII,<svg width=\"12\" height=\"12\" viewBox=\"0 0 16 16\" fill=\"%23111\"><path d=\"M4.293 5.293a1 1 0 0 1 1.414 0L8 8.586l2.293-2.293a1 1 0 1 1 1.414 1.414l-3 3a1 1 0 0 1-1.414 0l-3-3a1 1 0 0 1 0-1.414z\"/></svg>'); background-repeat: no-repeat; background-position: right 14px center;">
                            <option value="" disabled selected>Select age range</option>
                            <option value="18-24">18-24</option>
                            <option value="25-29">25-29</option>
                            <option value="30-34">30-34</option>
                            <option value="35-39">35-39</option>
                            <option value="40-44">40-44</option>
                            <option value="45-49">45-49</option>
                            <option value="50-54">50-54</option>
                            <option value="55-59">55-59</option>
                            <option value="60+">60+</option>
                        </select>
                    </div>
                </div>

                <div style="display: flex; align-items: flex-start; gap: 10px; margin-top: 10px;">
                    <input type="checkbox" id="chk_subscription" name="CONSENT" required style="margin-top: 4px; width: 16px; height: 16px; accent-color: #A03FA3;">
                    <label for="chk_subscription" style="font-size: 12px; color: #4B5563; line-height: 1.4; font-weight: 400; margin:0;">I consent to receive communications from Castle about the platform, MasterClasses, and updates.</label>
                </div>

                <button type="submit" id="submit_btn" style="background-color: #A03FA3; color: #FFFFFF; font-weight: 800; letter-spacing: 2px; padding: 16px 40px; border-radius: 50px; font-size: 14px; border: none; cursor: pointer; transition: transform 0.2s, box-shadow 0.2s; margin-top: 10px; width: 100%; box-shadow: 0 10px 20px rgba(160, 63, 163, 0.3); text-transform: uppercase;">SUBMIT</button>
            </form>
        </div>
    </div>
    
    <script src="https://cdn.jsdelivr.net/npm/intl-tel-input@18.2.1/build/js/intlTelInput.min.js"></script>
    <script>
        let iti;

        function updateDynamicFields() {
            const isContact = document.getElementById('chk_contact').checked;
            const isPartner = document.getElementById('chk_partner').checked;
            const isMasterclass = document.getElementById('chk_masterclass').checked;
            const isWaitlist = document.getElementById('chk_waitlist').checked;
            
            document.getElementById('dyn_contact').style.display = isContact ? 'block' : 'none';
            document.getElementById('dyn_partner').style.display = isPartner ? 'block' : 'none';
            document.getElementById('dyn_b2b').style.display = (isPartner || isContact || isMasterclass) ? 'flex' : 'none';
            document.getElementById('dyn_invest').style.display = (isMasterclass || isWaitlist) ? 'block' : 'none';
            
            // Toggle required attributes
            document.getElementById('message').required = isContact;
            document.getElementById('partnertype').required = isPartner;
        }

        // Setup listeners
        document.addEventListener("DOMContentLoaded", function() {
            if(document.getElementById('chk_contact')) document.getElementById('chk_contact').addEventListener('change', updateDynamicFields);
            if(document.getElementById('chk_partner')) document.getElementById('chk_partner').addEventListener('change', updateDynamicFields);
            if(document.getElementById('chk_masterclass')) document.getElementById('chk_masterclass').addEventListener('change', updateDynamicFields);
            if(document.getElementById('chk_waitlist')) document.getElementById('chk_waitlist').addEventListener('change', updateDynamicFields);
            
            const phoneInput = document.querySelector("#phone_intl");
            if (phoneInput) {
                iti = window.intlTelInput(phoneInput, {
                    utilsScript: "https://cdn.jsdelivr.net/npm/intl-tel-input@18.2.1/build/js/utils.js",
                    preferredCountries: ['us', 'gb', 'ca', 'au', 'es'],
                    separateDialCode: true
                });
            }
        });
        
        let isOpening = false;
        function openUnifiedModal(sourceType) {
            if(isOpening) return;
            isOpening = true;
            
            if(document.getElementById('waitlistModal')) {
                document.getElementById('waitlistModal').style.display = 'flex';
                document.getElementById('form_message').style.display = 'none';
            }
            
            // Uncheck all main interests first
            if(document.getElementById('chk_waitlist')) document.getElementById('chk_waitlist').checked = false;
            if(document.getElementById('chk_masterclass')) document.getElementById('chk_masterclass').checked = false;
            if(document.getElementById('chk_partner')) document.getElementById('chk_partner').checked = false;
            if(document.getElementById('chk_contact')) document.getElementById('chk_contact').checked = false;
            if(document.getElementById('chk_newsletter')) document.getElementById('chk_newsletter').checked = false;
            
            // Always keep newsletter subscription checked by default
            if(document.getElementById('chk_subscription')) document.getElementById('chk_subscription').checked = true;

            // Check based on source
            if (sourceType === 'waitlist') {
                if(document.getElementById('chk_waitlist')) document.getElementById('chk_waitlist').checked = true;
            } else if (sourceType === 'masterclass') {
                if(document.getElementById('chk_masterclass')) document.getElementById('chk_masterclass').checked = true;
            } else if (sourceType === 'partner') {
                if(document.getElementById('chk_partner')) document.getElementById('chk_partner').checked = true;
            } else if (sourceType === 'contact') {
                if(document.getElementById('chk_contact')) document.getElementById('chk_contact').checked = true;
            } else if (sourceType === 'newsletter') {
                if(document.getElementById('chk_newsletter')) document.getElementById('chk_newsletter').checked = true;
            }

            updateDynamicFields();
            isOpening = false;
        }

        function submitMailchimpJSONP(form) {
            const btn = document.getElementById('submit_btn');
            btn.innerText = 'SENDING...';
            btn.disabled = true;
            
            // Collect interests
            let interests = [];
            if (document.getElementById('chk_masterclass') && document.getElementById('chk_masterclass').checked) interests.push("Masterclass");
            if (document.getElementById('chk_waitlist') && document.getElementById('chk_waitlist').checked) interests.push("Waitlist");
            if (document.getElementById('chk_partner') && document.getElementById('chk_partner').checked) interests.push("Partner");
            if (document.getElementById('chk_contact') && document.getElementById('chk_contact').checked) interests.push("Contact");
            if (document.getElementById('chk_newsletter') && document.getElementById('chk_newsletter').checked) interests.push("Newsletter");
            
            if (interests.length === 0) {
                interests.push("No specific interest");
            }

            document.getElementById('unifiedSource').value = interests.join(", ");

            const params = new URLSearchParams();
            const formData = new FormData(form);
            for (const [key, value] of formData.entries()) {
                params.append(key, value);
            }
            
            // Append formatted phone using intl-tel-input
            if(iti && iti.isValidNumber()) {
                params.append('PHONE', iti.getNumber());
            } else if (iti) {
                params.append('PHONE', document.getElementById('phone_intl').value);
            }
            
            // Add honeypot
            params.append('b_4766d7bd8debcf610dadddfb6_53677e9563', '');
            
            // JSONP callback
            const callbackName = 'mcCallback' + Math.round(100000 * Math.random());
            params.append('c', callbackName);
            
            const url = "https://buildyourcastle.us10.list-manage.com/subscribe/post-json?u=4766d7bd8debcf610dadddfb6&id=53677e9563&" + params.toString();
            
            window[callbackName] = function(data) {
                btn.innerText = 'SUBMIT';
                btn.disabled = false;
                const msgDiv = document.getElementById('form_message');
                msgDiv.style.display = 'block';
                if (data.result === 'success') {
                    msgDiv.style.backgroundColor = '#D1FAE5';
                    msgDiv.style.color = '#065F46';
                    msgDiv.innerHTML = 'Thank you! We have successfully received your information.';
                    form.reset();
                    updateDynamicFields();
                    setTimeout(() => { 
                        if(document.getElementById('waitlistModal')) document.getElementById('waitlistModal').style.display='none'; 
                        msgDiv.style.display='none'; 
                    }, 4000);
                } else {
                    msgDiv.style.backgroundColor = '#FEE2E2';
                    msgDiv.style.color = '#991B1B';
                    msgDiv.innerHTML = 'There was an error: ' + data.msg;
                }
                delete window[callbackName];
                document.body.removeChild(script);
            };
            
            const script = document.createElement('script');
            script.src = url;
            document.body.appendChild(script);
        }
    </script>
    <!-- INJECTED UNIFIED MODAL END -->
    """
    
    # Insert new js before </body>
    if '</body>' in content:
        content = content.replace('</body>', new_js + '\n</body>')
    else:
        content += new_js

    # Clean up duplicate <script src="./js/mailchimp.js"></script> if any remaining outside the modal
    content = content.replace('<script src="./js/mailchimp.js"></script>', '')

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Processed {filename}")

pages = ['index.html', 'about.html', 'masterclass.html', 'partners.html', 'contact.html']
for p in pages:
    process_file(p)
