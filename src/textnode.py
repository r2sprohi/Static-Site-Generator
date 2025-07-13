from enum import Enum,auto
from htmlnode import LeafNode

class TextType(Enum):
    TEXT = auto()
    BOLD= auto()
    ITALIC = auto()
    CODE = auto()
    LINK = auto()
    IMAGE = auto()


class TextNode:
    def __init__(self,text,text_type, url=None):
        if not isinstance(text_type, TextType):
            raise Exception("text_type must be a member of the TextType enum.")
        self.text = text
        self.text_type = text_type
        self.url = url
    def __eq__(self,other):
        if not isinstance(other,TextNode):
            return NotImplemented
        return self.text == other.text and self.text_type == other.text_type and self.url == other.url
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"

def text_node_to_html_node(text_node):
    if not isinstance(text_node.text_type,TextType):
        raise Exception("Not a valid text type")
    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(tag = None,value = text_node.text)
        case TextType.BOLD:
            return LeafNode(tag = 'b' ,value = text_node.text)
        case TextType.ITALIC:
            return LeafNode(tag = 'i', value = text_node.text)
        case TextType.CODE:
            return LeafNode(tag = 'code', value = text_node.text)
        case TextType.LINK:
            return LeafNode(tag = 'a', value = text_node.text, props = {'href':text_node.url})
        case TextType.IMAGE:
            return LeafNode(tag = 'img',value = '', props = {'src':text_node.url, 'alt':text_node.text})
        case _:
            raise Exception("Invalid Type")    


