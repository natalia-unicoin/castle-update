with open('index_es.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

start_idx = -1
end_idx = -1
for i, line in enumerate(lines):
    if "<!-- Challenge Teaser -->" in line:
        start_idx = i
    if start_idx != -1 and i > start_idx and "</section>" in line:
        end_idx = i
        break

if start_idx != -1 and end_idx != -1:
    challenge_block = lines[start_idx:end_idx+1]
    
    # Remove from original location
    del lines[start_idx:end_idx+1]
    
    # Find insert location (before #2.5 Ecosystem Stack)
    insert_idx = -1
    for i, line in enumerate(lines):
        if "<!-- #2.5 Ecosystem Stack -->" in line:
            insert_idx = i
            break
            
    if insert_idx != -1:
        # Update text inside the block
        block_text = "".join(challenge_block)
        
        # Replace title
        block_text = block_text.replace(
            "The Castle Wealth Reset<br>&amp; Rewire Challenge™", 
            "Deja de gestionar el dinero.<br>Empieza a construir riqueza."
        )
        
        # Replace subtitle
        block_text = block_text.replace(
            "A focused 21 days sprint designed to rewire your financial habits and help you build your first intelligent portfolio alongside thousands of other driven Women.",
            "La Masterclass Castle es el primer paso de tu reset financiero. Programa diseñado para cambiar como piensas, como decides y como actúas con el dinero."
        )
        
        # Replace CTA
        block_text = block_text.replace(
            "UNITE A LA LISTA DE ESPERA",
            "ACCEDER A LA MASTERCLASS"
        )
        
        # Insert back
        lines.insert(insert_idx, block_text + "\n")
        
        with open('index_es.html', 'w', encoding='utf-8') as f:
            f.writelines(lines)
        print("Successfully moved and translated block.")
    else:
        print("Could not find insert location.")
else:
    print("Could not find challenge block.")
