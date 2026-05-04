import os
import glob

html_files = glob.glob('*.html')

old_input = '<input type="number" id="age" name="AGE" placeholder="30">'
new_select = """<select id="age" name="AGE">
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
                        </select>"""

for fname in html_files:
    with open(fname, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if old_input in content:
        content = content.replace(old_input, new_select)
        with open(fname, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {fname}")

