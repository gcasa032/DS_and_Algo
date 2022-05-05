class Node:
    ''' A binary search tree node'''
    def __init__(self, val= None):
        self.left = None
        self.right = None
        self.val = val

    def insert(self, val):
        '''Inserts a node into a binary search tree'''
        if self.val:
            if self.val > val:
                if self.left is None:
                    self.left = Node(val)
                else:
                    self.left.insert(val)
            elif self.val < val:
                if self.right is None:
                    self.right = Node(val)
                else:
                    self.right.insert(val)         
        else:
            self.val = val

class BinarySearchTree:
    '''Implements many Binary Search Tree functions'''

    def __init__(self, key = None):
        self.root = Node(key)

    def insert(self, key):
        self.root.insert(key)