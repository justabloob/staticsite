from enum import Enum
from htmlnode import HTMLNode, LeafNode, ParentNode
from textnode import TextNode, text_node_to_html_node
from markdown_inline import text_to_textnodes

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def markdown_to_block(markdown):
    blocks = markdown.split("\n\n")
    filtered_blocks = []
    for block in blocks:
        if block == "":
            continue
        block = block.strip()
        filtered_blocks.append(block)
    return filtered_blocks

def block_to_block_type(block):
    lines = block.split('\n')
    # Check if the block is empty
    if not block.strip():
        return BlockType.PARAGRAPH
    # Check if the block is a heading
    if block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return BlockType.HEADING
    # Check if the block is a code block
    if block.startswith('```') and block.endswith('```'):
        return BlockType.CODE
    # Check if the block is a quote
    if block.startswith('>'):
        for line in lines:
            if not line.startswith('>'):
                return BlockType.PARAGRAPH
        return BlockType.QUOTE
    # Check if the block is an unordered list
    if block.startswith('- '):
        for line in lines:
            if not line.startswith('- '):
                return BlockType.PARAGRAPH
        return BlockType.UNORDERED_LIST
    # Check if the block is an ordered list
    if block.startswith("1. "):
        i = 1
        for line in lines:
            if not line.startswith(f"{i}. "):
                return BlockType.PARAGRAPH
            i += 1
        return BlockType.ORDERED_LIST
    # If none of the above, return paragraph type
    return BlockType.PARAGRAPH

def markdown_to_html_node(markdown):
    blocks = markdown_to_block(markdown) # split markdown into blocks
    for block in blocks:
        block_type = block_to_block_type(block)
        pass

def text_to_children(text):
    # Convert the text to a list of TextNode objects
    text_nodes = text_to_textnodes(text)
    # Convert the TextNode objects to LeafNode objects
    children_nodes = []
    for text_node in text_nodes:
        children_node = text_node_to_html_node(text_node)
        children_nodes.append(children_node)
    return children_nodes

    
def block_to_html_node(block, block_type):
    # Convert the block to an HTML node based on its type
    if block_type == BlockType.PARAGRAPH:
        return HTMLNode(tag="<p>", value=block)
    elif block_type == BlockType.HEADING:
        level = block.count("#")
        tag = f"<h{level}>"
        value = block[level:].strip()
        return HTMLNode(tag=tag, value=value)
    elif block_type == BlockType.CODE:
        pass