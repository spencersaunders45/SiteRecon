from unittest.mock import Mock
import pytest
import sys

sys.path.append('c:\\Users\\Spencer\\spenc\\SiteRecon')

from src.Node import Node

class TestNode:

    root = Node(0)
    count = 1

    def create_Node(self):
        for i in range(1,5):
            node = Node(i)
            self.root.add_child(node)
        children = self.root.get_children()
        count = 5
        for child in children:
            for i in range(3):
                node = Node(count)
                child.add_child(node)
                count += 1

    def breadth_first_search(self, node):
        # Exit Case
        if len(node.get_children()) == 0:
            return

        # Assert Check
        for child in node.get_children():
            assert self.count == child.url
            self.count += 1

        # Breadth First Search
        for child in node.get_children():
            self.breadth_first_search(child)

    def test_breadth_first_search(self):
        self.create_Node()
        self.breadth_first_search(self.root)