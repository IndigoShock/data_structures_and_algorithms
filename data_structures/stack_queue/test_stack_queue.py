from .stack import Stack
from .queue import Queue
import pytest


@pytest.fixture
def empty_stack():
    return Stack()


@pytest.fixture
def small_stack():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    return stack


@pytest.fixture
def empty_queue():
    return Queue()


def test_stacks_module_exists():
    assert Stack


def test_queue_module_exists():
    assert Queue


def test_can_instantiate_empty_stack(empty_stack):
    assert isinstance(empty_stack, Stack)


def test_insertion_of_value_in_stack_increases_len(empty_stack):
    assert len(empty_stack) == 0
    empty_stack.push(100)
    assert len(empty_stack) == 1


def test_default_value_of_top(empty_stack):
    assert empty_stack.top is None


def test_default_value_of_front(empty_queue):
    assert empty_queue.front is None


def test_default_value_of_rear(empty_queue):
    assert empty_queue.rear is None


def test_can_instantiate_empty_queue(empty_queue):
    assert isinstance(empty_queue, Queue)
