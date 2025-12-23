from argparse import ArgumentError


class Queue:

    def __init__(self):
        self.storage = []
        self.capacity = 0

    def enqueue(self, item):
        """
        Exercise 5.2.

        Time complexity: O(1)
        Memory complexity: O(N)
        """
        self.capacity += 1
        self.storage.append(item)

    def dequeue(self):
        """
        Exercise 5.2.

        Time complexity: O(1)
        Memory complexity: O(1)
        """
        if self.capacity == 0:
            return None

        self.capacity -= 1
        return self.storage.pop(0)

    def size(self):
        """
        Exercise 5.2.

        Time complexity: O(1)
        Memory complexity: O(1)
        """
        return self.capacity

    def rotate(self, count):
        """
        Exercise 5.3.

        Рефлексия: Сначала сделал очередь на связном списке
        потом понял, что тогда вращение будет за Линейное
        время, но, видимо, переписывание ничего не дало

        Time complexity: O(N)
        Memory complexity: O(1)
        """
        if count < 0:
            raise IndexError("Rotate number less then 0")

        rotate_num = count % self.capacity
        if rotate_num != 0:
            self.storage =  self.storage[-rotate_num:] + self.storage[:-rotate_num]