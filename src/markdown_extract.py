import re
def extract_markdown_images(text):
    markdown_img = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)",text)
    return markdown_img
def extract_markdown_url(text): 
    markdown_url = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)",text)
    return markdown_url


    
