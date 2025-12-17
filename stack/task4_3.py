import unittest
from stack.task4 import Stack

if __name__ == "__main__":
    unittest.main()

class TestPushClass(unittest.TestCase):

    def test_into_empty(self):
        # given
        stack = Stack()
        # when
        stack.push(1)
        # then
        self.assertEqual(1, stack.peek())
        self.assertEqual(1, stack.size())

    def test_into_single_el(self):
        # given
        stack = Stack()
        stack.push(10)
        # when
        stack.push(1)
        # then
        self.assertEqual(1, stack.peek())
        self.assertEqual(2, stack.size())

    def test_into_full(self):
        # given
        stack = Stack()
        stack.push(10)
        stack.push(20)
        stack.push(30)
        # when
        stack.push(1)
        # then
        self.assertEqual(1, stack.peek())
        self.assertEqual(4, stack.size())

class TestPeekClass(unittest.TestCase):

    def test_from_empty(self):
        # given
        stack = Stack()
        # when
        el = stack.peek()
        # then
        self.assertIsNone(el)

    def test_into_single_el(self):
        # given
        stack = Stack()
        stack.push(10)
        # when
        el = stack.peek()
        # then
        self.assertEqual(10, el)

    def test_into_full(self):
        # given
        stack = Stack()
        stack.push(10)
        stack.push(20)
        stack.push(30)
        # when
        el = stack.peek()
        # then
        self.assertEqual(30, el)

class TestPopClass(unittest.TestCase):

    def test_from_empty(self):
        # given
        stack = Stack()
        # when
        el = stack.pop()
        # then
        self.assertIsNone(el)

    def test_from_single_el(self):
        # given
        stack = Stack()
        stack.push(10)
        # when
        el = stack.pop()
        # then
        self.assertEqual(10, el)
        self.assertEqual(0, stack.size())

    def test_from_full(self):
        # given
        stack = Stack()
        stack.push(10)
        stack.push(20)
        stack.push(30)
        # when
        el = stack.pop()
        # then
        self.assertEqual(30, el)
        self.assertEqual(2, stack.size())
        self.assertEqual(20, stack.pop())
        self.assertEqual(1, stack.size())
        self.assertEqual(10, stack.pop())
        self.assertEqual(0, stack.size())