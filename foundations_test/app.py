#implementing the pushmethod
class ArrayStack:
    def __init__(self):
        self._items = []
        
    def push(self,item):
        self._items.append(item)
        
    def pop(self):
        if self.is_empty():
            raise IndexError("Pop an empty stack")
        return self._items.pop()
    
    def is_empty(self):
        return len(self._items) == 0
        
    def __len__(self):
        #return the number of items in the stack
        return len(self._items)
    
stack = ArrayStack()
stack.push(42)

print(len(stack) == 0)


    
        