#!/usr/bin/env python3
"""AVL Trees and their simple functions.

Author: Miłosz Chodkowski
Date Created: 25.03.2019
Python Version: 3.7.2
"""

# Begin code

import random
from tree import AVLTree  # tree.py module

if __name__ == "__main__":

    myTree2 = AVLTree()
    myList2 = [random.randint(10,80) for i in range(10)]
    myList2.sort()
    print(*myList2, "\n")
    myTree2.insert_from_list(myList2)
    myTree2.visualize()
    print("\n")
    myTree2.selfDelete()


