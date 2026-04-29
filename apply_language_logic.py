import os
import glob

html_files = glob.glob("/Users/Nati/.gemini/antigravity/scratch/Castle_V3_Standalone/*.html")

script_to_inject = """
    <!-- Language Auto-Detection -->
    <script>
        if (!localStorage.getItem('lang_selected')) {
            var lang = navigator.language || navigator.userLanguage;
            var isSpanish = lang.startsWith('es');
            var currentPath = window.location.pathname;
            var isCurrentSpanish = currentPath.indexOf('_es.html') !== -1;
            
            if (isSpanish && !isCurrentSpanish) {
                var newPage = currentPath.split('/').pop();
                if (!newPage || newPage === '/') newPage = 'index.html';
                window.location.replace(newPage.replace('.html', '_es.html'));
            } else if (!isSpanish && isCurrentSpanish) {
                var newPage = currentPath.split('/').pop();
                if (!newPage || newPage === '/') newPage = 'index_es.html';
                window.location.replace(newPage.replace('_es.html', '.html'));
            }
        }
    </script>
</head>"""

for file in html_files:
    # Skip backup files
    if "backup" in file:
        continue
        
    with open(file, "r") as f:
        content = f.read()

    is_es = "_es.html" in file
    
    # 1. Update logo link
    if is_es:
        content = content.replace('<a href="/" class="header-logo">', '<a href="index_es.html" class="header-logo">')
    else:
        content = content.replace('<a href="/" class="header-logo">', '<a href="index.html" class="header-logo">')
        
    # 2. Update language selector to set localStorage
    old_select = 'onchange="if(this.value) window.location.href=this.value"'
    new_select = 'onchange="if(this.value) { localStorage.setItem(\'lang_selected\', \'true\'); window.location.href=this.value; }"'
    content = content.replace(old_select, new_select)
    
    # 3. Inject language auto-detection script before </head> if not already there
    if "localStorage.getItem('lang_selected')" not in content:
        content = content.replace("</head>", script_to_inject)
        
    with open(file, "w") as f:
        f.write(content)

print("Applied language logic to all html files.")
