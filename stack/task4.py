class Stack:
    def __init__(self):
        self.stack = []

    def size(self):
        return len(self.stack)

    def pop(self):
        """
        Exercise 4.1.
        Time complexity: O(1)
        Memory complexity: O(1)
        """
        if len(self.stack) == 0:
            return None
        return self.stack.pop()

    def push(self, value):
        """
        Exercise 4.1.
        Time complexity: o(n)
        Memory complexity: O(1)
        """
        return self.stack.append(value)

    def peek(self):
        """
        Exercise 4.1.
        Time complexity: O(1)
        Memory complexity: O(1)
        """
        if self.size() == 0:
            return None
        return self.stack[self.size() - 1]