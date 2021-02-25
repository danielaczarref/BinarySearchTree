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

    def search(self, value):
        if (self.root != None):
            return self._search(value, self.root)
        else:
            return None
    
    def _search(self, value, node):
        if (value === node.data):
            return node  
        elif (value < node.data and node.left != None):
            self._search(value, node.left)
            print(value, True)
        elif (value > node.data and node.right != None):
            self._search(value, node.right)
            print(value, True)

    def preOrder(self):
        if (self.root != None):
            self._preOrder(self.root)

    def _preOrder(self, node):
        if (node != None):
            print(node.data)
            self._preOrder(node.left)
            self._preOrder(node.right)
    
    # def remove(self, value):
    #     if self.root is None:
    #         return False