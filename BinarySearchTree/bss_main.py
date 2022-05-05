from bss import Node, BinarySearchTree
import random

tree = BinarySearchTree()

for x in range(100):
    val = random.randint(0, 999999)
    tree.insert(val)

tree.insert(47)

print(tree.find(47))
print(tree.delete(47))
print(tree.find(47))