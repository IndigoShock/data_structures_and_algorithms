from typing import Any


class Node(object):
    """Node class which takes in an object with several methods below
    """
    def __init__(self, val: Any, _next=None):
        """The lines below are the value and reference or the val
        and reference respectively.
        """
        self.val = val
        self._next = _next

    def __str__(self):
        """str shows the value
        """
        return f'{self.val}'

    def __repr__(self):
        """repr shows the value and the reference to the node
        next to the current node.
        """
        return f'<Node | Val: {self.val} | Next: {self._next}>'
