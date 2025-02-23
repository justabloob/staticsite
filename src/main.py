from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode, ParentNode

def main():
    node = TextNode("This is a textnode", TextType.ITALIC, "https://www.google.com")
    print(node)



if __name__ == "__main__":
    main()