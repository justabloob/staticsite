from enum import Enum
import re
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
        return HTMLNode(tag="p", value=None, children=text_to_children(block))
    elif block_type == BlockType.HEADING:
        level = block.count("#") # Count the number of '#' characters to determine the heading level
        tag = f"h{level}" # Set the tag to h1, h2, etc. based on the level
        text = block[level:].strip() # Get the text after the '#' characters
        return HTMLNode(tag=tag, value=None, children=text_to_children(text))
    elif block_type == BlockType.CODE:
        text = block.strip("```").strip() # Remove the backticks and strip whitespace
        code_node = HTMLNode(tag="code", value=text, children=None)
        return HTMLNode(tag="pre", value=None, children=[code_node])
    elif block_type == BlockType.QUOTE:
        lines = block.split("\n")
        child = []
        for line in lines:
            stripped_line = line.lstrip('> ').strip() # Remove the '>' character and strip whitespace
            if stripped_line:
                child.append(HTMLNode(tag="p", value=stripped_line, children=None))
        return HTMLNode(tag="blockquote", value=None, children=child)
    elif block_type == BlockType.UNORDERED_LIST:
        lines = block.split("\n")
        child = []
        for line in lines:
            stripped_line = line.lstrip('- ').strip() # Remove the '-' character and strip whitespace
            if stripped_line:
                child.append(HTMLNode(tag="li", value=stripped_line, children=None))
        return HTMLNode(tag="ul", value=None, children=child)
    elif block_type == BlockType.ORDERED_LIST:
        pattern = r"^\d+\.\s" # Regex pattern to match "<number>. " at the start of the line
        lines = block.split("\n")
        child = []
        for line in lines:
            # Check if the line starts with a number and a dot
            if re.match(pattern, line.strip()):
                # Remove the number and dot to isolate the content
                stripped_line = re.sub(pattern, "", line.strip())
                child.append(HTMLNode(tag="li", value=stripped_line, children=None))
        return HTMLNode(tag="ol", value=None, children=child)
    else:
        raise ValueError(f"Invalid block type: {block_type}")