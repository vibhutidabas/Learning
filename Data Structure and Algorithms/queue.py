#FIFO (first in first out)

class Queue:
    def __init__(self):
        self.q = []

    def enqueue(self, data):
        self.q.append(data)

    def dequeue(self):
        if self.size() < 1:
            return "underflow"
        p = self.q[0]
        del self.q[0]
        return p

    def peek(self):
        return self.q[0]

    def size(self):
        return len(self.q)

    def is_empty(self):
        return self.q == []

queue = Queue() 