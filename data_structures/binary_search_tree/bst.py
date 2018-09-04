from .node import Node


class BinaryTree:
    def __init__(self, iterable=None):
        self.root = None

        if iterable is None:
            iterable = []

        for ele in iterable:
            self.insert(ele)

    def __str__(self):
        """This shows the root node
        """
        return f'Root {self.root}'

    def __repr__(self):
        """This also shows the root node but more elegantly
        """
        return f'Binary Tree. The root node is {self.root}'

    def insert(self, val):
        """This will insert the wanted value into a binary tree.
        If the current node is not empty, the value will insert itself as the
        root. But if it is not empty, it will traverse through starting from
        root. And determine whether they are less than or equal to current
        value. If so, assign the value as the left child. If greater than the
        current value, assign the value as right child.
        """

        node = Node(val)
        if self.root is None:
            self.root = node

        current = self.root
        while current:
            if val <= current.val:
                if current.left is None:
                    current.left = node
                    break
                current = current.left

            if val > current.val:
                if current.right is None:
                    current.right = node
                    break
                current = current.right

        return node

    def in_order(self, callable=lambda node: print(node)):
        """Go left, visit, then go right
        """
        def _walk(node=None):
            if node is None:
                return

            # Go left
            if node.left is not None:
                _walk(node.left)

            # Visit
            callable(node)

            # Go right
            if node.right is not None:
                _walk(node.right)

        _walk(self.root)

    def pre_order(self, callable=lambda node: print(node)):
        """Visit, go left, then right
        """
        def _walk(node=None):
            if node is None:
                return

            # Visit
            callable(node)

            # Go left
            if node.left is not None:
                _walk(node.left)

            # Go right
            if node.right is not None:
                _walk(node.right)

        _walk(self.root)

    def post_order(self, callable=lambda node: print(node)):
        """Go left, then right then visit
        """
        def _walk(node=None):
            if node is None:
                return

            # Go left
            if node.left is not None:
                _walk(node.left)

            # Go right
            if node.right is not None:
                _walk(node.right)

            # Visit
            callable(node)

        _walk(self.root)
