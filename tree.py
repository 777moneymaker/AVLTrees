#!/usr/bin/env python
'''Provides AVLTrees. Necessary for creating AVL Tree '''


class TreeNode:
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


class AVLTree:
    def __init__(self, keys=None):
        self.root_node = None
        if keys is not None:
            if len(keys) >= 1:
                for key in keys:
                    self.insert(key)

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

    def find(self, key):
        return self.find_in_subtree(self.root_node, key)

    def find_in_subtree(self, node, key):
        if node is None:
            return None  # key not found
        if key < node.key:
            return self.find_in_subtree(node.left, key)
        elif key > node.key:
            return self.find_in_subtree(node.right, key)
        else:  # key equal to node.key
            return node

    def remove(self, key):  # will remove first find
        node = self.find(key)
        if node is not None:
            if node.is_Leaf():
                self.remove_leaf(node)
            elif (bool(node.left)) and (bool(node.right)):
                self.remove_branch(node)
            else:
                assert (node.left) and (node.right)
                self.swap_with_child_and_remove(node)

    def remove_leaf(self, node):
        if node.parent is not None:
            if node.parent.left == node:
                node.parent.left = None
            else:
                assert node.parent.right == node
                node.parent.right = None
        del node

    def remove_branch(self, node):
        if node.parent is not None:
            if node.parent.left == node:
                node.parent.left = node.right or node.left
            else:
                assert (node.parent.right == node)
                node.parent.right = node.right or node.left
            if node.left:
                node.left.parent = node.parent
            else:
                assert node.right
                node.right.parent = node.parent
        del node

    def swap_with_child_and_remove(self, node):
        if node is not None:
            if node.right is not None:
                if node.parent.right == node:
                    node.parent.right = node.right
                    del node
                else:
                    assert node.parent.left == node
                    node.parent.left = node.left
                    del node
            else:
                assert node.left
                node.parent = node.left

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
        if self.root_node is not None:
            if order == "preorder" or order is None:
                self.preorder_view(self.root_node)
            if order == "inorder":
                self.inorder_view(self.root_node)
            if order == "postorder":
                self.postorder_view(self.root_node)
