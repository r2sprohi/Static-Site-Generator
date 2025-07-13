import unittest
from textnode import TextNode, TextType
from split_images_links import split_nodes_image, split_nodes_link


class SplitImageLinkMarkdown(unittest.TestCase):
    def test_delim_link(self):
        node = TextNode(
        "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
        TextType.TEXT,)
        new_nodes = split_nodes_link([node])
        actual_nodes = [
        TextNode("This is text with a link ", TextType.TEXT),
        TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
        TextNode(" and ", TextType.TEXT),
        TextNode( "to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"),]
        self.assertListEqual(actual_nodes,new_nodes)
    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )
    def test_split_images_2(self):
        node1 = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        node2 = TextNode("This is just normal",
            TextType.TEXT,)
        new_nodes = split_nodes_image([node1,node2])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
                TextNode("This is just normal", TextType.TEXT)
            ],
            new_nodes,
        )
    def test_split_links_2(self):
        node1 = TextNode(
        "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
        TextType.TEXT,)
        node2 = TextNode("This is just normal",
            TextType.TEXT,)
        new_nodes = split_nodes_link([node1,node2])
        self.assertListEqual(
            [
                TextNode("This is text with a link ", TextType.TEXT),
                TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
                TextNode(" and ", TextType.TEXT),
                TextNode( "to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"),
                TextNode("This is just normal", TextType.TEXT)
            ],
            new_nodes,
        )
    def test_split_images_3(self):
        node1 = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        node2 = TextNode("This is another text with an ![image2](https://i.imgur.com/zjjcJKZ.jpg) and another ![second image](https://i.imgur.com/3elNhQu.jpeg)", TextType.TEXT)

        new_nodes = split_nodes_image([node1,node2])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
                TextNode("This is another text with an ", TextType.TEXT),
                TextNode("image2", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.jpg"),
                TextNode(" and another ", TextType.TEXT),
                TextNode("second image",TextType.IMAGE, "https://i.imgur.com/3elNhQu.jpeg")
            ],
            new_nodes,
        )

if __name__ == "__main__":
    unittest.main()

