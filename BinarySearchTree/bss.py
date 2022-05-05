import random


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
        if key is not None:
            self.root = Node(key)
        else:
            self.root = None

    def insert(self, key):
        ''' Insert key into tree '''
        if self.root is None:
            self.root = Node(key)
        else:
            self.root.insert(key)

    def find(self, key):
        '''Returns true if value is found in key, false if not'''
        temp = self.root

        while temp:
            if temp.val < key:
                temp = temp.right
            elif temp.val > key:
                temp = temp.left
            else:
                return True

        return False

    def delete(self, root: Node, key):
        ''' Deletes node = key. Returns true if deletion was successful and false if not'''    
        if root is None:
            return root
        elif key < root.val:
            root.left = self.delete(root.left, key)
        elif key > root.val:
            root.right = self.delete(root.right, key)
        else:                     
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp

            #if it has two children??


tree = BinarySearchTree()

for x in range(100):
    val = random.randint(48, 999999)
    tree.insert(val)

tree.insert(47)

print(tree.find(47))
tree.delete(tree.root, 47)
print(tree.find(47))