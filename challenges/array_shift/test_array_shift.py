from .array_shift import insertShiftArray
import pytest


def test_array_shift_module_exists():
  assert insertShiftArray


def test_list_gets_reversed_when_odd_number_length():
  #arrange
  expected = [1, 2, 3, 4]

  #act
  actual = insertShiftArray([1, 2, 4], 3)

  #assert
  assert expected == actual

def test_list_gets_reversed_when_even_number_length():
  #arrange
  expected = [1, 2, 3, 4, 5]

  #act
  actual = insertShiftArray([1, 2, 4, 5], 3)

  #assert
  assert expected == actual
