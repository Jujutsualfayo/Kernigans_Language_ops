def test_pop_returns_last_item():
    # Create the stack
    stack = ArrayStack()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    # Pop one item
    removed = stack.pop()

    assert removed == 30
    assert len(stack) == 2
        