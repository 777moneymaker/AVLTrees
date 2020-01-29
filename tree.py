#!/usr/bin/env python3
"""Provides AVLTrees.

Necessary for creating AVL Tree
"""


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
        if keys is not None and len (keys) >= 1:
            for key in keys:
                self.insert(key)

    def add_as_child(self, parent, child):  # Used in insert()
        if child.key < parent.key:
            if parent.left is None:
                parent.left = child
                child.parent = parent
            else:
                self.add_as_child(parent.left, child)
        else:
            assert child.key >= parent.key
            if parent.right is None:
                parent.right = child
                child.parent = parent
            else:
                self.add_as_child(parent.right, child)

    def insert(self, key):
        root = self.root_node
        new_node = TreeNode(key)
        if root is None:
            self.root_node = new_node
        else:
            self.add_as_child(root, new_node)

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
                        right_node = self.find_in_subtree(node.right, key)
                        return right_node
                else:
                    if node.left is not None:
                        node = self.find_in_subtree(node.left)
                    return node
            else:  # key not found
                return None

    def path_to_key(self, key):  # prints path to key
        self.find_path_to_key(self.root_node, key)

    def find_path_to_key(self, node, key):
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
        parent = node.parent
        if parent is not None:
            if parent.left == node:
                parent.left = None
            else:
                assert parent.right == node
                parent.right = None
        del node

    def remove_branch(self, node):  # when we have both successors
        parent = node.parent
        if parent is not None:
            if parent.left == node:
                parent.left = node.right or node.left
            else:
                assert parent.right == node
                parent.right = node.right or node.left
            if node.left is not None:
                node.left.parent = parent
            else:
                assert node.right
                node.right.parent = parent
        del node

    def swap_with_child_and_remove(self, node):  # when the is only one successor
        parent = node.parent
        if node is not None:
            if node.right is not None:
                assert parent
                parent.right = node.right
                node.right.parent = parent
            elif node.left is not None:
                assert parent
                parent.left = node.left
                node.left.parent = parent
            else:
                return None
            del node

    def selfDelete(self):  # general function and visualization of deleting
        self.post_remove(self.root_node)
        return None

    def post_remove(self, node):  # postorder remove
        root = self.root_node
        if root.right is None and root.left is None:
            return None
        if node is not None:
            #  Magic begins
            if node.left is not None:
                self.post_remove(node.left)
            if node.right is not None:
                self.post_remove(node.right)
            self.remove(node.key)
            self.visualize()
            print(" ")

    def preorder_view(self, node):
        print(node.key, end = " ")
        if node.left is not None:
            self.preorder_view(node.left)
        if node.right is not None:
            self.preorder_view(node.right)

    def inorder_view(self, node):
        if node.left is not None:
            self.inorder_view(node.left)
        print(node.key, end = " ")
        if node.right is not None:
            self.inorder_view(node.right)

    def postorder_view(self, node):
        if node.left is not None:
            self.postorder_view(node.left)
        if node.right is not None:
            self.postorder_view(node.right)
        print(node.key, end = " ")

    def visualize(self, order = None):  # main function for specific visualization
        if self.root_node is not None:
            if order == "preorder" or order is None:
                self.preorder_view(self.root_node)
            if order == "inorder":
                self.inorder_view(self.root_node)
            if order == "postorder":
                self.postorder_view(self.root_node)