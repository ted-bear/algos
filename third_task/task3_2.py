import ctypes
from third_task.task3 import DynArray

class BankDynArray:

    def __init__(self):
        self.count = 0
        self.capacity = 16
        self.operations_count = 0
        self.array = self.make_array(self.capacity)

    def __len__(self):
        return self.count

    def make_array(self, new_capacity):
        return (new_capacity * ctypes.py_object)()

    def __getitem__(self, i):
        if i < 0 or i >= self.count:
            raise IndexError('Index is out of bounds')
        return self.array[i]

    def append(self, itm):
        self.operations_count += 3
        self.resize_if_need()
        self.array[self.count] = itm
        self.count += 1

    def insert(self, i, itm):
        if i < 0 or i > self.count:
            raise IndexError('Index is out of bounds')

        self.operations_count += 3
        self.resize_if_need()
        self.move_right_elements(i)
        self.array[i] = itm
        self.count += 1

    def delete(self, i):
        if i < 0 or i >= self.count:
            raise IndexError('Index is out of bounds')

        self.move_left_elements(i)
        self.count -= 1
        self.squeeze()

    def resize_if_need(self):
        if self.operations_count >= self.capacity:
            new_capacity = 2 * self.capacity
            self.resize(new_capacity)
            cost = self.__eval_cost(new_capacity)
            self.operations_count -= cost

    def resize(self, new_capacity):
        new_array = self.make_array(new_capacity)
        for i in range(self.count):
            new_array[i] = self.array[i]
            self.operations_count += 3
        self.array = new_array
        self.capacity = new_capacity

    def __eval_cost(self, new_capacity):
        cost = 1
        while cost * 2 < new_capacity:
            cost *= 2
        return cost

    def squeeze(self):
        if self.count / self.capacity < 0.5:
            new_capacity = int(self.capacity // 1.5)
            if new_capacity > 16:
                self.resize(new_capacity)

    def move_right_elements(self, idx_from):
        for i in range(self.count, idx_from, -1):
            self.array[i] = self.array[i - 1]

    def move_left_elements(self, idx_from):
        for i in range(idx_from, self.count - 1):
            self.array[i] = self.array[i + 1]


class MultiDimensionalArray:

    def __init__(self, index):
        self.dimensions = index
        self.array = self.create_dimensions(index, 0)

    def append(self, index, value):
        self.validate_idx(index)
        arr = self.array
        for i in range(len(index) - 1):
            arr = arr[index[i]][0]
        arr[index[-1]].append(value)

    def insert(self, index, value):
        position = index[-1]
        index = index[:-1]
        self.validate_idx(index)
        arr = self.array
        for i in range(len(index) - 1):
            arr = arr[index[i]][0]
        arr[index[-1]].insert(position, value)

    def delete(self, index):
        position = index[-1]
        index = index[:-1]
        self.validate_idx(index)
        arr = self.array
        for i in range(len(index) - 1):
            arr = arr[index[i]][0]
        arr[index[-1]].delete(position)

    def getByIndex(self, index):
        position = index[-1]
        index = index[:-1]
        self.validate_idx(index)
        arr = self.array
        for i in range(len(index) - 1):
            arr = arr[index[i]][0]
        return arr[index[-1]].__getitem__(position)

    def create_dimensions(self, dimensions, depth):
        size = dimensions[depth]
        arr = self.make_array(size)

        for i in range(size):
            if depth < len(dimensions) - 1:
                arr[i] = [self.create_dimensions(dimensions, depth + 1)]
            else:
                arr[i] = DynArray()
        return arr

    def make_array(self, new_capacity):
        return (new_capacity * ctypes.py_object)()

    def validate_idx(self, index):
        for i in range(len(index)):
            if index[i] < 0 or index[i] >= self.dimensions[i]:
                raise IndexError(f'Index is out of bounds, max len: {self.dimensions[i]}')
