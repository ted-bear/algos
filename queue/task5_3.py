import unittest

from queue.task5 import Queue

if __name__ == "__main__":
    unittest.main()

class TestEnqueueAndSize(unittest.TestCase):

    def test_creation(self):
        # given
        # when
        queue = Queue()
        # then
        self.assertEqual(0, queue.size())

    def test_single_el(self):
        # given
        queue = Queue()
        # when
        queue.enqueue(1)
        # then
        self.assertEqual(1, queue.size())
        self.assertEqual(1, queue.storage[0])

    def test_two_el(self):
        # given
        queue = Queue()
        # when
        queue.enqueue(10)
        queue.enqueue(20)
        # then
        self.assertEqual(2, queue.size())
        self.assertEqual(10, queue.storage[0])
        self.assertEqual(20, queue.storage[1])

    def test_many_el(self):
        # given
        queue = Queue()
        # when
        for i in range(10):
            queue.enqueue(i)
        # then
        self.assertEqual(10, queue.size())
        for i in range(10):
            self.assertEqual(i, queue.storage[i])

    def test_after_deque(self):
        # given
        queue = Queue()
        # when
        for i in range(10):
            queue.enqueue(i)
        deq_el = queue.dequeue()
        # then
        self.assertEqual(9, queue.size())
        self.assertEqual(0, deq_el)

class TestDequeueAndSize(unittest.TestCase):

    def test_single_el(self):
        # given
        queue = Queue()
        queue.enqueue(1)
        # when
        el = queue.dequeue()
        # then
        self.assertEqual(0, queue.size())
        self.assertEqual(1, el)

    def test_one_el(self):
        # given
        queue = Queue()
        queue.enqueue(10)
        queue.enqueue(20)
        # when
        el = queue.dequeue()
        # then
        self.assertEqual(10, el)
        self.assertEqual(1, queue.size())
        self.assertEqual(20, queue.storage[0])

    def test_many_el(self):
        # given
        queue = self.create_and_fill_queue()
        # when
        first = queue.dequeue()
        middle = queue.dequeue()
        last = queue.dequeue()
        # then
        self.assertEqual(7, queue.size())
        self.assertEqual(0, first)
        self.assertEqual(1, middle)
        self.assertEqual(2, last)
        self.assertEqual(3, queue.storage[0])


    def create_and_fill_queue(self):
        queue = Queue()
        for i in range(10):
            queue.enqueue(i)
        return queue

class TestRotate(unittest.TestCase):

    def test_single(self):
        # given
        queue = Queue()
        queue.enqueue(1)
        # when
        queue.rotate(0)
        # then
        self.assertEqual(1, queue.size())
        self.assertEqual(1, queue.storage[0])

    def test_throws_error(self):
        # given
        queue = Queue()
        queue.enqueue(1)
        # when
        with self.assertRaises(IndexError):
            queue.rotate(-1)
        # then
        self.assertEqual(1, queue.size())
        self.assertEqual(1, queue.storage[0])

    def test_two_els_by_one(self):
        # given
        queue = Queue()
        queue.enqueue(2)
        queue.enqueue(1)
        # when
        queue.rotate(1)
        # then
        self.assertEqual(2, queue.size())
        self.assertEqual(1, queue.storage[0])
        self.assertEqual(2, queue.storage[1])

    def test_two_els_by_two(self):
        # given
        queue = Queue()
        queue.enqueue(2)
        queue.enqueue(1)
        # when
        queue.rotate(2)
        # then
        self.assertEqual(2, queue.size())
        self.assertEqual(2, queue.storage[0])
        self.assertEqual(1, queue.storage[1])

    def test_four_els_by_zero(self):
        # given
        queue = Queue()
        queue.enqueue(4)
        queue.enqueue(3)
        queue.enqueue(2)
        queue.enqueue(1)
        # when
        queue.rotate(0)
        # then
        self.assertEqual(4, queue.size())
        self.assertEqual(4, queue.storage[0])
        self.assertEqual(3, queue.storage[1])
        self.assertEqual(2, queue.storage[2])
        self.assertEqual(1, queue.storage[3])

    def test_four_els_by_one(self):
        # given
        queue = Queue()
        queue.enqueue(4)
        queue.enqueue(3)
        queue.enqueue(2)
        queue.enqueue(1)
        # when
        queue.rotate(1)
        # then
        self.assertEqual(4, queue.size())
        self.assertEqual(1, queue.storage[0])
        self.assertEqual(4, queue.storage[1])
        self.assertEqual(3, queue.storage[2])
        self.assertEqual(2, queue.storage[3])