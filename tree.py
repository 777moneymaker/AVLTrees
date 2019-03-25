#!/usr/bin/env python

class TreeNode:
    def __init__(self, key):
        self.parent = None
        self.left = None
        self.right = None
        self.key = key


class AVLTree:
    def __init__(self):
        self.root_node = None

    def add_as_child (self, parent_node, child_node):
        if child_node.key < parent_node.key:
            if parent_node.left is None:
                parent_node.left = child_node
                child_node.parent = parent_node
            else:
                self.add_as_child(parent_node.left, child_node)
        else:
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


    def visualize(self, order = None):
        if order is None or order == "preorder":
            self.preorder_view(self.root_node)
        if order == "inorder":
            self.inorder_view(self.root_node)
        if order == "postorder":
            self.postorder_view(self.root_node)
