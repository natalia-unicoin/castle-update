import re

with open('contact.html', 'r', encoding='utf-8') as f:
    content = f.read()

contact_section = """
    <!-- Contact Form Section -->
    <section class="snap-section" style="background-color: #F8F8FA; padding: 100px 4vw; display: flex; justify-content: center; align-items: center;">
        <div class="container" style="max-width: 800px; width: 100%; background: #FFFFFF; border-radius: 12px; padding: 60px 40px; box-shadow: 0 20px 40px rgba(0,0,0,0.05); border: 1px solid #E5E7EB;">
            <div style="text-align: center; margin-bottom: 40px;">
                <h2 style="font-size: clamp(32px, 5vw, 48px); font-weight: 800; color: #1A1A1A; line-height: 1.2; letter-spacing: -1px; margin-bottom: 16px; font-family: 'Inter', sans-serif;">Get in Touch</h2>
                <p style="font-size: 18px; color: #4B5563; font-family: 'Inter', sans-serif; line-height: 1.6; max-width: 500px; margin: 0 auto;">
                    Have a question, partnership idea, or just want to say hello? Drop us a message below and our team will get back to you.
                </p>
            </div>
            
            <form action="#" method="POST" class="waitlist-form" style="display: grid; gap: 24px; text-align: left;">
                <div class="form-row" style="display: grid; grid-template-columns: 1fr 1fr; gap: 24px;">
                    <div class="form-group" style="display: flex; flex-direction: column;">
                        <label for="contact-fname" style="font-size: 14px; font-weight: 600; color: #1A1A1A; margin-bottom: 8px;">First Name *</label>
                        <input type="text" id="contact-fname" name="FNAME" required placeholder="Jane" style="padding: 16px; border: 1px solid #D1D5DB; border-radius: 6px; font-size: 15px; font-family: 'Inter', sans-serif; background: #F9FAFB; transition: border-color 0.2s, box-shadow 0.2s; color:#1A1A1A;">
                    </div>
                    <div class="form-group" style="display: flex; flex-direction: column;">
                        <label for="contact-lname" style="font-size: 14px; font-weight: 600; color: #1A1A1A; margin-bottom: 8px;">Last Name *</label>
                        <input type="text" id="contact-lname" name="LNAME" required placeholder="Doe" style="padding: 16px; border: 1px solid #D1D5DB; border-radius: 6px; font-size: 15px; font-family: 'Inter', sans-serif; background: #F9FAFB; transition: border-color 0.2s, box-shadow 0.2s; color:#1A1A1A;">
                    </div>
                </div>

                <div class="form-group" style="display: flex; flex-direction: column;">
                    <label for="contact-email" style="font-size: 14px; font-weight: 600; color: #1A1A1A; margin-bottom: 8px;">Email Address *</label>
                    <input type="email" id="contact-email" name="EMAIL" required placeholder="jane@example.com" style="padding: 16px; border: 1px solid #D1D5DB; border-radius: 6px; font-size: 15px; font-family: 'Inter', sans-serif; background: #F9FAFB; transition: border-color 0.2s, box-shadow 0.2s; color:#1A1A1A;">
                </div>

                <div class="form-group" style="display: flex; flex-direction: column;">
                    <label for="contact-subject" style="font-size: 14px; font-weight: 600; color: #1A1A1A; margin-bottom: 8px;">Subject *</label>
                    <select id="contact-subject" name="SUBJECT" required style="padding: 16px; border: 1px solid #D1D5DB; border-radius: 6px; font-size: 15px; font-family: 'Inter', sans-serif; background: #F9FAFB; transition: border-color 0.2s, box-shadow 0.2s; color:#1A1A1A; appearance: none; background-image: url('data:image/svg+xml;charset=US-ASCII,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20width%3D%2216%22%20height%3D%2216%22%20fill%3D%22%23111111%22%20viewBox%3D%220%200%2016%2016%22%3E%3Cpath%20d%3D%22M4.293%205.293a1%201%200%200%201%201.414%200L8%208.586l2.293-2.293a1%201%200%201%201%201.414%201.414l-3%203a1%201%200%200%201-1.414%200l-3-3a1%201%200%200%201%200-1.414z%22%2F%3E%3C%2Fsvg%3E'); background-repeat: no-repeat; background-position: right 16px center; background-size: 16px;">
                        <option value="" disabled selected>Select a topic</option>
                        <option value="Partnerships">Partnerships</option>
                        <option value="Press / Media">Press / Media</option>
                        <option value="Masterclass Inquiry">Masterclass Inquiry</option>
                        <option value="General Inquiry">General Inquiry</option>
                    </select>
                </div>

                <div class="form-group" style="display: flex; flex-direction: column;">
                    <label for="contact-message" style="font-size: 14px; font-weight: 600; color: #1A1A1A; margin-bottom: 8px;">Your Message *</label>
                    <textarea id="contact-message" name="MESSAGE" required rows="5" placeholder="How can we help you?" style="padding: 16px; border: 1px solid #D1D5DB; border-radius: 6px; font-size: 15px; font-family: 'Inter', sans-serif; background: #F9FAFB; transition: border-color 0.2s, box-shadow 0.2s; color:#1A1A1A; resize: vertical;"></textarea>
                </div>

                <button type="submit" style="background-color: #A03FA3; color: #FFFFFF; font-weight: 800; letter-spacing: 2px; padding: 20px 40px; border-radius: 50px; font-size: 15px; border: none; cursor: pointer; transition: transform 0.2s, box-shadow 0.2s; margin-top: 10px; width: 100%; text-transform: uppercase;">Send Message</button>
            </form>
        </div>
    </section>

    <!-- Additional required CSS for focus states -->
    <style>
        .waitlist-form input:focus, .waitlist-form select:focus, .waitlist-form textarea:focus {
            border-color: #A03FA3 !important;
            box-shadow: 0 0 0 3px rgba(160,63,163,0.1) !important;
            outline: none !important;
            background: #FFFFFF !important;
        }
        .waitlist-form button:hover {
            transform: translateY(-3px) !important;
            box-shadow: 0 15px 30px rgba(160, 63, 163, 0.4) !important;
            background-color: #B85AB8 !important;
        }
        @media(max-width: 600px) {
            .form-row { grid-template-columns: 1fr !important; }
        }
    </style>
"""

# Find where to inject: after the Hero section, before the footer.
# The hero section ends with </section>. The footer starts with <footer class="site-footer">
pattern = re.compile(r'(</section>\s*)(\s*<footer class="site-footer">)')
if pattern.search(content):
    new_content = pattern.sub(r'\1' + contact_section + r'\2', content)
    with open('contact.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Form injected successfully.")
else:
    print("Could not find injection point.")
