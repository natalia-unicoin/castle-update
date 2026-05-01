import os
import glob

def main():
    directory = '/Users/Nati/.gemini/antigravity/scratch/Castle_V3_Standalone'
    html_files = glob.glob(os.path.join(directory, '*.html'))
    
    old_linkedin = '<svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z"></path><rect x="2" y="9" width="4" height="12"></rect><circle cx="4" cy="4" r="2"></circle></svg>'
    new_linkedin = '<svg viewBox="0 0 24 24" width="20" height="20"><circle cx="12" cy="12" r="12" fill="currentColor"/><path fill="#fff" d="M8 17H5V9h3v8zM6.5 7.7a1.6 1.6 0 1 1 0-3.2 1.6 1.6 0 0 1 0 3.2zM19 17h-3v-4.5c0-1.1-.4-1.8-1.3-1.8-.7 0-1.2.5-1.4 1-.1.2-.1.5-.1.8V17h-3V9h3v1.2a3 3 0 0 1 2.7-1.5c2 0 3.5 1.3 3.5 4.1V17z"/></svg>'
    
    old_email = '<svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"></path><polyline points="22,6 12,13 2,6"></polyline></svg>'
    new_email = '<svg viewBox="0 0 24 24" width="20" height="20"><circle cx="12" cy="12" r="12" fill="currentColor"/><path fill="#fff" d="M18 8H6a1 1 0 0 0-1 1v6a1 1 0 0 0 1 1h12a1 1 0 0 0 1-1V9a1 1 0 0 0-1-1zm-.5 2l-4.7 3.1a1 1 0 0 1-1.1 0L7 10h10.5z"/></svg>'

    old_ig = '<svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="2" width="20" height="20" rx="5" ry="5"></rect><path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"></path><line x1="17.5" y1="6.5" x2="17.51" y2="6.5"></line></svg>'
    new_ig = '<svg viewBox="0 0 24 24" width="20" height="20"><circle cx="12" cy="12" r="12" fill="currentColor"/><path fill="#fff" d="M15.5 6h-7C7.1 6 6 7.1 6 8.5v7C6 16.9 7.1 18 8.5 18h7c1.4 0 2.5-1.1 2.5-2.5v-7C18 7.1 16.9 6 15.5 6zM12 15a3 3 0 1 1 0-6 3 3 0 0 1 0 6zm3-5a1 1 0 1 1 0-2 1 1 0 0 1 0 2zM12 10.5a1.5 1.5 0 1 0 0 3 1.5 1.5 0 0 0 0-3z"/></svg>'

    old_yt = '<svg viewBox="0 0 24 24" width="20" height="20" fill="currentColor"><path d="M21.582,6.186c-0.23-0.86-0.908-1.538-1.768-1.768C18.254,4,12,4,12,4S5.746,4,4.186,4.418c-0.86,0.23-1.538,0.908-1.768,1.768C2,7.746,2,12,2,12s0,4.254,0.418,5.814c0.23,0.86,0.908,1.538,1.768,1.768C5.746,20,12,20,12,20s6.254,0,7.814-0.418c0.86-0.23,1.538-0.908,1.768-1.768C22,16.254,22,12,22,12S22,7.746,21.582,6.186z M9.799,15.276V8.724l5.632,3.276L9.799,15.276z"/></svg>'
    new_yt = '<svg viewBox="0 0 24 24" width="20" height="20"><circle cx="12" cy="12" r="12" fill="currentColor"/><path fill="#fff" d="M17.8 8.4c-.2-.7-.7-1.2-1.4-1.4-1.2-.3-6.4-.3-6.4-.3s-5.2 0-6.4.3c-.7.2-1.2.7-1.4 1.4C2 9.6 2 12 2 12s0 2.4.2 3.6c.2.7.7 1.2 1.4 1.4 1.2.3 6.4.3 6.4.3s5.2 0 6.4-.3c.7-.2 1.2-.7 1.4-1.4.2-1.2.2-3.6.2-3.6s0-2.4-.2-3.6zM10 14.5V9.5l4.5 2.5-4.5 2.5z"/></svg>'

    old_x = '<svg viewBox="0 0 24 24" width="20" height="20" fill="currentColor"><path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z"/></svg>'
    new_x = '<svg viewBox="0 0 24 24" width="20" height="20"><circle cx="12" cy="12" r="12" fill="currentColor"/><path fill="#fff" d="M15.5 7h1.6l-3.5 4 4.1 5.4h-3.2l-2.5-3.3-2.9 3.3h-1.6l3.7-4.2-3.9-5.2h3.3l2.2 3 2.5-3zm-1.2 8.3L9 7.8H7.7l6.2 8.1h1.3z"/></svg>'
    
    for f in html_files:
        with open(f, 'r') as file:
            content = file.read()
            
        new_content = content.replace(old_linkedin, new_linkedin)
        new_content = new_content.replace(old_email, new_email)
        new_content = new_content.replace(old_ig, new_ig)
        new_content = new_content.replace(old_yt, new_yt)
        new_content = new_content.replace(old_x, new_x)
        
        if content != new_content:
            with open(f, 'w') as file:
                file.write(new_content)
            print(f"Updated {f}")

if __name__ == '__main__':
    main()
