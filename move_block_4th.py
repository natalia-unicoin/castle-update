import re

def move_challenge_to_4th(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the challenge teaser section
    pattern = r'(<!-- Challenge Teaser -->\s*<section.*?</section>\n)'
    match = re.search(pattern, content, re.DOTALL)
    if not match:
        print(f"Could not find Challenge Teaser in {filename}")
        return
    
    challenge_block = match.group(1)
    
    # Remove from current location
    content = content.replace(challenge_block, '')
    
    # Find insertion point: right before <!-- #4 What Makes Us Different -->
    insert_marker = '<!-- #4 What Makes Us Different -->'
    if insert_marker not in content:
        print(f"Could not find {insert_marker} in {filename}")
        return
        
    content = content.replace(insert_marker, challenge_block + '\n    ' + insert_marker)
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print(f"Successfully moved Challenge Teaser in {filename}")

move_challenge_to_4th('index.html')
move_challenge_to_4th('index_es.html')
