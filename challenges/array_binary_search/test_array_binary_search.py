from .array_binary_search import binary_search
import pytest


def test_binary_search_module_exists():
    assert binary_search


def test_array_functions_properly():
    # act
    expected = 2

    # arrange
    actual = binary_search([1, 2, 3, 4, 5], 3)

    # assert
    assert expected == actual


def test_array_is_odd_length():
    # act
    expected = 1

    # arrange
    actual = binary_search([1, 2, 3], 2)

    # assert
    assert expected == actual


def test_array_is_even_length():
    # act
    expected = 3

    # arrange
    actual = binary_search([1, 2, 3, 4, 5, 6], 4)

    # assert
    assert expected == actual


def test_array_is_empty():
    # act
    expected = -1

    # arrange
    actual = binary_search([], -1)

    # assert
    assert expected == actual
