#!/usr/bin/env python3
"""Provides AVLTrees.

Necessary for creating AVL Tree
"""

import random

class TreeNode:  # Nodes
    def __init__(self, key):
        self.parent = None
        self.left = None
        self.right = None
        self.key = key

    def is_Leaf(self):
        if self.left is None and self.right is None:
            return True
        else:
            return False


class AVLTree:  # General tree
    def __init__(self, keys=None):
        self.root_node = None
        if keys is not None:
            if len(keys) >= 1:
                for key in keys:
                    self.insert(key)

    def add_as_child(self, parent_node, child_node):  # Used in insert()
        if child_node.key < parent_node.key:
            if parent_node.left is None:
                parent_node.left = child_node
                child_node.parent = parent_node
            else:
                self.add_as_child(parent_node.left, child_node)
        else:
            assert child_node.key >= parent_node.key
            if parent_node.right is None:
                parent_node.right = child_node
                child_node.parent = parent_node
            else:
                self.add_as_child(parent_node.right, child_node)

    def insert(self, key):
        new_node = TreeNode(key)
        if self.root_node is None:
            self.root_node = new_node
        else:
            self.add_as_child(self.root_node, new_node)

    def insert_from_list(self, arr):
        if arr is None or len(arr) < 1:
            return None
        piv = (len(arr)) // 2  # pivot
        left, right = [], []
        for key in arr[0:piv]:
            left.append(key)
        for key in arr[piv + 1:len(arr)]:
            right.append(key)
        self.insert(arr[piv])
        self.insert_from_list(left)  # there goes recursion (magic)
        self.insert_from_list(right)

    def find(self, key):  # find function and used in remove()
        return self.find_in_subtree(self.root_node, key)

    def find_in_subtree(self, node, key):  # used for find()
        if node is not None:
            if key < node.key:
                return self.find_in_subtree(node.left, key)
            elif key > node.key:
                return self.find_in_subtree(node.right, key)
            elif key == node.key:
                if node.right is not None:
                    if node.right.key == node.key:
                        node = self.find_in_subtree(node.right, key)
                    return node
                else:
                    if node.left is not None:
                        node = self.find_in_subtree(node.left)
                    return node
            else:  # key not found
                return None

    def find_path_to_key(self, node, key):  # prints path to given key except root
        if node is not None:
            if key < node.key:
                print(node.key)
                self.find_path_to_key(node.left, key)
            else:
                assert key >= node.key
                print(node.key)
                self.find_path_to_key(node.right, key)

    def remove(self, key):  # will remove first find except root
        node = self.find(key)
        if node is not None:
            if node.is_Leaf():
                self.remove_leaf(node)
            elif bool(node.left) and bool(node.right):
                self.remove_branch(node)
            else:
                self.swap_with_child_and_remove(node)

    def remove_leaf(self, node):  # when there is no successor
        if node.parent is not None:
            if node.parent.left == node:
                node.parent.left = None
            else:
                assert node.parent.right == node
                node.parent.right = None
        del node

    def remove_branch(self, node):  # when we have both successors
        if node.parent is not None:
            if node.parent.left == node:
                node.parent.left = node.right or node.left
            else:
                assert node.parent.right == node
                node.parent.right = node.right or node.left
            if node.left is not None:
                node.left.parent = node.parent
            else:
                assert node.right
                node.right.parent = node.parent
        del node

    def swap_with_child_and_remove(self, node):  # when the is only one successor
        if node is not None:
            if node.right is not None:
                    if node.parent is not None:
                        node.parent.right = node.right
                        node.right.parent = node.parent
            else:
                assert node.left
                assert node.parent
                node.parent.left = node.left
                node.left.parent = node.parent
            del node

    def selfDelete(self):  # general function and visualization of deleting
        self.post_remove(self.root_node)
        return None

    def post_remove(self, node):  # postorder remove
        if node is not None:
            #  Magic begins
            if node.left is not None:
                self.post_remove(node.left)
            if node.right is not None:
                self.post_remove(node.right)
            self.remove(node.key)
            self.visualize()
            print(" ")

    def preorder_view(self, printed_node):
        print(printed_node.key, end = " ")
        if printed_node.left is not None:
            self.preorder_view(printed_node.left)
        if printed_node.right is not None:
            self.preorder_view(printed_node.right)

    def inorder_view(self, printed_node):
        if printed_node.left is not None:
            self.inorder_view(printed_node.left)
        print(printed_node.key, end = " ")
        if printed_node.right is not None:
            self.inorder_view(printed_node.right)

    def postorder_view(self, printed_node):
        if printed_node.left is not None:
            self.postorder_view(printed_node.left)
        if printed_node.right is not None:
            self.postorder_view(printed_node.right)
        print(printed_node.key, end = " ")

    def visualize(self, order = None):  # main function for specific visualization
        if self.root_node is not None:
            if order == "preorder" or order is None:
                self.preorder_view(self.root_node)
            if order == "inorder":
                self.inorder_view(self.root_node)
            if order == "postorder":
                self.postorder_view(self.root_node)