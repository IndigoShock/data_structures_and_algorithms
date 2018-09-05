class Node(object):
    def __init__(self, val, data=None, left=None, right=None):
        self.val = val
        self.data = data
        self.left = left
        self.right = right

    def __str__(self, val, data, left, right):
        """
        """
        return f'Val: {self.val} | Data: {self.data}> | Left: {self.left} | Right: {self.right}'

    def __repr__(self, val, data, left, right):
        """repr shows the value and the reference to the node
        next to the current node.
        """
        return f'<Node | Current Val: {self.val} | Data: {self.data}> | The Left Child: {self.left} | The Right Child: {self.right}'


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
            return node

        current = self.root
        while current:
            if val == current.val:
                raise ValueError('Value already exists')
            if val < current.val:
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


class Queue(Node):
    def __init__(self):
        self.front = None
        self.rear = None

    def __len__(self):
        """This shows the length
        """
        return self._length

    def __str__(self):
        """This will show the head and the length
        """
        return f'Front: {self.front} | Length: {self._length} | Rear: {self.rear}'

    def enqueue(self, node):
        self.rear.next = node
        self.rear = node

    def dequeue(self):
        temp = self.front
        self.front = self.front.next
        temp.next = None
        return temp

    def peek(self):
        return self.front


def traverse_breadth_first(Node, root):
    """ Return all the nodes on each level of a binary tree
    """

    breadth = Queue()
    breadth.enqueue(root)

    while breadth.head is not None:
        front = breadth.dequeue()
        print(front.Value)
        if (front.left is not None):
            breadth.enqueue(front.left)
        if (front.right is not None):
            breadth.enqueue(front.right)
