import pytest
from array_stack import ArrayStack

def test_pop_is_wokin():
    stack = ArrayStack()
    with pytest.raises(IndexError):
        stack.pop()
def test_peek_is_wokin():
    stack = ArrayStack()
    with pytest.raises(IndexError):
        stack.peek()
def test_pop_returns_last_item():
    stack = ArrayStack()
    stack.push(10)
    stack.push(20)
    stack.push(30)

    removed = stack.pop()

    assert removed == 30
    assert len(stack) == 2
def test_peek_does_not_remove_item():
    stack = ArrayStack()
    stack.push(10)
    stack.push(20)
    stack.push(30)

    result = stack.peek()

    assert result == 30
    assert len(stack) == 3
    assert stack.peek() == 30

