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

