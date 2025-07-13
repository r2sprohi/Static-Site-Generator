from split_images_links import split_nodes_link, split_nodes_image
from split_node_delimiter import split_nodes_delimiter
from textnode import TextNode, TextType
def text_to_textnodes(text):
    if not text:
        return []
    original_text_node = [TextNode(text=text, text_type= TextType.TEXT)]
    new_text_nodes= split_nodes_link(split_nodes_image(original_text_node))
    delimiters = [('**', TextType.BOLD), ('_',TextType.ITALIC), ('`',TextType.CODE)]
    for delimiter in delimiters:
        sign , texttype = delimiter 
        new_text_nodes = split_nodes_delimiter(new_text_nodes, sign , texttype)
    
    return new_text_nodes



    
