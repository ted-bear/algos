class Deque:
    """
    Exercise 6.1. Сложность для каждой пары методов addHead/removeHead
    addTail/removeTail будет зависеть от того какая структура
    лежит в основе deque.

    Если мы возьмем двусвязный список, то разницы во временной сложности
    не будет, так как удаление одного элемента и в конце и в начале делается
    путем перелинковки.

    Если же в основе лежит массив, то есть непрерывный блок памяти, то
    при вставке в начало нужно сдвигать все последующие элементы вперед, а
    при удалении - назад. Также массив может динамически расширяться, поэтому
    при вставке элемента в конец амортизированная сложность будет линейной.
    """

    def __init__(self):
        self._storage = []
        self._mins = []
        self._size = 0

    def addFront(self, item):
        """
        Exercise 6.1.

        Time complexity: O(N)
        Memory complexity: O(1)
        """
        if item is None:
            raise RuntimeError("None item")

        is_min = self._size == 0 or self._mins[0] > item
        min_el = item if is_min else self._mins[0]
        self._mins.insert(0, min_el)

        self._size += 1
        self._storage.insert(0, item)

    def addTail(self, item):
        """
        Exercise 6.1.

        Time complexity: O(N)
        Memory complexity: O(1)
        """
        if item is None:
            raise RuntimeError("None item")

        is_min = self._size == 0 or self._mins[-1] > item
        min_el = item if is_min else self._mins[-1]
        self._mins.append(min_el)

        self._size += 1
        self._storage.append(item)

    def removeFront(self):
        """
        Exercise 6.1.

        Time complexity: O(1)
        Memory complexity: O(1)
        """
        if self._size == 0:
            return None

        self._size -= 1
        return self._storage.pop(0)

    def removeTail(self):
        """
        Exercise 6.1.

        Time complexity: O(1)
        Memory complexity: O(1)
        """
        if self._size == 0:
            return None

        self._size -= 1
        return self._storage.pop(-1)

    def size(self):
        return self._size

    def get_min(self):
        """
        Exercise 6.4.

        Рефлексия: Задача интересная тем, что
        нужно поддерживать валидность элементов при удалении.
        Если сделать просто добавление минимального
        элемента, как это было в стеке, но добавив
        в обе стороны, мы получим невалидное
        состояние в случае если с одной из сторон
        удалится начальный элемент. На данный момент
        в моей голове только одна реализация:
        добавлять для каждого нового элемента
        новый массив в _mins, который будет относительно
        этого элемента составлять список минимальных
        и тогда при взятии минимального можно будет смотреть
        в лююбой из списков, но при удалении мы будем очищать
        невалидный массив и поддерживать консистентность

        Time complexity: O(1)
        Memory complexity: O(1)
        """

        if self._size == 0:
            return None

        return self._mins[-1] if (self._mins[-1] < self._mins[0]) else self._mins[0]
