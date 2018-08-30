from .node import Node


class Stack(Node):
    def __init__(self):
        self.top = None
        self._length = None

    def __len__(self):
        """This shows the length
        """
        return self._length

    def __str__(self):
        """This will show the head and the length
        """
        return f'Head: {self.top} | Length: {self._length}'

    def push(self, node):
        node.next = self.top
        self.top = node

    def pop(self):
        temp = self.top
        self.top = self.top.next
        temp.next = None
        return temp

    def peek(self):
        return self.top
