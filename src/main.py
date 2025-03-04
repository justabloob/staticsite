from textnode import *

def main():
    node = TextNode("This is a test", TextType.BOLD, "https://www.google.com")
    print(node)

if __name__ == "__main__":
    main()