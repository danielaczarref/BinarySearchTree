class Node:
    def __init__ (self, data):
        self.left = None
        self.right = None
        self.data = data

class Tree:
    def __init__(self):
        self.root = None

    def getRoot(self):
        return self.root

    def add(self, value):
        if (self.root == None):
            self.root == Node(value)
        else:
            self._add(value, self.root)
    
    def _add(self, value, node):
        if (value < node.data):
            if (node.left != None):
                self._add(value, node.left)
            else:
                node.left = Node(value)
        else:
            if (node.right != None):
                self._add(value, node.right)
            else:
                node.right = Node(value) 