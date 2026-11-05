import pytest

from src.custom_stack_class import CustomStack, StackEmptyException, StackFullException


def test_new_stack_is_empty():
    cut = CustomStack(5)

    assert cut.is_empty()
    assert cut.size() == 0


def test_push_one_element_in_stack():
    element_value = 5.0

    cut = CustomStack(5)
    cut.push(element_value)

    assert not cut.is_empty()
    assert cut.top() == element_value
    assert cut.size() == 1


def test_push_until_limit_keeps_all_elements():
    cut = CustomStack(3)

    for value in (1, 2, 3):
        cut.push(value)

    assert cut.size() == 3
    assert cut.top() == 3


def test_push_on_full_stack_raises_exception():
    cut = CustomStack(2)
    cut.push(1)
    cut.push(2)

    with pytest.raises(StackFullException):
        cut.push(3)

    assert cut.size() == 2
    assert cut.top() == 2


def test_top_does_not_remove_element():
    cut = CustomStack(5)
    cut.push(7)

    assert cut.top() == 7
    assert cut.top() == 7
    assert cut.size() == 1


def test_top_on_empty_stack_raises_exception():
    cut = CustomStack(5)

    with pytest.raises(StackEmptyException):
        cut.top()


def test_pop_returns_elements_in_lifo_order():
    cut = CustomStack(5)
    cut.push(1)
    cut.push(2)
    cut.push(3)

    assert cut.pop() == 3
    assert cut.pop() == 2
    assert cut.pop() == 1
    assert cut.is_empty()


def test_pop_on_empty_stack_raises_exception():
    cut = CustomStack(5)

    with pytest.raises(StackEmptyException):
        cut.pop()
