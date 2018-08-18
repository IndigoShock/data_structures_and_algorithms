from typing import Any
from .node import Node


class LinkedList(object):
    def __init__(self, iterable=None):
        self.head = None
        self._length = 0
        if iterable is not None:
            try:
                for value in iterable:
                    self.insert(value)
            except TypeError:
                self.insert(iterable)

    def __str__(self):
        return f'Head: {self.head} | Length: {self._length}'

    def __repr__(self):
        return f'<Linked List | Head: {self.head} | Length: {self._length}>'

    def __len__(self):
        return self._length

    def __iter__(self):
        if self.head:
            self.current = self.head
        return self

    def __next__(self):
        pass

    def insert(self, val: Any) -> Any:
        inserted_node = Node(val, self.head)
        self.head = inserted_node
        self._length += 1
        return

    def includes(self, val: Any) -> bool:
        current = self.head
        while current is not None:
            if current.val == val:
                return True
            current = current._next
        return False
