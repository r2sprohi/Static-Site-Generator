import unittest

from markdown_extract import extract_markdown_images, extract_markdown_url

class ExtractMarkdown(unittest.TestCase):
    def some_markdown_url(self):
        link = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        result = extract_markdown_url(link)
        self.assertListEqual(
            [("to boot dev","https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")],result
        )
    def some_markdown_img(self):
        img = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        result = extract_markdown_images(img)
        self.assertListEqual(
            [("rick roll","https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")],result
        )

    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
        "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)")
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)
    def test_extract_markdown_url(self):
        matches = extract_markdown_url(
            "This is text with a [url](https://google.com)"
        )
        self.assertListEqual([("url", "https://google.com")],matches)
if __name__ == "__main__":
    unittest.main()