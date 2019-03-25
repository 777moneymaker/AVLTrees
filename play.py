#!/usr/bin/env python
'''AVL Trees and their simple functions.

Implementation made for Algorithm's laboratories.'''

from tree import AVLTree # tree.py module
import random

__author__ = "Miłosz Chodkowski"
__license__ = "MIT License "
__version__ = "1.0"
__maintainer__ = "Miłosz Chodkowski"
__email__ = "milosz.chodkowski@student.put.poznan.pl"
__status__ = "Production"

if __name__ == "__main__":
    myList = []
    for i in range(50):
        r = random.randint(10, 100)
        myList.append(r)
    myTree = AVLTree(myList)

    myTree.visualize()
    print("")
    myTree.visualize("inorder")
    print("")
    myTree.visualize("postorder")





