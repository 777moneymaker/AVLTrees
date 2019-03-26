#!/usr/bin/env python3
"""AVL Trees and their simple functions.
Author: Miłosz Chodkowski
Date Created: 25.03.2019
Python Version: 3.7.2"""

# Begin code

from tree import AVLTree  # tree.py module
import random

if __name__ == "__main__":
    myList = []
    for i in range(50):
        r = random.randint(10, 100)
        myList.append(r)
    myTree = AVLTree(myList)

    myTree.visualize()
