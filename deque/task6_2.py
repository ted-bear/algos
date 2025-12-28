from deque.task6 import Deque

def is_palindrome(word) -> bool:
    """
    Exercise 6.3. Проверка палиндрома

    Рефлексия: обычно это задание делаю
    с помощью паттерна двух указателей,
    но тут результат такой же. Единственный вопрос
    нужно ли фильтровать пробелы и различные знаки
    препинания. В варианте без фильтраци алгоритм выглядит
    очень чисто и просто

    Time complexity: O(N)
    Memory complexity: O(N)
    """
    deque = Deque()
    # 1. add all letters from word
    for letter in word:
        deque.addTail(letter)

    # 2. check
    while deque.size() != 0 and deque.size() != 1:
        first = deque.removeFront()
        last = deque.removeTail()

        if first != last:
            return False

    return True

def is_valid_brackets(brackets):
    """
    Exercise 6.6. Проверка скобочной последовательности

    Рефлексия: в варианте с хранением всех занчений
    в структурах данных, гораздо понятнее код, но
    сложность остается прежней

    Time complexity: O(N)
    Memory complexity: O(N)
    """
    deque = Deque()
    bracket_pairs = {
        '(': ')',
        '[': ']',
        '{': '}'
    }
    closing_brackets = {')', ']', '}'}

    for bracket in brackets:
        if bracket in bracket_pairs:
            deque.addTail(bracket)
            continue

        if bracket in closing_brackets:
            if deque.size() == 0:
                return False

            last_opened = deque.removeTail()
            if bracket_pairs[last_opened] != bracket:
                return False

    return deque.size() == 0



class DequeOnList:
    """
    Exercise 6.5. Deque on linked list

    Рефлексия: Данна реализация является
    наиболее ээфективной, так как все операции
    с элементами происходят за O(1)
    """

    def __init__(self):
        self._front = None
        self._tail = None
        self._size = 0

    def addFront(self, item):
        """
        Exercise 6.5.

        Time complexity: O(1)
        Memory complexity: O(1)
        """
        if item is None:
            raise RuntimeError("None item")

        self._size += 1
        new_node = Node(item)
        if self._front is None:
            self._front = new_node
            self._tail = new_node
        else:
            new_node.next = self._front
            self._front.prev = new_node
            self._front = new_node

    def addTail(self, item):
        """
        Exercise 6.5.

        Time complexity: O(1)
        Memory complexity: O(1)
        """
        if item is None:
            raise RuntimeError("None item")

        self._size += 1
        new_node = Node(item)
        if self._front is None:
            self._front = new_node
            self._tail = new_node
        else:
            new_node.prev = self._tail
            self._tail.next = new_node
            self._tail = new_node

    def removeFront(self):
        """
        Exercise 6.5.

        Time complexity: O(1)
        Memory complexity: O(1)
        """
        if self._size == 0:
            return None

        el = self._front.value
        if self._size == 1:
            self._front = None
            self._tail = None
        else:
            self._front = self._front.next
            self._front.prev.next = None
            self._front.prev = None
        self._size -= 1
        return el

    def removeTail(self):
        """
        Exercise 6.5.

        Time complexity: O(1)
        Memory complexity: O(1)
        """
        if self._size == 0:
            return None

        el = self._tail.value
        if self._size == 1:
            self._front = None
            self._tail = None
        else:
            self._tail = self._tail.prev
            self._tail.next.prev = None
            self._tail.next = None
        self._size -= 1
        return el

    def size(self):
        return self._size

class Node:

    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None