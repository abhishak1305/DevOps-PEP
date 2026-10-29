class Stack:
    def __init__(self):
        self.st = []

    # Insert element at the top
    def push(self, x):
        self.st.append(x)

    # Remove and return the top element
    def pop(self):
        if not self.st:
            return None
        return self.st.pop()

    # Return the top element without removing it
    def peek(self):
        if not self.st:
            return None
        return self.st[-1]

    # Check whether the stack is empty
    def isEmpty(self):
        return len(self.st) == 0

    # Return the number of elements
    def size(self):
        return len(self.st)

    # Remove all elements
    def clear(self):
        self.st.clear()


# Usage
st = Stack()

st.push(10)
st.push(20)
st.push(30)

print(st.peek())     # 30
print(st.pop())      # 30
print(st.size())     # 2
print(st.isEmpty())  # False

st.clear()
print(st.isEmpty())  # True
