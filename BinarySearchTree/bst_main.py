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



print(tree.find(12))
print(tree.delete(tree.root,12))
print(tree.find(12))


# tree = BinarySearchTree()

# for x in range(100):
#     val = random.randint(48, 999999)
#     tree.insert(val)

# tree.insert(47)

# print(tree.find(47))
# tree.delete(tree.root, 47)
# print(tree.find(47))