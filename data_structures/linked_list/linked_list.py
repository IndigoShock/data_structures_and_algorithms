from typing import Any
from .node import Node


class LinkedList(object):
    """LinkedList takes in an object and has several methods down below
    """
    def __init__(self, iterable=None):
        """The head has no value at present time. With no length as well.
        If the iterable is not null, iterate through with a for loop
        and insert a value in. Otherwise, show the TypeError.
        """
        self.head = None
        self._length = 0
        if iterable is not None:
            try:
                for value in iterable:
                    self.insert(value)
            except TypeError:
                self.insert(iterable)

    def __str__(self):
        """This will show the head and the length
        """
        return f'Head: {self.head} | Length: {self._length}'

    def __repr__(self):
        """This will be more specific in saying this is a linked list and
        show the head and the length
        """
        return f'<Linked List | Head: {self.head} | Length: {self._length}>'

    def __len__(self):
        """This shows the length
        """
        return self._length

    def __iter__(self):
        """This will iterate through the linkedlist by starting at the head
        and reassigning to the next node
        """
        if self.head:
            self.current = self.head
        return self

    def __next__(self):
        pass

    def insert(self, val: Any) -> Any:
        """This will insert. The new node has the properties of a
        value and reference of head. It'll move over from the head to where
        it needs to based on the length.
        """
        inserted_node = Node(val, self.head)
        self.head = inserted_node
        self._length += 1
        return

    def includes(self, val: Any) -> bool:
        """Similar to insert but will determine whether the value
        we are looking for exists or not via boolean. This will iterate
        through and try to find the value. If it is found, true. If not,
        return false.
        """
        current = self.head
        while current is not None:
            if current.val == val:
                return True
            current = current._next
        return False
