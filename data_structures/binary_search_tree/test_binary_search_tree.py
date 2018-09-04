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


def test_empty_bt():
    bt = BinaryTree()
    assert isinstance(bt, BinaryTree)
    assert bt.root is None


def test_insert_into_empty_bt():
    bt = BinaryTree()
    assert bt.root is not None
    bt.insert(25)
    assert bt.root.value == 25


def test_iterable_creates_bt():
    bt = BinaryTree([20, 18, 12, 19, 11, 14, 40, 31, 22, 33])
    assert bt.root.value == 20
    assert bt.root.left.value == 18
    assert bt.root.right.value == 40


def test_inorder_traversal():
    bt = BinaryTree([20, 18, 12, 19, 11, 14, 40, 31, 22, 33])
    expected = [11, 12, 14, 18, 19, 20, 22, 31, 33, 40]
    actual = []

    def generate_list(node):
        actual.append(node.value)

    bt.in_order(generate_list)
    assert expected == actual


def test_insert_value_that_already_exists():
    bt = BinaryTree([25])
    bt.insert(25)
    with pytest.raises(ValueError):
        bt.insert(25)
