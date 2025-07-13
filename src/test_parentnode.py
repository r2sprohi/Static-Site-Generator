import unittest
from htmlnode import ParentNode
from htmlnode import LeafNode
class ParentTextTest(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )
    def test_to_html_with_multiple_children(self):
        child1 = LeafNode("b", "bold")
        child2 = LeafNode("i", "italic")
        parent = ParentNode("p", [child1, child2])
        self.assertEqual(parent.to_html(), "<p><b>bold</b><i>italic</i></p>")
        
    def test_to_html_deep_nesting(self):
        level3 = LeafNode("u", "deep")
        level2 = ParentNode("span", [level3])
        level1 = ParentNode("div", [level2])
        root = ParentNode("section", [level1])
        self.assertEqual(
            root.to_html(),
            "<section><div><span><u>deep</u></span></div></section>"
        )
    def test_to_html_with_props(self):
        child = LeafNode(None,"click here")
        parent = ParentNode("a",[child],{"href": "https://example.com", "target": "_blank"})
        self.assertEqual(
            parent.to_html(),
            '<a href="https://example.com" target="_blank">click here</a>'
        )

if __name__ == "__main__":
    unittest.main()