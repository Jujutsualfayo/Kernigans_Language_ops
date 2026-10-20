#implementing the pushmethod
class ArrayStack:
    def __init__(self):
        self._items = []
        
    def push(self,item):
        self._items.append(item)
        
    def is_empty(self):
        return len(self._items) == 0
    
    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self._items.pop()
    
    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self._items[-1] 
    
    def __len__(self):
        return len(self._items)
    
    
stack = ArrayStack()

stack.push(10)
stack.push(20)
stack.push(30)

print("Length:", len(stack))
print("Top item:", stack.peek())
print("Removed:", stack.pop())
print("New top:", stack.peek())
print("New length:", len(stack))
print("Empty:", stack.is_empty())
    