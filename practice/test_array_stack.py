import pytest
from array_stack import ArrayStack

def test_if_pop_is_wokin():
    stack = ArrayStack()
    with pytest.raises(IndexError):
        stack.pop()
