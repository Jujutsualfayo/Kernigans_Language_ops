import pytest

def test_peek_empty_stack_raises_error():
    stack = ArrayStack()
    
    with pytest.raises(IndexError):
        stack.peek()