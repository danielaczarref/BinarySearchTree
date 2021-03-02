# Binary Search Tree

Binary Search Trees is a node-based binary tree data structure which has the following properties:

    The left subtree of a node contains only nodes with keys lesser than the node’s key.
    The right subtree of a node contains only nodes with keys greater than the node’s key.
    The left and right subtree each must also be a binary search tree.


## Basic info 

This code includings the following functions:

- getRoot: return the value on tree's root;
- add: insert value on binary tree;
- search: search on tree's nodes if value was inserted, otherwise it prints 404 not found;
- preOrder: print the tree elements in pre order (the order in which they were added);
- remove: it will remove the value on tree if it was inserted before. it will do so by search the value on tree's root and, if not found on tree's root, it will search on left and right sides of the tree.

## Running

It's possible to test this code with the following commands, for example:

```
a = Tree()
a.add(52)
a.add(18)
a.add(7)
a.add(25)
a.add(19)
a.add(60)
a.add(72)
a.add(98)
a.add(63)
a.preOrder()
print ('---------------------')
a.remove(19)
a.preOrder()
print ('-----------------')
a.search(63)
a.search(19)
```

You can change the values on the example above in order to test it with values of your own preference.
