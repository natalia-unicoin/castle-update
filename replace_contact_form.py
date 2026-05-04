import re

with open('contact.html', 'r', encoding='utf-8') as f:
    content = f.read()

new_contact_section = """
    <!-- Contact Form Section (Waitlist Style) -->
    <section class="snap-section" style="background-color: #F8F8FA; padding: 100px 4vw; display: flex; justify-content: center; align-items: center;">
        <div class="container" style="max-width: 700px; width: 100%; background: #FFFFFF; border-radius: 8px; padding: 60px 40px; box-shadow: 0 40px 100px rgba(0,0,0,0.1); border: 1px solid #E5E7EB; text-align: left;">
            <div style="text-align: center; margin-bottom: 40px;">
                <h2 style="font-size: clamp(36px, 6vw, 56px); font-weight: 800; color: #1A1A1A; line-height: 1.1; letter-spacing: -2px; margin-bottom: 16px; font-family: 'Inter', sans-serif;">Contact Us</h2>
                <p style="font-size: 16px; color: #2A2A2A; font-family: 'Inter', sans-serif; line-height: 1.5; max-width: 500px; margin: 0 auto;">
                    Have a question, partnership idea, or just want to say hello? Drop us a message below and our team will get back to you.
                </p>
            </div>
            
            <form action="#" method="POST" class="waitlist-form">
                
                <div class="form-row">
                    <div class="form-group">
                        <label for="fname">Full Name *</label>
                        <input type="text" id="fname" name="FNAME" required placeholder="Jane Doe">
                    </div>
                    <div class="form-group">
                        <label for="email">Email Address *</label>
                        <input type="email" id="email" name="EMAIL" required placeholder="jane@example.com">
                    </div>
                </div>

                <div class="form-row">
                    <div class="form-group">
                        <label for="phone">Phone Number</label>
                        <input type="tel" id="phone" name="PHONE" placeholder="+1 234 567 8900">
                    </div>
                    <div class="form-group">
                        <label for="age">Age</label>
                        <input type="number" id="age" name="AGE" placeholder="30">
                    </div>
                </div>

                <div class="form-row">
                    <div class="form-group">
                        <label for="country">Country</label>
                        <select id="country" name="COUNTRY">
                            <option value="" disabled selected>Select your country</option>
                            <option value="United States">United States</option>
                            <option value="United Kingdom">United Kingdom</option>
                            <option value="Canada">Canada</option>
                            <option value="Australia">Australia</option>
                            <option value="Argentina">Argentina</option>
                            <option value="Brazil">Brazil</option>
                            <option value="Chile">Chile</option>
                            <option value="Colombia">Colombia</option>
                            <option value="Mexico">Mexico</option>
                            <option value="Peru">Peru</option>
                            <option value="Spain">Spain</option>
                            <option value="Other">Other</option>
                        </select>
                    </div>
                    <div class="form-group">
                        <label for="linkedin">LinkedIn URL</label>
                        <input type="url" id="linkedin" name="LINKEDIN" placeholder="https://linkedin.com/in/janedoe">
                    </div>
                </div>

                <div class="form-row">
                    <div class="form-group">
                        <label for="company">Company / Organization</label>
                        <input type="text" id="company" name="COMPANY" placeholder="Acme Corp">
                    </div>
                    <div class="form-group">
                        <label for="role">Your Role / Title</label>
                        <input type="text" id="role" name="ROLE" placeholder="Founder">
                    </div>
                </div>

                <div class="form-group">
                    <label for="instagram">Instagram Handle</label>
                    <input type="text" id="instagram" name="INSTAGRAM" placeholder="@janedoe">
                </div>

                <div class="form-group" style="margin-top: 20px;">
                    <label for="message">Tell us *</label>
                    <textarea id="message" name="MESSAGE" required rows="4" placeholder="Why are you contacting us?" style="padding: 14px 16px; border: 1px solid #D1D5DB; border-radius: 6px; font-size: 15px; font-family: 'Inter', sans-serif; background: #F9FAFB; transition: border-color 0.2s, box-shadow 0.2s; color:#1A1A1A; resize: vertical;"></textarea>
                </div>

                <div class="checkbox-group" style="margin-top: 20px;">
                    <input type="checkbox" id="consent" name="CONSENT" required>
                    <label for="consent">I consent to Castle contacting me to share updates about the platform, launch information, and Community events.</label>
                </div>

                <button type="submit" class="waitlist-submit" style="margin-top: 20px; font-weight: 800; text-transform: none; letter-spacing: 0;">Contact Us</button>
            </form>
        </div>
    </section>
"""

# Regex to find my previously injected Contact Form block and replace it.
pattern = re.compile(r'    <!-- Contact Form Section -->.*?    </style>\n', re.DOTALL)

if pattern.search(content):
    content = pattern.sub(new_contact_section, content)
    with open('contact.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Replaced with waitlist-style form.")
else:
    print("Old form block not found.")

