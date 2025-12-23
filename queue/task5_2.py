from stack.task4 import Stack
import ctypes

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
        return self.capacity


class CycledQueue:
    """
    Exercise 5.6.

    Рефлексия: Интересное задание на
    работу с краевыми случаями

    Time complexity: O(N)
    Memory complexity: O(1)
    """

    def __init__(self, capacity):
        self.capacity = capacity
        self.__size = 0
        self.start = 0
        self.buffer = (capacity * ctypes.py_object)()

    """
    Exercise 5.6.

    Time complexity: O(1)
    Memory complexity: O(1)
    """
    def enqueue(self, item):
        if self.__size == self.capacity:
            raise RuntimeError("Queue is full")

        last_idx = (self.start + self.__size) % self.capacity
        self.buffer[last_idx] = item
        self.__size += 1

    """
    Exercise 5.6.

    Time complexity: O(1)
    Memory complexity: O(1)
    """
    def dequeue(self):
        if self.__size <= 0:
            return None

        el = self.buffer[self.start]
        self.start = 0 if self.start == self.capacity - 1 else self.start + 1
        self.__size -= 1
        return el

    def size(self):
        return self.__size