from bss import Node, BinarySearchTree
import random

tree = BinarySearchTree()

for x in range(100):
    val = random.randint(0, 999999)
    print(val)
    tree.insert(val)