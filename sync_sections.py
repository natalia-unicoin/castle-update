import re

def sync_html_block(source, dest, start_tag, end_tag):
    pattern = re.compile(f"{start_tag}.*?{end_tag}", re.DOTALL)
    source_match = pattern.search(source)
    if source_match:
        return pattern.sub(lambda m: source_match.group(0), dest, count=1)
    return dest
