import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode("div", "This is a text node", [], {"class": "test"})
        self.assertEqual(node.props_to_html(), 'class="test"')

    def test_props_to_html_no_props(self):
        node = HTMLNode("div", "This is a text node", [])
        self.assertEqual(node.props_to_html(), "")

    def test_props_to_html_multiple_props(self):
        node = HTMLNode("div", "This is a text node", [], {"class": "test", "id": "test"})
        self.assertEqual(node.props_to_html(), 'class="test" id="test"')

    def test_leaf_node_no_tag(self):
        node = LeafNode(None, "This is a text node")
        self.assertEqual(node.to_html(), "This is a text node")
    
    def test_leaf_node_no_value(self):
        node = LeafNode("div", None)
        with self.assertRaises(ValueError):
            node.to_html()

    def test_leaf_node(self):
        node = LeafNode("div", "This is a text node")
        self.assertEqual(node.to_html(), "<div >This is a text node</div>")

    def test_parent_node_no_tag(self):
        node = ParentNode(None, [LeafNode("div", "This is a text node")])
        with self.assertRaises(ValueError):
            node.to_html()
    
    def test_parent_node_no_children(self):
        node = ParentNode("div", None)
        with self.assertRaises(ValueError):
            node.to_html()

    def test_parent_node(self):
        node = ParentNode("div", [LeafNode("div", "This is a text node")])
        self.assertEqual(node.to_html(), "<div ><div >This is a text node</div></div>") 

    def test_parent_node_multiple_children(self):
        node = ParentNode("div", [LeafNode("div", "This is a text node"), LeafNode("div", "This is a text node")])
        self.assertEqual(node.to_html(), "<div ><div >This is a text node</div><div >This is a text node</div></div>")

    def test_parent_node_props(self):
        node = ParentNode("div", [LeafNode("div", "This is a text node")], {"class": "test"})
        self.assertEqual(node.to_html(), '<div class="test"><div >This is a text node</div></div>')

    def test_parent_node_nested(self):
        node = ParentNode("div", [ParentNode("div", [LeafNode("div", "This is a text node")])])
        self.assertEqual(node.to_html(), "<div ><div ><div >This is a text node</div></div></div>")

    def test_text_node_to_html_node(self):
        node = LeafNode("div", "This is a text node")
        self.assertEqual(node.to_html(), "<div >This is a text node</div>")

    def test_text_node_to_html_node_no_tag(self):
        node = LeafNode(None, "This is a text node")
        self.assertEqual(node.to_html(), "This is a text node")



if __name__ == "__main__":
    unittest.main()