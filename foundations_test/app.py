def test_peek_does_not_remove_item():
    stack = ArrayStack()
    stack.push(10)
    stack.push(20)
    stack.push(30)

    # Step 1: Store the result of peek()
    result = stack.peek()

    # Step 2: Assert that the result is 30
    assert result == 30

    # Step 3: Assert that the stack still contains 3 items
    assert len(stack) == 3

    # Step 4: Assert that another peek() still returns 30
    assert stack.peek() == 30