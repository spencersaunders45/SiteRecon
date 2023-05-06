class Node:
    """Creates a node that will be added into the Node
    
    Attributes:
    url : str
        A page URL
    children : list
        A list of Node objects
    """

    def __init__(self, url: str):
        self.url = url
        self.children = []

    def add_child(self, node):
        """ Adds a Node object to the list of children
        
        Parameters:
        node : Node
            An object of Node

        Returns:
            None
        """
        self.children.append(node)

    def get_children(self) -> list:
        """Gets the list of child nodes

        Returns:
        list
            A list of Node objects
        
        """
        return self.children