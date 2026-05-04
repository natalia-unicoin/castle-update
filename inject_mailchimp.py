import glob
import re

files = glob.glob("*.html")
files = [f for f in files if "backup" not in f]

mailchimp_url = "https://buildyourcastle.us10.list-manage.com/subscribe/post?u=4766d7bd8debcf610dadddfb6&amp;id=53677e9563&amp;f_id=0079ece5f0"
honeypot = '<div aria-hidden="true" style="position: absolute; left: -5000px;"><input type="text" name="b_4766d7bd8debcf610dadddfb6_53677e9563" tabindex="-1" value=""></div>'

for f in files:
    with open(f, "r") as file:
        content = file.read()
    
    # 1. Waitlist forms: replace YOUR_MAILCHIMP_URL_HERE
    content = content.replace('action="YOUR_MAILCHIMP_URL_HERE"', f'action="{mailchimp_url}" target="_blank"')
    
    # 2. Contact form main: replace action="#" class="waitlist-form"
    content = content.replace('action="#" method="POST" class="waitlist-form"', f'action="{mailchimp_url}" method="POST" class="waitlist-form" target="_blank"')
    
    # 3. Add honeypot field to waitlist forms. It usually goes right before the submit button, but anywhere inside the <form> is fine.
    # The forms look like: <form ... class="waitlist-form"> ... </form>
    # We can inject it right after the opening form tag.
    # Wait, using regex for the waitlist-form opening tag
    content = re.sub(r'(<form[^>]*class="waitlist-form"[^>]*>)', r'\1\n                ' + honeypot, content)
    
    # 4. Newsletter forms:
    # From: <form class="subscribe-form" onsubmit="event.preventDefault(); alert('Subscribed to Newsletter!');" ...>
    # To: <form action="MAILCHIMP_URL" method="POST" target="_blank" class="subscribe-form" ...>
    content = re.sub(
        r'<form class="subscribe-form" onsubmit="[^"]*"',
        f'<form action="{mailchimp_url}" method="POST" target="_blank" class="subscribe-form"',
        content
    )
    
    # Add name="EMAIL" to the subscribe input if it doesn't have it
    # From: <input type="email" class="subscribe-input"
    # To: <input type="email" name="EMAIL" class="subscribe-input"
    content = content.replace('<input type="email" class="subscribe-input"', '<input type="email" name="EMAIL" class="subscribe-input"')
    
    # Inject honeypot into subscribe-form too
    content = re.sub(r'(<form[^>]*class="subscribe-form"[^>]*>)', r'\1\n                ' + honeypot, content)
    
    with open(f, "w") as file:
        file.write(content)

print("Mailchimp integration injected into all files.")
