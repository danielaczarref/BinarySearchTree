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
    
    def remove(self, value):
        if self.root is None:
            return False

        elif self.root.data == value:
            if self.root.left is None and self.root.right is None:
                self.root = None
            elif self.root.left and self.root.right is None:
                self.root = self.root.left
            elif self.root.left is None and self.root.right:
                self.root = self.root.right
            elif self.root.left and self.root.right:
                delParent = self.root
                delNode = self.root.right
                while delNode.left:
                    delParent = delNode
                    delNode = delNode.left

                self.root.data = delNode.data
                if delNode.right:
                    if delParent.data > delNode.data:
                        delParent.left = delNode.right
                    elif delParent.data < delNode.data:
                        delParent.right = delNode.right

                else:
                    if delNode.data < delParent.data:
                        delParent.left = None
                    else:
                        delParent.right = None

            return True

        parent = None
        newNode = self.root

        while newNode and newNode.data != value:
            parent = newNode
            if value  < newNode.data:
                newNode = newNode.left
            elif value > newNode.data:
                newNode = newNode.right

        if newNode is None or newNode.data != value:
            return False
        elif newNode.left is None and newNode.right is None:
            if value < parent.data:
                parent.left = None
            else:
                parent.right = None 
            return True
        elif newNode.left is None and newNode.right:
            if value < parent.data:
                parent.left = newNode.right
            else:
                parent.right = newNode.right
            return True
        else:
            delParent = newNode
            delNode = newNode.right
            while delNode.left:
                delParent = delNode
                delNode = delNode.left
            newNode.data = delNode.data
            if delNode.right:
                if delParent.data > delNode.data:
                    delParent.left = delNode.right
                elif delParent.data < delNode.data:
                    delParent.right = delNode.right
            else:
                if delNode.data < delParent.data:
                    delParent.left = None
                else:
                    delParent.right = None