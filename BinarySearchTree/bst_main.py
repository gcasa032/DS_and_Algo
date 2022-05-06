from bst import Node, BinarySearchTree
import random

tree = BinarySearchTree()

# for x in range(100):
#     val = random.randint(0, 999999)
#     tree.insert(val)

tree.insert(10)
tree.insert(7)
tree.insert(12)
tree.insert(11)
tree.insert(14)
tree.insert(13)
tree.insert(16)

print(tree.inorder_traversal())