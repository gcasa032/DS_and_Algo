class Node:
    ''' A binary search tree node'''
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val

class BinarySearchTree:
    '''Implements many Binary Search Tree functions'''

    def __init__(self, head: Node = None):
        self.head = head

    def insert(self, data: Node):
        '''Inserts a node into a binary search tree'''
        if self.head:
            if self.head.val > data.val:
                if self.head.left is None:
                    self.head.left = data
                else:
                    self.head.left.insert(data)
            elif self.head.val < data.val:
                if self.head.right is None:
                    self.head.right = data
                else:
                    self.head.right.insert(data)          
        else:
            self.head = data

            
tree = BinarySearchTree()
tree.insert(Node(3))
tree.insert(Node(2))

print(tree.head.val)
print(tree.head.left.val)