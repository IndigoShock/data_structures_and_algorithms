from .node import Node


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
