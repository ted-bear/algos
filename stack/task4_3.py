import unittest
from stack.task4 import Stack
from stack.task4_2 import is_valid_brackets
from stack.task4_2 import evaluate_in_postfix

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

class TestGetMinimum(unittest.TestCase):

    def test_empty_stack(self):
        # given
        stack = Stack()
        # when
        min_el = stack.get_minimum()
        # then
        self.assertIsNone(min_el)

    def test_one_el_stack(self):
        # given
        stack = Stack()
        stack.push(1)
        # when
        min_el = stack.get_minimum()
        # then
        self.assertEqual(1, min_el)

    def test_two_min_in_head(self):
        # given
        stack = Stack()
        stack.push(1)
        stack.push(2)
        # when
        min_el = stack.get_minimum()
        # then
        self.assertEqual(1, min_el)

    def test_min_in_tail(self):
        # given
        stack = Stack()
        stack.push(2)
        stack.push(1)
        # when
        min_el = stack.get_minimum()
        # then
        self.assertEqual(1, min_el)

    def test_min_in_middle(self):
        # given
        stack = Stack()
        stack.push(2)
        stack.push(1)
        stack.push(3)
        # when
        min_el = stack.get_minimum()
        # then
        self.assertEqual(1, min_el)

    def test_all_min(self):
        # given
        stack = Stack()
        stack.push(1)
        stack.push(1)
        stack.push(1)
        # when
        min_el = stack.get_minimum()
        # then
        self.assertEqual(1, min_el)

    def test_min_somewhere(self):
        for i in range(1000):
            # given
            stack, el = generate_stack_for_min()
            # when
            min_el = stack.get_minimum()
            # then
            self.assertEqual(el, min_el)

    def test_min_after_del_not_min(self):
        # given
        stack = Stack()
        stack.push(5)
        stack.push(7)
        stack.push(1)
        stack.push(2)
        # when
        min_el = stack.get_minimum()
        stack.pop()
        # then
        self.assertEqual(1, min_el)

    def test_min_after_del_min(self):
        # given
        stack = Stack()
        stack.push(7)
        stack.push(2)
        stack.push(3)
        stack.push(1)
        # when
        stack.pop()
        min_el = stack.get_minimum()
        # then
        self.assertEqual(2, min_el)

    def test_min_after_del_two_mins(self):
        # given
        stack = Stack()
        stack.push(9)
        stack.push(10)
        stack.push(7)
        stack.push(2)
        stack.push(3)
        stack.push(1)
        # when
        stack.pop()
        stack.pop()
        stack.pop()
        min_el = stack.get_minimum()
        # then
        self.assertEqual(7, min_el)

class TestGetAverage(unittest.TestCase):

    def test_empty(self):
        # given
        stack = Stack()
        # when
        avg = stack.get_average()
        # then
        self.assertEqual(None, avg)

    def test_single_el(self):
        # given
        stack = Stack()
        stack.push(1)
        # when
        avg = stack.get_average()
        # then
        self.assertEqual(1, avg)

    def test_two_els(self):
        # given
        stack = Stack()
        stack.push(1)
        stack.push(3)
        # when
        avg = stack.get_average()
        # then
        self.assertEqual(2, avg)

    def test_many_els(self):
        # given
        stack = Stack()
        stack.push(1)
        stack.push(3)
        stack.push(11)
        stack.push(1)
        # when
        avg = stack.get_average()
        # then
        self.assertEqual(4, avg)

    def test_many_after_del(self):
        # given
        stack = Stack()
        stack.push(2)
        stack.push(14)
        stack.push(11)
        stack.push(2)
        # when
        stack.pop()
        avg = stack.get_average()
        # then
        self.assertEqual(9, avg)

    def test_many_random_els(self):
        for i in range(1000):
            # given
            stack, avg_expected = generate_stack_for_avg()
            # when
            avg = stack.get_average()
            # then
            self.assertEqual(avg_expected, avg)

class TestPrefixExpressionEvaluator(unittest.TestCase):

    def test_empty_exp(self):
        # given
        exp = ''
        # when
        res = evaluate_in_postfix(exp)
        # then
        self.assertEqual(None, res)

    def test_single_exp(self):
        # given
        exp = '1 ='
        # when
        res = evaluate_in_postfix(exp)
        # then
        self.assertEqual(1, int(res))

    def test_sum_exp(self):
        # given
        exp = '1 1 + ='
        # when
        res = evaluate_in_postfix(exp)
        # then
        self.assertEqual(2, int(res))

    def test_multiply_exp(self):
        # given
        exp = '2 2 * ='
        # when
        res = evaluate_in_postfix(exp)
        # then
        self.assertEqual(4, int(res))

    def test_multiply_and_sum_exp(self):
        # given
        exp = '2 2 * 3 + ='
        # when
        res = evaluate_in_postfix(exp)
        # then
        self.assertEqual(7, int(res))

    def test_from_example(self):
        # given
        exp = '8 2 + 5 * 9 + ='
        # when
        res = evaluate_in_postfix(exp)
        # then
        self.assertEqual(59, int(res))


def generate_stack_for_min():
    import random
    stack = Stack()
    rand_size = random.randint(1, 100)
    min_el = 101
    for i in range(rand_size):
        el = random.randint(-100, 100)
        stack.push(el)
        min_el = min(el, min_el)
    return stack, min_el

def generate_stack_for_avg():
    import random
    stack = Stack()
    rand_size = random.randint(1, 100)
    sums = 0
    for i in range(rand_size):
        el = random.randint(-100, 100)
        stack.push(el)
        sums += el
    avg = sums / rand_size
    return stack, avg