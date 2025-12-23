from stack.task4 import Stack


class StackQueue:
    """
    Exercise 5.4. stack queue

    Рефлексия: Такие приседния с перегоном
    элементов туда сюда не нравятся, но
    как это оптимизировать не придумал(

    """
    def __init__(self):
        self.stack = Stack()
        self.additional = Stack()
        self.capacity = 0

    """
    Exercise 5.4.

    Time complexity: O(1)
    Memory complexity: O(1)
    """
    def enqueue(self, item):
        self.capacity += 1
        self.stack.push(item)
    # вставка в хвост

    """
    Exercise 5.4.

    Time complexity: O(N)
    Memory complexity: O(1)
    """
    def dequeue(self):
        if self.capacity <= 0:
            return None

        while self.stack.size() != 0:
            self.additional.push(self.stack.pop())

        element = self.additional.pop()

        while self.additional.size() != 0:
            self.stack.push(self.additional.pop())

        self.capacity -= 1
        return element

    def size(self):
        return self.capacity  # размер очереди