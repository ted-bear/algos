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