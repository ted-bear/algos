import unittest

from deque.task6 import Deque
from deque.task6_2 import is_palindrome
from deque.task6_2 import DequeOnList
from deque.task6_2 import is_valid_brackets

if __name__ == "__main__":
    unittest.main()

class TestAddFrontAndSize(unittest.TestCase):

    def test_creation(self):
        # given
        # when
        queue = Deque()
        # then
        self.assertEqual(0, queue.size())

    def test_single_el(self):
        # given
        queue = Deque()
        # when
        queue.addFront(1)
        # then
        self.assertEqual(1, queue.size())
        self.assertEqual(1, queue._storage[0])

    def test_two_el(self):
        # given
        queue = Deque()
        # when
        queue.addFront(10)
        queue.addFront(20)
        # then
        self.assertEqual(2, queue.size())
        self.assertEqual(20, queue._storage[0])
        self.assertEqual(10, queue._storage[1])

    def test_many_el(self):
        # given
        queue = Deque()
        # when
        for i in range(10):
            queue.addFront(i)
        # then
        self.assertEqual(10, queue.size())
        for i in range(10):
            el = 9 - i
            self.assertEqual(el, queue._storage[i])

class TestAddTailAndSize(unittest.TestCase):

    def test_creation(self):
        # given
        # when
        queue = Deque()
        # then
        self.assertEqual(0, queue.size())

    def test_single_el(self):
        # given
        queue = Deque()
        # when
        queue.addTail(1)
        # then
        self.assertEqual(1, queue.size())
        self.assertEqual(1, queue._storage[0])

    def test_two_el(self):
        # given
        queue = Deque()
        # when
        queue.addTail(10)
        queue.addTail(20)
        # then
        self.assertEqual(2, queue.size())
        self.assertEqual(10, queue._storage[0])
        self.assertEqual(20, queue._storage[1])

    def test_many_el(self):
        # given
        queue = Deque()
        # when
        for i in range(10):
            queue.addTail(i)
        # then
        self.assertEqual(10, queue.size())
        for i in range(10):
            self.assertEqual(i, queue._storage[i])

class TestAddAndRemoveFrontAndSize(unittest.TestCase):

    def test_empty(self):
        # given
        queue = Deque()
        # when 1
        el = queue.removeFront()
        # then 1
        self.assertEqual(0, queue.size())
        self.assertEqual(None, el)

    def test_single_el(self):
        # given
        queue = Deque()
        # when 1
        queue.addFront(1)
        # then 1
        self.assertEqual(1, queue.size())
        self.assertEqual(1, queue._storage[0])

        # when 2
        el = queue.removeFront()
        # then 2
        self.assertEqual(0, queue.size())
        self.assertEqual(1, el)

    def test_two_el(self):
        # given
        queue = Deque()
        # when
        queue.addFront(10)
        queue.addFront(20)
        # then
        self.assertEqual(2, queue.size())
        self.assertEqual(20, queue._storage[0])
        self.assertEqual(10, queue._storage[1])

        # when 2
        el = queue.removeFront()
        # then 2
        self.assertEqual(1, queue.size())
        self.assertEqual(20, el)

        # when 3
        el = queue.removeFront()
        # then 3
        self.assertEqual(0, queue.size())
        self.assertEqual(10, el)

    def test_many_el(self):
        # given
        queue = Deque()
        # when
        for i in range(10):
            queue.addFront(i)
        # then
        self.assertEqual(10, queue.size())
        for i in range(10):
            self.assertEqual(9 - i, queue.removeFront())
        self.assertEqual(0, queue.size())

class TestAddAndRemoveTailAndSize(unittest.TestCase):

    def test_empty(self):
        # given
        queue = Deque()
        # when 1
        el = queue.removeTail()
        # then 1
        self.assertEqual(0, queue.size())
        self.assertEqual(None, el)

    def test_single_el(self):
        # given
        queue = Deque()
        # when 1
        queue.addTail(1)
        # then 1
        self.assertEqual(1, queue.size())
        self.assertEqual(1, queue._storage[0])

        # when 2
        el = queue.removeTail()
        # then 2
        self.assertEqual(0, queue.size())
        self.assertEqual(1, el)

    def test_two_el(self):
        # given
        queue = Deque()
        # when
        queue.addTail(10)
        queue.addTail(20)
        # then
        self.assertEqual(2, queue.size())
        self.assertEqual(10, queue._storage[0])
        self.assertEqual(20, queue._storage[1])

        # when 2
        el = queue.removeTail()
        # then 2
        self.assertEqual(1, queue.size())
        self.assertEqual(20, el)

        # when 3
        el = queue.removeTail()
        # then 3
        self.assertEqual(0, queue.size())
        self.assertEqual(10, el)

    def test_many_el(self):
        # given
        queue = Deque()
        # when
        for i in range(10):
            queue.addTail(i)
        # then
        self.assertEqual(10, queue.size())
        for i in range(10):
            self.assertEqual(9 - i, queue.removeTail())
        self.assertEqual(0, queue.size())

class TestIsPalindrome(unittest.TestCase):

    def test_empty_word(self):
        # given
        word = ''
        # when
        result = is_palindrome(word)
        # then
        self.assertTrue(result)

    def test_one_letter_word(self):
        # given
        word = 'a'
        # when
        result = is_palindrome(word)
        # then
        self.assertTrue(result)

    def test_two_letter_palindrome(self):
        # given
        word = 'aa'
        # when
        result = is_palindrome(word)
        # then
        self.assertTrue(result)

    def test_two_letter_not_palindrome(self):
        # given
        word = 'ab'
        # when
        result = is_palindrome(word)
        # then
        self.assertFalse(result)

    def test_three_letter_palindrome(self):
        # given
        word = 'aba'
        # when
        result = is_palindrome(word)
        # then
        self.assertTrue(result)

    def test_three_letter_not_palindrome(self):
        # given
        word = 'abb'
        # when
        result = is_palindrome(word)
        # then
        self.assertFalse(result)

    def test_four_letter_palindrome(self):
        # given
        word = 'abba'
        # when
        result = is_palindrome(word)
        # then
        self.assertTrue(result)

    def test_random_not_palindrome(self):
        # given
        word = 'asfdjasdhgsaew'
        # when
        result = is_palindrome(word)
        # then
        self.assertFalse(result)

    def test_long_palindrome(self):
        # given
        word = 'asdfghgfdsa'
        # when
        result = is_palindrome(word)
        # then
        self.assertTrue(result)

class TestListAddFrontAndSize(unittest.TestCase):

    def test_creation(self):
        # given
        # when
        queue = DequeOnList()
        # then
        self.assertEqual(0, queue.size())

    def test_single_el(self):
        # given
        queue = DequeOnList()
        # when
        queue.addFront(1)
        # then
        self.assertEqual(1, queue.size())
        self.assertEqual(1, queue._front.value)

    def test_two_el(self):
        # given
        queue = DequeOnList()
        # when
        queue.addFront(10)
        queue.addFront(20)
        # then
        self.assertEqual(2, queue.size())
        self.assertEqual(20, queue._front.value)
        self.assertEqual(10, queue._tail.value)

    def test_many_el(self):
        # given
        queue = Deque()
        # when
        for i in range(10):
            queue.addFront(i)
        # then
        self.assertEqual(10, queue.size())
        for i in range(10):
            el = 9 - i
            self.assertEqual(el, queue.removeFront())

class TestListAddTailAndSize(unittest.TestCase):

    def test_creation(self):
        # given
        # when
        queue = DequeOnList()
        # then
        self.assertEqual(0, queue.size())

    def test_single_el(self):
        # given
        queue = DequeOnList()
        # when
        queue.addTail(1)
        # then
        self.assertEqual(1, queue.size())
        self.assertEqual(1, queue.removeTail())

    def test_two_el(self):
        # given
        queue = DequeOnList()
        # when
        queue.addTail(10)
        queue.addTail(20)
        # then
        self.assertEqual(2, queue.size())
        self.assertEqual(20, queue.removeTail())
        self.assertEqual(10, queue.removeTail())

    def test_many_el(self):
        # given
        queue = DequeOnList()
        # when
        for i in range(10):
            queue.addTail(i)
        # then
        self.assertEqual(10, queue.size())
        for i in range(10):
            self.assertEqual(9 - i, queue.removeTail())

class TestListAddAndRemoveFrontAndSize(unittest.TestCase):

    def test_empty(self):
        # given
        queue = DequeOnList()
        # when 1
        el = queue.removeFront()
        # then 1
        self.assertEqual(0, queue.size())
        self.assertEqual(None, el)

    def test_single_el(self):
        # given
        queue = DequeOnList()
        # when 1
        queue.addFront(1)
        # then 1
        self.assertEqual(1, queue.size())

        # when 2
        el = queue.removeFront()
        # then 2
        self.assertEqual(0, queue.size())
        self.assertEqual(1, el)

    def test_two_el(self):
        # given
        queue = DequeOnList()
        # when
        queue.addFront(10)
        queue.addFront(20)
        # then
        self.assertEqual(2, queue.size())

        # when 2
        el = queue.removeFront()
        # then 2
        self.assertEqual(1, queue.size())
        self.assertEqual(20, el)

        # when 3
        el = queue.removeFront()
        # then 3
        self.assertEqual(0, queue.size())
        self.assertEqual(10, el)

    def test_many_el(self):
        # given
        queue = DequeOnList()
        # when
        for i in range(10):
            queue.addFront(i)
        # then
        self.assertEqual(10, queue.size())
        for i in range(10):
            self.assertEqual(9 - i, queue.removeFront())
        self.assertEqual(0, queue.size())

class TestListAddAndRemoveTailAndSize(unittest.TestCase):

    def test_empty(self):
        # given
        queue = DequeOnList()
        # when 1
        el = queue.removeTail()
        # then 1
        self.assertEqual(0, queue.size())
        self.assertEqual(None, el)

    def test_single_el(self):
        # given
        queue = DequeOnList()
        # when 1
        queue.addTail(1)
        # then 1
        self.assertEqual(1, queue.size())

        # when 2
        el = queue.removeTail()
        # then 2
        self.assertEqual(0, queue.size())
        self.assertEqual(1, el)

    def test_two_el(self):
        # given
        queue = DequeOnList()
        # when
        queue.addTail(10)
        queue.addTail(20)
        # then
        self.assertEqual(2, queue.size())

        # when 2
        el = queue.removeTail()
        # then 2
        self.assertEqual(1, queue.size())
        self.assertEqual(20, el)

        # when 3
        el = queue.removeTail()
        # then 3
        self.assertEqual(0, queue.size())
        self.assertEqual(10, el)

    def test_many_el(self):
        # given
        queue = DequeOnList()
        # when
        for i in range(10):
            queue.addTail(i)
        # then
        self.assertEqual(10, queue.size())
        for i in range(10):
            self.assertEqual(9 - i, queue.removeTail())
        self.assertEqual(0, queue.size())

class TestGetMin(unittest.TestCase):

    def test_empty(self):
        # given
        queue = Deque()
        # when 1
        el = queue.get_min()
        # then 1
        self.assertEqual(0, queue.size())
        self.assertEqual(None, el)

    def test_single_el(self):
        # given
        queue = Deque()
        queue.addTail(10)
        # when 1
        el = queue.get_min()
        # then 1
        self.assertEqual(1, queue.size())
        self.assertEqual(10, el)

    def test_two_els(self):
        # given
        # deque: [-1 2]
        # mins:  [-1 2]
        queue = Deque()
        queue.addTail(2)
        queue.addFront(-1)
        # when
        el = queue.get_min()
        # then
        self.assertEqual(-1, el)

    def test_three_els(self):
        # given
        # deque: [-1 2 1]
        # mins:  [-1 2 1]
        queue = Deque()
        queue.addTail(2)
        queue.addFront(-1)
        queue.addTail(1)
        # when
        el = queue.get_min()
        # then
        self.assertEqual(-1, el)

    def test_four_after_remove_els(self):
        # given
        queue = Deque()
        queue.addTail(2)
        queue.addFront(-1)
        queue.addTail(1)
        queue.addFront(-1)
        # when
        el = queue.get_min()
        # then
        self.assertEqual(-1, el)

class TestBracketsValidation(unittest.TestCase):

    def test_empty_string(self):
        # given
        brackets = ''
        # when
        is_valid = is_valid_brackets(brackets)
        # then
        self.assertTrue(is_valid)

    def test_open_bracket_string(self):
        # given
        brackets = '('
        # when
        is_valid = is_valid_brackets(brackets)
        # then
        self.assertFalse(is_valid)

    def test_close_bracket_string(self):
        # given
        brackets = ')'
        # when
        is_valid = is_valid_brackets(brackets)
        # then
        self.assertFalse(is_valid)

    def test_two_close_bracket_string(self):
        # given
        brackets = '))'
        # when
        is_valid = is_valid_brackets(brackets)
        # then
        self.assertFalse(is_valid)

    def test_invalid_three(self):
        # given
        brackets = '())'
        # when
        is_valid = is_valid_brackets(brackets)
        # then
        self.assertFalse(is_valid)

    def test_invalid_four(self):
        # given
        brackets = '(()'
        # when
        is_valid = is_valid_brackets(brackets)
        # then
        self.assertFalse(is_valid)

    def test_invalid_five(self):
        # given
        brackets = '(()))'
        # when
        is_valid = is_valid_brackets(brackets)
        # then
        self.assertFalse(is_valid)

    def test_invalid_five_two(self):
        # given
        brackets = '((())'
        # when
        is_valid = is_valid_brackets(brackets)
        # then
        self.assertFalse(is_valid)

    def test_invalid_seven(self):
        # given
        brackets = '()()(()'
        # when
        is_valid = is_valid_brackets(brackets)
        # then
        self.assertFalse(is_valid)

    def test_invalid_seven_two(self):
        # given
        brackets = '()()())'
        # when
        is_valid = is_valid_brackets(brackets)
        # then
        self.assertFalse(is_valid)

    def test_valid_seven_two(self):
        # given
        brackets = '()()(())'
        # when
        is_valid = is_valid_brackets(brackets)
        # then
        self.assertTrue(is_valid)

    def test_valid(self):
        # given
        brackets = '()()(())(()()(()()))'
        # when
        is_valid = is_valid_brackets(brackets)
        # then
        self.assertTrue(is_valid)

    def test_second_diff_bracket_1(self):
        # given
        brackets = '(}'
        # when
        is_valid = is_valid_brackets(brackets)
        # then
        self.assertFalse(is_valid)

    def test_second_diff_bracket_2(self):
        # given
        brackets = '{)'
        # when
        is_valid = is_valid_brackets(brackets)
        # then
        self.assertFalse(is_valid)

    def test_second_diff_bracket_3(self):
        # given
        brackets = '{})'
        # when
        is_valid = is_valid_brackets(brackets)
        # then
        self.assertFalse(is_valid)

    def test_second_diff_bracket_4(self):
        # given
        brackets = '({}'
        # when
        is_valid = is_valid_brackets(brackets)
        # then
        self.assertFalse(is_valid)

    def test_second_diff_bracket_5(self):
        # given
        brackets = '{}'
        # when
        is_valid = is_valid_brackets(brackets)
        # then
        self.assertTrue(is_valid)

    def test_second_diff_bracket_6(self):
        # given
        brackets = '{[]()}[({})]{{{[]({})}()}}'
        # when
        is_valid = is_valid_brackets(brackets)
        # then
        self.assertTrue(is_valid)