# Exercise 4.3
# Выполнение данного цикла может привести к двум результатам
# 1. Если в стеке четное количество элементов, то все они выведутся
#    и цикл завершится
# 2. Если в стеке нечетное количество элементов, то в последней итерации
#    вторым значением выведется None и программа завершится без ошибок, по нашей реализации

class Stack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

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
        self.min_stack.pop()
        return self.stack.pop()

    def push(self, value):
        """
        Exercise 4.1.
        Time complexity: o(n)
        Memory complexity: O(1)
        """

        self.evaluate_min(value)
        return self.stack.append(value)

    def evaluate_min(self, value):
        if self.size() > 0:
            cur_min = self.min_stack[-1]
            new_min = cur_min if cur_min < value else value
            self.min_stack.append(new_min)
        else:
            self.min_stack.append(value)


    def peek(self):
        """
        Exercise 4.1.
        Time complexity: O(1)
        Memory complexity: O(1)
        """
        if self.size() == 0:
            return None
        return self.stack[self.size() - 1]
    
    def get_minimum(self):
        """
        Exercise 4.7. Return min element

        Рефлексия: почему то очень часто вылетает из головы, что
        структуры данных очень хорошо миксовать друг с другом или
        как тут использовать одну и ту же структуру для получения
        результата, хотя этот прием один из самых важных в разработке
        Такие вещи - база

        Time complexity: O(1)
        Memory complexity: O(1)
        """
        if self.size() == 0:
            return None
        return self.min_stack[self.size() - 1]


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