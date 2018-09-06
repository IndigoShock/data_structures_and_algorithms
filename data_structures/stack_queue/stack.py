from .node import Node


class Stack(object):
    def __init__(self, iterable=None):
        """upon initialization, the top's value is nothing.
        and the length starts at 0 since nothing is input.
        if the argument of iterable is not null, then a
        try-except is here. iterating through the stack,
        we will pop all out via index until null is hit.
        if null is hit, a typeerror will throw and pop the
        stack.
        """
        self.top = None
        self._length = 0

    def __len__(self):
        """This shows the length
        """
        return self._length

    def __str__(self):
        """This will show the head and the length
        """
        return f'Head: {self.top} | Length: {self._length}'

    def push(self, val):
        """when pushing, the top will be reassigned to
        the node's value as well as be the new top.
        with each push, the length will increase by one. and return the top.
        """
        self.top = Node(val, self.top)
        self._length += 1

        return self.top

    def pop(self):
        """when popping, a temp node will be reassigned top.
        then the new top's value will be reassigned to the temp's next value.
        and the temp's next value will then be none.
        the length will shorten by 1 and be returned.
        """
        temp = self.top
        self.top = temp._next
        temp._next = None

        self._length -= 1
        return temp

    def peek(self):
        """peeking will show the top's value.
        """
        return self.top
