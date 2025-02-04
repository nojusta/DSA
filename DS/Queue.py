from collections import deque

class Queue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.popleft()
        else:
            return None
        
    def peek(self):
        if not self.is_empty():
            return self.queue[0]
        else:
            return None
        
    def is_empty(self):
        return len(self.queue) == 0
    
    def size(self):
        return len(self.queue)

# pvz
q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.dequeue())  # Output: 1
print(q.peek())     # Output: 2
print(q.is_empty()) # Output: False
print(q.size())     # Output: 2

