from textnode import TextNode, TextType
import re

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        split_nodes = []
        sections = node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError("invalid markdown, formatted section not closed")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], TextType.TEXT))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes

def extract_markdown_images(text):
    matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches

def extract_markdown_links(text):
    matches = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches

def split_nodes_image(old_nodes):
    new_nodes =[]
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        matches = extract_markdown_images(node.text)
        if len(matches) == 0:
            new_nodes.append(node)
            continue
        remaining_text = node.text
        for alt_text, url in matches:
            image_markdown = f"![{alt_text}]({url})"
            parts = remaining_text.split(image_markdown, 1) # split only once
            if len(parts) != 2:
                raise ValueError("invalid markdown, image section not closed")
            if parts[0]: # if there is text before the image
                new_nodes.append(TextNode(parts[0], TextType.TEXT))
            #add the image node
            new_nodes.append(TextNode(alt_text, TextType.IMAGE, url))
            if len(parts) > 1: # if theres text after the imageS
                remaining_text = parts[1]
            else:
                remaining_text = ""
        if remaining_text:
            new_nodes.append(TextNode(remaining_text, TextType.TEXT))
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = [] 
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        matches = extract_markdown_links(node.text)
        if len(matches) == 0:
            new_nodes.append(node)
            continue
        remaining_text = node.text
        for link_text, url in matches:
            link_markdown = f"[{link_text}]({url})"
            parts = remaining_text.split(link_markdown, 1)
            if len(parts) != 2:
                raise ValueError("invalid markdown, link section not closed")
            if parts[0]: # if there is text before the link
                new_nodes.append(TextNode(parts[0], TextType.TEXT))
            #add the link node
            new_nodes.append(TextNode(link_text, TextType.LINK, url))
            if len(parts) > 1:
                remaining_text = parts[1]
            else:
                remaining_text = ""
        if remaining_text:
            new_nodes.append(TextNode(remaining_text, TextType.TEXT))
    return new_nodes