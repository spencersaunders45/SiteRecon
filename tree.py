class URLTree:
    class Node:
        url = None
        children = []
        parent = None

        def __init__(self, url):
            self.url = url

    root = None
    known_urls = set()

    def __init__(self, url):
        self.root = self.create_root(url)

    def create_root(self, url):
        root = self.Node(url)
        return root

    def url_in_tree(self, url):
        if url in self.known_urls:
            return True
        else:
            self.known_urls.add(url)
            return False