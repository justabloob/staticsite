class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.children = children 
        self.value = value
        self.props = props
    
    def to_html(self):
        raise NotImplementedError()
    
    def props_to_html(self): # returns a string representation of the props
        if self.props:
            return " ".join(f'{key}="{value}"' for key, value in self.props.items())
        return ""
    
    def __repr__(self): # returns a string representation of the object
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)
    
    def to_html(self): 
        if self.value is None:
            raise ValueError("LeafNode must have a value")
        if self.tag is None:
            return self.value
        return f"<{self.tag} {self.props_to_html()}>{self.value}</{self.tag}>"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)
    
    def to_html(self):
        if self.tag is None:
            raise ValueError("ParentNode must have a tag")
        if self.children is None:
            raise ValueError("ParentNode must have children")
        children = "".join(child.to_html() for child in self.children)
        return f"<{self.tag} {self.props_to_html()}>{children}</{self.tag}>"