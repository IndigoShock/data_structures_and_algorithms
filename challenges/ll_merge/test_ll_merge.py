from .linked_list import LinkedList
from .ll_merge import merge
import pytest


@pytest.fixture
def empty_list():
    return LinkedList()


@pytest.fixture
def small_list():
    ll = LinkedList()
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    ll.insert(4)
    return ll


def test_linked_list_merge_returns_not_valid_list(empty_list, empty_list_two):
    """ assert empty lists give back None
    """
    expected = None
    actual = merge(empty_list, empty_list_two)
    assert expected == actual


def test_linked_list_merge_merges_lists_equal_lengths(small_list, empty_list):
    """ Test empty list and list input gives back list
    """
    expected = small_list
    actual = merge(small_list, empty_list)
    assert expected == actual


def test_linked_list_merge_merges_lists_equal_lengths_other(small_list, empty_list):
    """ Test empty list and list input gives back list
    """
    expected = small_list
    actual = merge(empty_list, small_list)
    assert expected == actual


def test_linked_list_ll_merge_exists():
    """ Test merge exists
    """
    assert merge
