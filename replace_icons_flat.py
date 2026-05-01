import os
import glob

def main():
    directory = '/Users/Nati/.gemini/antigravity/scratch/Castle_V3_Standalone'
    html_files = glob.glob(os.path.join(directory, '*.html'))
    
    old_linkedin = '<svg viewBox="0 0 24 24" width="20" height="20"><circle cx="12" cy="12" r="12" fill="currentColor"/><path fill="#fff" d="M8 17H5V9h3v8zM6.5 7.7a1.6 1.6 0 1 1 0-3.2 1.6 1.6 0 0 1 0 3.2zM19 17h-3v-4.5c0-1.1-.4-1.8-1.3-1.8-.7 0-1.2.5-1.4 1-.1.2-.1.5-.1.8V17h-3V9h3v1.2a3 3 0 0 1 2.7-1.5c2 0 3.5 1.3 3.5 4.1V17z"/></svg>'
    new_linkedin = '<svg viewBox="0 0 24 24" width="20" height="20" fill="currentColor"><path d="M19 0h-14c-2.761 0-5 2.239-5 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5v-14c0-2.761-2.238-5-5-5zm-11 19h-3v-11h3v11zm-1.5-12.268c-.966 0-1.75-.79-1.75-1.764s.784-1.764 1.75-1.764 1.75.79 1.75 1.764-.783 1.764-1.75 1.764zm13.5 12.268h-3v-5.604c0-3.368-4-3.113-4 0v5.604h-3v-11h3v1.765c1.396-2.586 7-2.777 7 2.476v6.759z"/></svg>'
    
    old_email = '<svg viewBox="0 0 24 24" width="20" height="20"><circle cx="12" cy="12" r="12" fill="currentColor"/><path fill="#fff" d="M18 8H6a1 1 0 0 0-1 1v6a1 1 0 0 0 1 1h12a1 1 0 0 0 1-1V9a1 1 0 0 0-1-1zm-.5 2l-4.7 3.1a1 1 0 0 1-1.1 0L7 10h10.5z"/></svg>'
    new_email = '<svg viewBox="0 0 24 24" width="20" height="20" fill="currentColor"><path d="M0 3v18h24v-18h-24zm21.518 2l-9.518 7.713-9.518-7.713h19.036zm-19.518 14v-11.817l10 8.104 10-8.104v11.817h-20z"/></svg>'

    old_ig = '<svg viewBox="0 0 24 24" width="20" height="20"><circle cx="12" cy="12" r="12" fill="currentColor"/><path fill="#fff" d="M15.5 6h-7C7.1 6 6 7.1 6 8.5v7C6 16.9 7.1 18 8.5 18h7c1.4 0 2.5-1.1 2.5-2.5v-7C18 7.1 16.9 6 15.5 6zM12 15a3 3 0 1 1 0-6 3 3 0 0 1 0 6zm3-5a1 1 0 1 1 0-2 1 1 0 0 1 0 2zM12 10.5a1.5 1.5 0 1 0 0 3 1.5 1.5 0 0 0 0-3z"/></svg>'
    new_ig = '<svg viewBox="0 0 24 24" width="20" height="20" fill="currentColor"><path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zm0-2.163c-3.259 0-3.667.014-4.947.072-4.358.2-6.78 2.618-6.98 6.98-.059 1.281-.073 1.689-.073 4.948 0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98 1.281.058 1.689.072 4.948.072 3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98-1.281-.059-1.69-.073-4.949-.073zm0 5.838c-3.403 0-6.162 2.759-6.162 6.162s2.759 6.163 6.162 6.163 6.162-2.759 6.162-6.163c0-3.403-2.759-6.162-6.162-6.162zm0 10.162c-2.209 0-4-1.79-4-4 0-2.209 1.791-4 4-4s4 1.791 4 4c0 2.21-1.791 4-4 4zm6.406-11.845c-.796 0-1.441.645-1.441 1.44s.645 1.44 1.441 1.44c.795 0 1.439-.645 1.439-1.44s-.644-1.44-1.439-1.44z"/></svg>'

    old_x = '<svg viewBox="0 0 24 24" width="20" height="20"><circle cx="12" cy="12" r="12" fill="currentColor"/><path fill="#fff" d="M15.5 7h1.6l-3.5 4 4.1 5.4h-3.2l-2.5-3.3-2.9 3.3h-1.6l3.7-4.2-3.9-5.2h3.3l2.2 3 2.5-3zm-1.2 8.3L9 7.8H7.7l6.2 8.1h1.3z"/></svg>'
    new_x = '<svg viewBox="0 0 24 24" width="20" height="20" fill="currentColor"><path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z"/></svg>'

    # YouTube didn't have a circle initially, we added it. But actually old_yt might be the circle one now.
    old_yt = '<svg viewBox="0 0 24 24" width="20" height="20"><circle cx="12" cy="12" r="12" fill="currentColor"/><path fill="#fff" d="M17.8 8.4c-.2-.7-.7-1.2-1.4-1.4-1.2-.3-6.4-.3-6.4-.3s-5.2 0-6.4.3c-.7.2-1.2.7-1.4 1.4C2 9.6 2 12 2 12s0 2.4.2 3.6c.2.7.7 1.2 1.4 1.4 1.2.3 6.4.3 6.4.3s5.2 0 6.4-.3c.7-.2 1.2-.7 1.4-1.4.2-1.2.2-3.6.2-3.6s0-2.4-.2-3.6zM10 14.5V9.5l4.5 2.5-4.5 2.5z"/></svg>'
    new_yt = '<svg viewBox="0 0 24 24" width="20" height="20" fill="currentColor"><path d="M21.582,6.186c-0.23-0.86-0.908-1.538-1.768-1.768C18.254,4,12,4,12,4S5.746,4,4.186,4.418c-0.86,0.23-1.538,0.908-1.768,1.768C2,7.746,2,12,2,12s0,4.254,0.418,5.814c0.23,0.86,0.908,1.538,1.768,1.768C5.746,20,12,20,12,20s6.254,0,7.814-0.418c0.86-0.23,1.538-0.908,1.768-1.768C22,16.254,22,12,22,12S22,7.746,21.582,6.186z M9.799,15.276V8.724l5.632,3.276L9.799,15.276z"/></svg>'

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
