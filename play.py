#!/usr/bin/env python3
"""AVL Trees and their simple functions."""

__author__ = 'Milosz Chodkowski'

import random
from tree import AVLTree  # tree.py module


if __name__ == "__main__":
    tree = AVLTree()
    numbers = list({random.randint(10, 90) for i in range(15)})
    print(sorted(numbers))
    for num in sorted(numbers):
        tree.insert(num)
    
    # Quicksort-like insertion
    # tree.insert_from_list(sorted(numbers))
    
    # Enter type of view: postorder, inorder, preorder
    tree.visualize('postorder')
