import unittest
from markdown_block import markdown_to_block, block_to_block_type, BlockType, block_to_html_node

class TestMarkdownToBlock(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_block(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )


    def test_markdown_to_blocks_newlines(self):
        md = """
This is **bolded** paragraph




This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_block(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_block_to_block_types(self):
        block = "# heading"
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)
        block = "```\ncode\n```"
        self.assertEqual(block_to_block_type(block), BlockType.CODE)
        block = "> quote\n> more quote"
        self.assertEqual(block_to_block_type(block), BlockType.QUOTE)
        block = "- list\n- items"
        self.assertEqual(block_to_block_type(block), BlockType.UNORDERED_LIST)
        block = "1. list\n2. items"
        self.assertEqual(block_to_block_type(block), BlockType.ORDERED_LIST)
        block = "paragraph"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_block_to_html_node(self):
        block = "# heading"
        html_node = block_to_html_node(block, block_type=BlockType.HEADING)
        self.assertEqual(html_node.tag, "h1")
        self.assertEqual(html_node.value, None)
        self.assertEqual(len(html_node.children), 1)
        self.assertEqual(html_node.children[0].tag, "text")
        self.assertEqual(html_node.children[0].value, "heading")
        self.assertEqual(html_node.children[0].children, None)
        self.assertEqual(html_node.props, None)

        block = "```\ncode\n```"
        html_node = block_to_html_node(block, block_type=BlockType.CODE)
        self.assertEqual(html_node.tag, "pre")
        self.assertEqual(html_node.value, None)
        self.assertEqual(len(html_node.children), 1)
        self.assertEqual(html_node.children[0].tag, "code")
        self.assertEqual(html_node.children[0].value, "code")
        self.assertEqual(html_node.children[0].children, None)
        self.assertEqual(html_node.props, None)

        block = "> quote\n> more quote"
        html_node = block_to_html_node(block, block_type=BlockType.QUOTE)
        self.assertEqual(html_node.tag, "blockquote")
        self.assertEqual(html_node.value, None)
        self.assertEqual(len(html_node.children), 2)
        self.assertEqual(html_node.children[0].tag, "p")
        self.assertEqual(html_node.children[0].value, "quote")
        self.assertEqual(html_node.children[0].children, None)
        self.assertEqual(html_node.children[1].tag, "p")
        self.assertEqual(html_node.children[1].value, "more quote")
        self.assertEqual(html_node.children[1].children, None)
        self.assertEqual(html_node.props, None)

        block = "- list\n- items"
        html_node = block_to_html_node(block, block_type=BlockType.UNORDERED_LIST)
        self.assertEqual(html_node.tag, "ul")
        self.assertEqual(html_node.value, None)
        self.assertEqual(len(html_node.children), 2)
        self.assertEqual(html_node.children[0].tag, "li")
        self.assertEqual(html_node.children[0].value, "list")
        self.assertEqual(html_node.children[0].children, None)
        self.assertEqual(html_node.children[1].tag, "li")
        self.assertEqual(html_node.children[1].value, "items")
        self.assertEqual(html_node.children[1].children, None)
        self.assertEqual(html_node.props, None)

        block = "1. list\n2. items"
        html_node = block_to_html_node(block, block_type=BlockType.ORDERED_LIST)
        self.assertEqual(html_node.tag, "ol")
        self.assertEqual(html_node.value, None)
        self.assertEqual(len(html_node.children), 2)
        self.assertEqual(html_node.children[0].tag, "li")
        self.assertEqual(html_node.children[0].value, "list")
        self.assertEqual(html_node.children[0].children, None)
        self.assertEqual(html_node.children[1].tag, "li")
        self.assertEqual(html_node.children[1].value, "items")
        self.assertEqual(html_node.children[1].children, None)
        self.assertEqual(html_node.props, None)


if __name__ == "__main__":
    unittest.main()