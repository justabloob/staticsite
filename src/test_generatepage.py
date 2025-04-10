import unittest
from generate_page import extract_title

class TestExtractTitle(unittest.TestCase):
    def test_extract_title(self):
        md = """
# This is a title
This is a paragraph with **bold** text and _italic_ text.
"""
        title = extract_title(md)
        self.assertEqual(title, "This is a title")
    
    def test_extract_title_no_title(self):
        md = """
This is a paragraph with **bold** text and _italic_ text.
"""
        title = extract_title(md)
        self.assertEqual(title, "")