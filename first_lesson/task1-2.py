from first_lesson.task1 import LinkedList
from first_lesson.task1 import Node
import unittest

def sum_linked_lists(first_list: LinkedList, second_list: LinkedList):
    """
    Exercise 1.8. Evaluate sum of elements from two lists
    Time complexity: O(N)
    Memory complexity: O(N)

    Рефлексия:
    """
    if first_list.len() != second_list.len():
        return None

    sum_list = LinkedList()
    first_ptr = first_list.head
    second_ptr = second_list.head

    while first_ptr is not None:
        elements_sum = first_ptr.value + second_ptr.value
        sum_list.add_in_tail(Node(elements_sum))

        first_ptr = first_ptr.next
        second_ptr = second_ptr.next

    return sum_list


class TestSumLists(unittest.TestCase):

    def test_zero_len(self):
        # given
        list1 = LinkedList()
        list2 = LinkedList()

        # when
        merged = sum_linked_lists(list1, list2)
        
        # then
        self.assertEqual(0, merged.len())


    def test_diff_len(self):
        # given
        list1 = LinkedList()
        list2 = LinkedList()
        list2.add_in_tail(Node(12))

        # when
        merged = sum_linked_lists(list1, list2)

        # then
        self.assertEqual(None, merged)

    def test_one_len(self):
        # given
        list1 = LinkedList()
        list1.add_in_tail(Node(13))
        list2 = LinkedList()
        list2.add_in_tail(Node(12))

        # when
        merged = sum_linked_lists(list1, list2)

        # then
        self.assertEqual(1, merged.len())
        self.assertEqual(25, merged.head.value)
        self.assertEqual(25, merged.tail.value)

    def test_different_len(self):
        # given
        list1 = LinkedList()
        list1.add_in_tail(Node(13))
        list1.add_in_tail(Node(13))
        list2 = LinkedList()
        list2.add_in_tail(Node(12))

        # when
        merged = sum_linked_lists(list1, list2)

        # then
        self.assertEqual(None, merged)

    def test_many_same_len(self):
        # given
        list1 = LinkedList()
        list1.add_in_tail(Node(13))
        list1.add_in_tail(Node(14))
        list1.add_in_tail(Node(15))
        list1.add_in_tail(Node(16))
        list2 = LinkedList()
        list2.add_in_tail(Node(1))
        list2.add_in_tail(Node(12))
        list2.add_in_tail(Node(123))
        list2.add_in_tail(Node(1234))

        # when
        merged = sum_linked_lists(list1, list2)

        # then
        self.assertEqual(4, merged.len())
        self.assertEqual(14, merged.head.value)
        self.assertEqual(26, merged.head.next.value)
        self.assertEqual(138, merged.head.next.next.value)
        self.assertEqual(1250, merged.tail.value)



if __name__ == '__main__':
    unittest.main()
    print('Everything passed')
