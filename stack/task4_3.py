import unittest
from stack.task4 import Stack
from stack.task4_2 import is_valid_brackets

if __name__ == "__main__":
    unittest.main()

class TestPushAndSizeStack(unittest.TestCase):

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

class TestPeekStack(unittest.TestCase):

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

class TestPopAndSizeStack(unittest.TestCase):

    def test_from_empty(self):
        # given
        stack = Stack()
        # when
        el = stack.pop()
        # then
        self.assertIsNone(el)
        self.assertEqual(0, stack.size())

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

class TestPushAndSizeHeadStack(unittest.TestCase):

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

class TestPeekHeadStack(unittest.TestCase):

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

class TestPopAndSizeHeadStack(unittest.TestCase):

    def test_from_empty(self):
        # given
        stack = Stack()
        # when
        el = stack.pop()
        # then
        self.assertIsNone(el)
        self.assertEqual(0, stack.size())

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