from .bst import BinaryTree
import pytest


@pytest.fixture
def empty_tree():
    return BinaryTree()


@pytest.fixture
def small_tree():
    bst = BinaryTree()
    bst.insert(1)
    bst.insert(2)
    bst.insert(3)
    bst.insert(4)
    return bst


def test_bt_module_exists():
    assert BinaryTree


def test_pre_order_module_exists():
    assert BinaryTree.pre_order


def test_in_order_module_exists():
    assert BinaryTree.in_order


def test_post_order_module_exists():
    assert BinaryTree.post_order


def test_insert_module_exists():
    assert BinaryTree.insert


def test_small_tree_exists():
    assert small_tree


def test_insert_small_tree():
    bst = empty_tree()
    bst.insert(small_tree)
    assert bst is not None
