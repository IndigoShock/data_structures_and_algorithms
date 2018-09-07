from .node import Node


class Queue(object):
    def __init__(self):
        """upon starting up the queue, the front and rear are noted as none
        since the queue doesn't have anything in it yet.
        which means, the length is also 0.
        """
        self.front = None
        self.rear = None
        self._length = 0

    def __len__(self):
        """This shows the length
        """
        return self._length

    def __str__(self):
        """This will show the head and the length
        """
        return f'Front: {self.front} | Length: {self._length} | Rear: {self.rear}'

    def enqueue(self, val):
        # (two if's rear is none)
        node = Node(val)
        # import pdb; pdb.set_trace()
        node._next = self.rear
        self.rear = node

    def dequeue(self):
        temp = self.front
        self.front = self.front._next
        temp._next = None
        return temp

    def peek(self):
        return self.front
