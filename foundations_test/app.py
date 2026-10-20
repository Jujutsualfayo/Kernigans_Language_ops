#implementing the pushmethod
class ArrayStack:
    def __init__(self):
        self._items = []
        
    def push(self,item):
        self._items.append(item)