# Exercise 4.3
# Выполнение данного цикла может привести к двум результатам
# 1. Если в стеке четное количество элементов, то все они выведутся
#    и цикл завершится
# 2. Если в стеке нечетное количество элементов, то в последней итерации
#    вторым значением выведется None и программа завершится без ошибок, по нашей реализации

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


class HeadStack:
    def __init__(self):
        self.stack = []

    def size(self):
        return len(self.stack)

    def pop(self):
        """
        Exercise 4.2.
        Time complexity: O(n) - always copies elements
        Memory complexity: O(1)
        """
        if len(self.stack) == 0:
            return None
        return self.stack.pop(0)

    def push(self, value):
        """
        Exercise 4.2.
        Time complexity: O(n) - always copies elements
        Memory complexity: O(1)
        """
        return self.stack.insert(0, value)

    def peek(self):
        """
        Exercise 4.2.
        Time complexity: O(1)
        Memory complexity: O(1)
        """
        if self.size() == 0:
            return None
        return self.stack[0]