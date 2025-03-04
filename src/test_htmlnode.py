import unittest
from htmlnode import HTMLNode, LeafNode

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

    def test_values(self):
        node = HTMLNode( "div", "I wish I could read", None, None)
        self.assertEqual(node.tag, "div")
        self.assertEqual(node.value,"I wish I could read")
        self.assertEqual(node.children, None)
        self.assertEqual(node.props, None)

    def test_repr(self):
        node = HTMLNode("p", "What a strange world", None, {"class": "primary"})
        self.assertEqual(node.__repr__(), "HTMLNode(p, What a strange world, None, {'class': 'primary'})")

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_h1(self):
        node = LeafNode("h1", "Hello, world!")
        self.assertEqual(node.to_html(), "<h1>Hello, world!</h1>")

    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")



if __name__ == "__main__":
    unittest.main()