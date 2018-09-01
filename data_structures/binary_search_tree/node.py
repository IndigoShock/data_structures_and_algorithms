class Node(object):
    def __init__(self, val, data, left=None, right=None):
        self.value = val
        self.data = data
        self.left = left
        self.right = right

    def __str__():
        pass

    def __repr__(self, val, data, left, right):
        """repr shows the value and the reference to the node
        next to the current node.
        """
        return f'<Node | Val: {self.val} | Data: {self.data}> | Left Child: {self.left} | Right Child: {self.right}'
