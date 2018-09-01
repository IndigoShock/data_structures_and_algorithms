class Node(object):
    def __init__(self, val, data, left=None, right=None):
        self.value = val
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
