#!/usr/bin/env python
"""AVL Trees and their simple functions.
Implementation made for Algorithm's laboratories."""



from tree import AVLTree # tree.py module

import random

myTree = AVLTree()
myList = []

for i in range(15):
    r = random.randint(10, 100)
    myList.append(r)

for key in myList:
    myTree.insert(key)

myTree.visualize()

