from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.NORMAL: # if the node is not a normal text node
            new_nodes.append(node)
            continue # skip the rest of the loop
        split_nodes = []
        parts = node.text.split(delimiter)
        if len(parts) % 2 == 0: # if the delimiter is not used correctly
            raise Exception("Invalid Markdown syntax")
        for i in range(len(parts)): # for each part of the text
            if parts[i] == "": # if the part is empty
                continue
            if i % 2 == 0: # if the part is not bolded
                split_nodes.append(TextNode(parts[i], TextType.NORMAL))
            else:
                split_nodes.append(TextNode(parts[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes