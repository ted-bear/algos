import ctypes


class DynArray:

    def __init__(self):
        self.count = 0
        self.capacity = 16
        self.array = self.make_array(self.capacity)

    def __len__(self):
        return self.count

    def make_array(self, new_capacity):
        return (new_capacity * ctypes.py_object)()

    def __getitem__(self, i):
        if i < 0 or i >= self.count:
            raise IndexError('Index is out of bounds')
        return self.array[i]

    def resize(self, new_capacity):
        new_array = self.make_array(new_capacity)
        for i in range(self.count):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity

    def append(self, itm):
        """
        Time complexity: O(1), o(n)
        Memory complexity: O(1)
        """
        if self.count == self.capacity:
            self.resize(2 * self.capacity)
        self.array[self.count] = itm
        self.count += 1

    def insert(self, i, itm):
        """
        Exercise 5.1: insert
        Time complexity: O(n)
        Memory complexity: O(1)
        """
        if i < 0 or i > self.count:
            raise IndexError('Index is out of bounds')

        if self.count == self.capacity:
            self.resize(2 * self.capacity)

        self.move_right_elements(i)
        self.array[i] = itm
        self.count += 1

    def delete(self, i):
        """
        Exercise 5.2: delete
        Time complexity: O(n)
        Memory complexity: O(1)
        """
        if i < 0 or i >= self.count:
            raise IndexError('Index is out of bounds')

        for j in range(i, self.count - 1):
            self.array[j] = self.array[j + 1]

        self.count -= 1
        new_arr = self.make_array(self.capacity)
        for i in range(self.count):
            new_arr[i] = self.array[i]
        self.array = new_arr
        self.squeeze()

    def squeeze(self):
        if self.count * 2 < self.capacity:
            evaluated = int(self.capacity // 1.5)
            new_capacity = evaluated if evaluated > 16 else 16
            self.resize(new_capacity)

    def move_right_elements(self, idx_from):
        for i in range(self.count, idx_from, -1):
            self.array[i] = self.array[i - 1]
