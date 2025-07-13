import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def same_tag_type(self):
        node1 = HTMLNode("p","i am paragraph tag", ["a","p","h1"],{"href": "https://www.google.com"})
        node2 = HTMLNode("p","i am paragraph tag", ["a","p","h1"],{"href": "https://www.google.com"})
        self.assertEqual(node1.tag, node2.tag)
    def test_children(self):
        node1 = HTMLNode("p","i am paragraph tag",["a","p","h1"],{"href": "https://www.google.com"})
        self.assertTrue(node1.children is not None)
    def test_value(self):
        node1 = HTMLNode("p","i am paragraph tag",None,{"href": "https://www.google.com"})
        self.assertTrue(node1.value is not None)
    def test_propstohtml_method(self):
        node1 = HTMLNode("p","i am paragraph tag",None,{"href": "https://www.google.com","target": "_blank"})
        output_str = ' href="https://www.google.com" target="_blank"'
        props_to_html_output = node1.props_to_html()
        self.assertEqual(props_to_html_output,output_str)
if __name__ == "__main__":
    unittest.main()