#implementing the pushmethod
class ArrayStack:
    def __init__(self):
        self._items = []
        
    def push(self,item):
        self._items.append(item)
        
stack = ArrayStack()

stack.push(5)
stack.push(15)
stack.push(25)

print(stack._items)       