class Tree:
    def __init__(self, url):
        self.url = url
        self.children = []

    def add_child(self, node):
        self.children.append(node)

    def get_children(self):
        return self.children