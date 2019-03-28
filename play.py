#!/usr/bin/env python3
"""AVL Trees and their simple functions.

Author: Miłosz Chodkowski
Date Created: 25.03.2019
Python Version: 3.7.2
"""

# Begin code

import random
from tree import AVLTree  # tree.py module

def commands():
    print("1 - add element \n"
          "2 - delete element \n"
          "3 - search for element \n"
          "4 - tree visualization\n"
          "5 - insert from sorted list \n"
          "6 - postorder tree delete\n"
          "7 - exit")

if __name__ == "__main__":

    commands()

    tree = AVLTree()
    numbers = [random.randint(10, 90) for i in range(15)]
    numbers.sort()

    while True:
        choice = input("Enter your choice: ")
        if choice == "1":
            numchoice = int(input("Enter number to insert: "))
            tree.insert(numchoice)
        elif choice == "2":
            numchoice = int(input("Enter number to delete: "))
            tree.remove(numchoice)
        elif choice == "3":
            numchoice = int(input("Enter number to find path to: "))
        elif choice == "4":
            viewchoice = input("Enter type of view (postorder, inorder, preorder): ")
            tree.visualize(viewchoice)
            print("\n")
        elif choice == "5":
            print("List of random ints: ", *numbers)
            ynchoice = input("Do you wanna insert it? (y/n): ")
            if ynchoice == "y":
                tree.insert_from_list(numbers)
            else:
                continue
        elif choice == "6":
            tree.selfDelete()
        elif choice == "7":  # bye!
            exit(0)
        else:
            print("Wrong!")


