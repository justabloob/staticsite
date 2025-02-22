from enum import Enum

class Texttype(Enum):
    NORMAL_TEXT = text
    BOLD_TEXT = **{text}**
    ITALIC_TEXT = *{text}*
    CODE_TEXT = `{text}`
    LINKS = [text](url)
    IMAGES = ![text](url)

class TextNode(Texttype):
    def __init__(self, text, url=None):
        self.text_type = Texttype
        self.text = text
        self.url = url