import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode("p", "This is a paragraph", None, {"class": "paragraph"})
        self.assertEqual(node.props_to_html(), ' class="paragraph"')

    def test_props_to_html_none(self):
        node = HTMLNode("p", "This is a paragraph", None, None)
        self.assertEqual(node.props_to_html(), '')

    def test_multiple_props_to_html(self):
        node = HTMLNode("p", "This is a paragraph", None, {"class": "paragraph", "id": "paragraph1"})
        self.assertEqual(node.props_to_html(), ' class="paragraph" id="paragraph1"')

    def test_props_to_html_special_chars(self):
        node = HTMLNode("p", "This is a paragraph", None, {"class": "paragraph", "id": "paragraph1", "data-test": "test"})
        self.assertEqual(node.props_to_html(), ' class="paragraph" id="paragraph1" data-test="test"')


if __name__ == "__main__":
    unittest.main()