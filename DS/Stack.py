class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            return None # in case of error
        
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            return None; # in case of error

    def is_empty(self):
        return len(self.stack) == 0
    
    def size(self):
        return len(self.stack)
    
# pvz
s = Stack()
s.push(1)
s.push(2)
s.push(3)
print(s.pop()) # output: 3 (ir panaikina paskutini elementa)
print(s.peek()) # output: 2
print(s.is_empty()) # output: false
print(s.size()) # output: 2
