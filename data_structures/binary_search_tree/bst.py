class BinaryTree:
    def __init__(self, iterable=None):
        self.root = None

    def __str__(self):
        pass

    def __repr__(self):
        pass

    def insert(self, callable=lambda node: print(node)):
        """
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
