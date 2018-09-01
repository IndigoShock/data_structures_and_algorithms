class BinaryTree:
    def __init__(self, iterable=None):
        self.root = None

    def __str__(self):
        """This shows the root node
        """
        return f'Root {self.root}'

    def __repr__(self):
        """This also shows the root node but more elegantly
        """
        return f'Binary Tree. The root node is {self.root}'

    def insert(self, callable=lambda node: print(node)):
        """This will insert the wanted value into a binary tree.
        If the current node is not empty, the value will insert itself as the
        root. But if it is not empty, it will traverse through starting from
        root. And determine whether they are less than or equal to current
        value. If so, assign the value as the left child. If greater than the
        current value, assign the value as right child.
        """
        def _walk(root, new_node=None):
            if root is not None:
                root = new_node

            if new_node.val <= root.val:
                if root.left is not None:
                    _walk(self.root.left, new_node)

                else:
                    root.left = new_node

            if new_node.val > root.val:
                if root.right is not None:
                    _walk(self.root.right, new_node)

                else:
                    root.right = new_node

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
