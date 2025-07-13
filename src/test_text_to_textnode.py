from text_to_textnode import text_to_textnodes
from textnode import TextNode, TextType

import unittest

class TextToTextNode(unittest.TestCase):
    def test_case_1(self):
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        output_nodes = text_to_textnodes(text)
        nodes = [
        TextNode("This is ", TextType.TEXT),
        TextNode("text", TextType.BOLD),
        TextNode(" with an ", TextType.TEXT),
        TextNode("italic", TextType.ITALIC),
        TextNode(" word and a ", TextType.TEXT),
        TextNode("code block", TextType.CODE),
        TextNode(" and an ", TextType.TEXT),
        TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
        TextNode(" and a ", TextType.TEXT),
        TextNode("link", TextType.LINK, "https://boot.dev"),]
        self.assertListEqual(output_nodes,nodes)
    def test_plain_text_only(self):
        input_text = "Just some plain text with no formatting."
        expected_output = [TextNode("Just some plain text with no formatting.", TextType.TEXT)]
        self.assertListEqual(text_to_textnodes(input_text), expected_output)
    
    def test_multiple_styles(self):
        input_text = "**bold1** and **bold2** _italic1_ `code1`"
        expected_output = [
            TextNode("bold1", TextType.BOLD),
            TextNode(" and ", TextType.TEXT),
            TextNode("bold2", TextType.BOLD),
            TextNode(" ", TextType.TEXT),
            TextNode("italic1", TextType.ITALIC),
            TextNode(" ", TextType.TEXT),
            TextNode("code1", TextType.CODE),
        ]
        self.assertListEqual(text_to_textnodes(input_text), expected_output)
    def test_adjacent_formatting(self):
        input_text = "**bold**_italic_`code`"
        expected_output = [
            TextNode("bold", TextType.BOLD),
            TextNode("italic", TextType.ITALIC),
            TextNode("code", TextType.CODE),
        ]
        self.assertListEqual(text_to_textnodes(input_text), expected_output)

if __name__ == "__main__":
    unittest.main()