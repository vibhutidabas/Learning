#LIFO (last in first out)

class Stack:
    def __init__(self):
        self.s = []

    def push(self, data):
        self.s.append(data)

    def pop(self):
        if self.size() < 1:
            return -1
        p = self.s[-1]
        del self.s[-1]
        return p

    def peek(self):
        return self.s[-1]

    def is_empty(self):
        return self.s == []

    def size(self):
        return len(self.s)

st = Stack()
st.push(1)
st.push(2)
st.push(3)
print(st.pop())