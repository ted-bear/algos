from second_lesson.task2 import LinkedList2, Node
from second_lesson.task2_2 import reverse_linked_list
from second_lesson.task2_2 import has_cycle
from second_lesson.task2_2 import sort_list
from second_lesson.task2_2 import sort_and_merge_list
import unittest

if __name__ == '__main__':
    unittest.main()

class TestFind(unittest.TestCase):

    def test_find_empty(self):
        # given
        ll = LinkedList2()
        # when
        node = ll.find(1)
        # then
        self.assertIsNone(node)

    def test_single_el_found(self):
        # given
        ll = LinkedList2()
        ll.add_in_tail(Node(1))
        # when
        node = ll.find(1)
        # then
        self.assertIsNotNone(node)
        self.assertEqual(1, node.value)

    def test_single_el_not_found(self):
        # given
        ll = LinkedList2()
        ll.add_in_tail(Node(1))
        # when
        node = ll.find(2)
        # then
        self.assertIsNone(node)

    def test_many_el_found(self):
        # given
        ll = create_1234_linked_list()
        # when
        node = ll.find(2)
        # then
        self.assertIsNotNone(node)
        self.assertEqual(2, node.value)

    def test_many_el_not_found(self):
        # given
        ll = create_1234_linked_list()
        # when
        node = ll.find(10)
        # then
        self.assertIsNone(node)

class TestFindAll(unittest.TestCase):

    def test_find_all_in_empty(self):
        # given
        linked_list = LinkedList2()
        # when
        founded = linked_list.find_all(1)
        # then
        self.assertEqual(len(founded), 0)


    def test_find_all_in_single(self):
        # given
        linked_list = LinkedList2()
        linked_list.add_in_tail(Node(1))
        # when
        founded = linked_list.find_all(1)
        # then
        self.assertEqual(len(founded), 1)
        self.assertEqual(founded[0].value, 1)


    def test_find_all_single_el(self):
        # given
        linked_list = create_duplicated_linked_list()
        # when
        founded = linked_list.find_all(2)
        # then
        self.assertEqual(len(founded), 1)
        self.assertEqual(founded[0].value, 2)


    def test_find_all_multiple_el(self):
        # given
        linked_list = create_duplicated_linked_list()
        # when
        founded = linked_list.find_all(7)
        # then
        self.assertEqual(len(founded), 2)
        self.assertEqual(founded[0].value, 7)

class TestDelete(unittest.TestCase):

    def test_delete_head_el(self):
        # given
        linked_list = create_1234_linked_list()
        # when
        linked_list.delete(1)
        # then
        self.assertEqual(linked_list.head.value, 2)
        self.assertEqual(linked_list.head.next.value, 3)
        self.assertEqual(linked_list.tail.value, 4)

    def test_delete_tail_el(self):
        # given
        linked_list = create_1234_linked_list()
        # when
        linked_list.delete(4)
        # then
        self.assertEqual(linked_list.head.value, 1)
        self.assertEqual(linked_list.head.next.value, 2)
        self.assertEqual(linked_list.tail.value, 3)

    def test_delete_middle_el(self):
        # given
        linked_list = create_1234_linked_list()
        # when
        linked_list.delete(2)
        # then
        self.assertEqual(linked_list.head.value, 1)
        self.assertEqual(linked_list.head.next.value, 3)
        self.assertEqual(linked_list.tail.value, 4)

    def test_delete_single_el(self):
        # given
        node = Node(1)
        linked_list = LinkedList2()
        linked_list.add_in_tail(node)
        # when
        linked_list.delete(1)
        # then
        self.assertEqual(linked_list.head, None)
        self.assertEqual(linked_list.tail, None)

    def test_delete_from_two_len_tail_el(self):
        # given
        node1 = Node(1)
        node2 = Node(2)
        linked_list = LinkedList2()
        linked_list.add_in_tail(node1)
        linked_list.add_in_tail(node2)
        # when
        linked_list.delete(2)
        # then
        self.assertEqual(linked_list.head.value, 1)
        self.assertEqual(linked_list.tail.value, 1)

    def test_delete_from_two_len_head_el(self):
        # given
        node1 = Node(1)
        node2 = Node(2)
        linked_list = LinkedList2()
        linked_list.add_in_tail(node1)
        linked_list.add_in_tail(node2)
        # when
        linked_list.delete(1)
        # then
        self.assertEqual(linked_list.head.value, 2)
        self.assertEqual(linked_list.tail.value, 2)

class TestDeleteAll(unittest.TestCase):

    def test_delete_all_head_el(self):
        # given
        linked_list = create_head_linked_list()
        # when
        linked_list.delete(1, all=True)
        # then
        self.assertEqual(linked_list.head, None)
        self.assertEqual(linked_list.len(), 0)

    def test_delete_all_heads_el(self):
        # given
        linked_list = create_pairs_linked_list()
        # when
        linked_list.delete(1, all=True)
        # then
        self.assertEqual(linked_list.head.value, 2)
        self.assertEqual(linked_list.tail.value, 3)
        self.assertEqual(linked_list.len(), 4)

    def test_delete_all_tails_el(self):
        # given
        linked_list = create_pairs_linked_list()
        # when
        linked_list.delete(3, all=True)
        # then
        self.assertEqual(linked_list.head.value, 1)
        self.assertEqual(linked_list.tail.value, 2)
        self.assertEqual(linked_list.len(), 4)

    def test_delete_middle_el(self):
        # given
        linked_list = create_pairs_linked_list()
        # when
        linked_list.delete(2, all=True)
        # then
        self.assertEqual(linked_list.head.value, 1)
        self.assertEqual(linked_list.tail.value, 3)
        self.assertEqual(linked_list.len(), 4)

    def test_delete_all_one_el(self):
        # given
        linked_list = create_duplicated_linked_list()
        # when
        linked_list.delete(2, all=True)
        # then
        self.assertEqual(linked_list.head.value, 1)
        self.assertEqual(linked_list.tail.value, 5)
        self.assertEqual(linked_list.len(), 7)

    def test_delete_all_head_middle_el(self):
        # given
        linked_list = create_duplicated_linked_list()
        # when
        linked_list.delete(1, all=True)
        # then
        self.assertEqual(linked_list.head.value, 2)
        self.assertEqual(linked_list.tail.value, 5)
        self.assertEqual(linked_list.len(), 6)

    def test_delete_all_middles_el(self):
        # given
        linked_list = create_duplicated_linked_list()
        # when
        linked_list.delete(7, all=True)
        # then
        self.assertEqual(linked_list.head.value, 1)
        self.assertEqual(linked_list.tail.value, 5)
        self.assertEqual(linked_list.len(), 6)

    def test_delete_all_tail_middle_el(self):
        # given
        linked_list = create_duplicated_linked_list()
        # when
        linked_list.delete(5, all=True)
        # then
        self.assertEqual(linked_list.head.value, 1)
        self.assertEqual(linked_list.tail.value, 7)
        self.assertEqual(linked_list.len(), 6)

class TestInsert(unittest.TestCase):

    def test_insert_empty(self):
        # given
        linked_list = LinkedList2()

        # when
        linked_list.insert(None, Node(1))

        # then
        self.assertEqual(1, linked_list.len())
        self.assertEqual(1, linked_list.head.value)
        self.assertEqual(1, linked_list.tail.value)

    def test_insert_in_single(self):
        # given
        linked_list = LinkedList2()
        node1 = Node(1)
        node2 = Node(2)
        node3 = Node(3)

        # when
        linked_list.insert(None, node1)
        linked_list.insert(node1, node2)
        linked_list.insert(None, node3)

        # then
        self.assertEqual(3, linked_list.len())
        self.assertEqual(1, linked_list.head.value)
        self.assertEqual(3, linked_list.tail.value)
        self.assertEqual(2, linked_list.tail.prev.value)

    def test_insert_last_el(self):
        # given
        linked_list = LinkedList2()
        node1 = Node(1)
        node2 = Node(2)
        node3 = Node(3)

        # when
        linked_list.insert(None, node1)
        linked_list.insert(node1, node2)
        linked_list.insert(node2, node3)

        # then
        self.assertEqual(3, linked_list.len())
        self.assertEqual(1, linked_list.head.value)
        self.assertEqual(3, linked_list.tail.value)

    def test_insert_middle_el(self):
        # given
        linked_list = LinkedList2()
        node1 = Node(1)
        node2 = Node(2)
        node3 = Node(3)
        node4 = Node(4)


        # when
        linked_list.insert(None, node1)
        linked_list.insert(node1, node2)
        linked_list.insert(node2, node3)
        linked_list.insert(node2, node4)

        # then
        self.assertEqual(4, linked_list.len())
        self.assertEqual(1, linked_list.head.value)
        self.assertEqual(3, linked_list.tail.value)
        self.assertEqual(4, linked_list.head.next.next.value)

    def test_insert_after_middle(self):
        node1 = Node(1)
        node2 = Node(2)
        node3 = Node(3)
        node5 = Node(5)
        ll = LinkedList2()
        ll.add_in_tail(node1)
        ll.add_in_tail(node2)
        ll.add_in_tail(node3)
        ll.add_in_tail(node5)

        # when
        node4 = Node(4)
        ll.insert(node3, node4)

        # then
        self.assertEqual(5, ll.len())
        self.assertEqual(1, ll.head.value)
        self.assertEqual(2, ll.head.next.value)
        self.assertEqual(3, ll.head.next.next.value)
        self.assertEqual(4, ll.head.next.next.next.value)
        self.assertEqual(5, ll.head.next.next.next.next.value)
        self.assertEqual(5, ll.tail.value)
        self.assertEqual(4, ll.tail.prev.value)
        self.assertEqual(3, ll.tail.prev.prev.value)
        self.assertEqual(2, ll.tail.prev.prev.prev.value)
        self.assertEqual(1, ll.tail.prev.prev.prev.prev.value)

    def test_insert_after_tail(self):
        node1 = Node(1)
        node2 = Node(2)
        node3 = Node(3)
        node4 = Node(4)
        ll = LinkedList2()
        ll.add_in_tail(node1)
        ll.add_in_tail(node2)
        ll.add_in_tail(node3)
        ll.add_in_tail(node4)

        # when
        node5 = Node(5)
        ll.insert(node4, node5)

        # then
        self.assertEqual(5, ll.len())
        self.assertEqual(1, ll.head.value)
        self.assertEqual(2, ll.head.next.value)
        self.assertEqual(3, ll.head.next.next.value)
        self.assertEqual(4, ll.head.next.next.next.value)
        self.assertEqual(5, ll.head.next.next.next.next.value)
        self.assertEqual(5, ll.tail.value)
        self.assertEqual(4, ll.tail.prev.value)
        self.assertEqual(3, ll.tail.prev.prev.value)
        self.assertEqual(2, ll.tail.prev.prev.prev.value)
        self.assertEqual(1, ll.tail.prev.prev.prev.prev.value)


    def test_insert_in_tail(self):
        # given
        ll = create_1234_linked_list()
        node10 = Node(10)

        # when
        ll.insert(None, node10)

        # then
        self.assertEqual(5, ll.len())
        self.assertEqual(1, ll.head.value)
        self.assertEqual(10, ll.tail.value)
        self.assertEqual(4, ll.tail.prev.value)


class TestClean(unittest.TestCase):

    def test_empty_list(self):
        # given
        linked_list = LinkedList2()

        # when
        linked_list.clean()

        # then
        self.assertEqual(0 , linked_list.len())
        self.assertEqual(None , linked_list.head)
        self.assertEqual(None , linked_list.tail)

    def test_single_el_list(self):
        # given
        linked_list = LinkedList2()
        linked_list.add_in_tail(Node(1))

        # when
        linked_list.clean()

        # then
        self.assertEqual(0 , linked_list.len())
        self.assertEqual(None , linked_list.head)
        self.assertEqual(None , linked_list.tail)

    def test_many_el_list(self):
        # given
        linked_list = create_duplicated_linked_list()

        # when
        linked_list.clean()

        # then
        self.assertEqual(0 , linked_list.len())
        self.assertEqual(None , linked_list.head)
        self.assertEqual(None , linked_list.tail)

class TestLenList(unittest.TestCase):

    def test_empty_list(self):
        # given
        linked_list = LinkedList2()

        # then
        self.assertEqual(0, linked_list.len())

    def test_after_insert_empty_list(self):
        # given
        linked_list = LinkedList2()
        linked_list.insert(None, Node(1))

        # then
        self.assertEqual(1, linked_list.len())
        self.assertEqual(1, linked_list.head.value)

    def test_after_insert_list(self):
        # given
        linked_list = LinkedList2()
        node1 = Node(1)
        linked_list.insert(None, node1)
        linked_list.insert(node1, Node(2))

        # then
        self.assertEqual(2, linked_list.len())
        self.assertEqual(1, linked_list.head.value)
        self.assertEqual(2, linked_list.tail.value)

    def test_after_append_single_list(self):
        # given
        linked_list = LinkedList2()
        linked_list.add_in_tail(Node(1))

        # then
        self.assertEqual(1, linked_list.len())
        self.assertEqual(1, linked_list.head.value)
        self.assertEqual(1, linked_list.tail.value)

    def test_after_append_list(self):
        # given
        linked_list = LinkedList2()
        linked_list.add_in_tail(Node(1))
        linked_list.add_in_tail(Node(2))

        # then
        self.assertEqual(2, linked_list.len())
        self.assertEqual(1, linked_list.head.value)
        self.assertEqual(2, linked_list.tail.value)

    def test_after_delete_list(self):
        # given
        linked_list = LinkedList2()
        linked_list.add_in_tail(Node(1))
        linked_list.add_in_tail(Node(2))
        self.assertEqual(2, linked_list.len())

        linked_list.delete(2)

        # then
        self.assertEqual(1, linked_list.len())
        self.assertEqual(1, linked_list.head.value)
        self.assertEqual(1, linked_list.tail.value)

    def test_after_delete_list_single(self):
        # given
        linked_list = LinkedList2()
        linked_list.add_in_tail(Node(1))
        self.assertEqual(1, linked_list.len())

        linked_list.delete(1)

        # then
        self.assertEqual(0, linked_list.len())
        self.assertEqual(None, linked_list.head)
        self.assertEqual(None, linked_list.tail)

    def test_after_delete_many_list(self):
        # given
        linked_list = LinkedList2()
        linked_list.add_in_tail(Node(1))
        linked_list.add_in_tail(Node(1))
        linked_list.add_in_tail(Node(2))
        self.assertEqual(3, linked_list.len())

        linked_list.delete(1, True)

        # then
        self.assertEqual(1, linked_list.len())
        self.assertEqual(linked_list.head, linked_list.tail)
        self.assertEqual(2, linked_list.head.value)
        self.assertEqual(2, linked_list.tail.value)

class TestAddInHead(unittest.TestCase):

    def test_in_empty(self):
        # given
        ll = LinkedList2()
        # when
        ll.add_in_head(Node(1))
        # then
        self.assertEqual(1, ll.len())
        self.assertEqual(1, ll.head.value)
        self.assertEqual(1, ll.tail.value)

    def test_in_single(self):
        # given
        ll = LinkedList2()
        ll.add_in_head(Node(1))
        # when
        ll.add_in_head(Node(3))
        # then
        self.assertEqual(2, ll.len())
        self.assertEqual(3, ll.head.value)
        self.assertEqual(1, ll.tail.value)

    def test_in_many(self):
        # given
        ll = create_1234_linked_list()
        # when
        ll.add_in_head(Node(3))
        # then
        self.assertEqual(5, ll.len())
        self.assertEqual(3, ll.head.value)
        self.assertEqual(4, ll.tail.value)

    def test_many_els(self):
        # given
        ll = create_shuffled_linked_list()
        # when
        ll.add_in_head(Node(8))
        # then
        self.assertEqual(6, ll.len())
        self.assertIsNone(ll.head.prev)
        self.assertEqual(8, ll.head.value)
        self.assertEqual(2, ll.head.next.value)
        self.assertEqual(8, ll.head.next.prev.value)
        self.assertEqual(3, ll.tail.value)

class TestReverse(unittest.TestCase):

    def test_empty(self):
        # given
        ll = LinkedList2()
        # when
        reverse_linked_list(ll)
        # then
        self.assertIsNone(ll.head)
        self.assertIsNone(ll.tail)

    def test_reverse(self):
        # given
        ll = create_1234_linked_list()
        # when
        reverse_linked_list(ll)

        # then
        self.assertEqual(ll.head.value, 4)
        self.assertEqual(ll.tail.value, 1)
        self.assertEqual(ll.head.next.value, 3)
        self.assertEqual(ll.tail.prev.value, 2)

    def test_single_el(self):
        # given
        ll = LinkedList2()
        ll.add_in_tail(Node(1))
        # when
        reverse_linked_list(ll)
        # then
        self.assertEqual(ll.head.value, 1)
        self.assertEqual(ll.tail.value, 1)

    def test_reverse_two_el(self):
        # given
        ll = LinkedList2()
        ll.add_in_tail(Node(1))
        ll.add_in_tail(Node(2))
        # when
        reverse_linked_list(ll)
        # then
        self.assertEqual(ll.head.value, 2)
        self.assertEqual(ll.tail.value, 1)

    def test_reverse_three_el(self):
        # given
        ll = LinkedList2()
        ll.add_in_tail(Node(1))
        ll.add_in_tail(Node(2))
        ll.add_in_tail(Node(3))
        # when
        reverse_linked_list(ll)
        # then
        self.assertEqual(ll.head.value, 3)
        self.assertEqual(ll.tail.value, 1)
        self.assertEqual(ll.head.next.value, ll.tail.prev.value)

class TestHasCycle(unittest.TestCase):

    def test_empty_list(self):
        # given
        ll = LinkedList2()
        # when
        is_cycle = has_cycle(ll)
        # then
        self.assertFalse(is_cycle)

    def test_single_list_without(self):
        # given
        ll = LinkedList2()
        ll.add_in_tail(Node(1))
        # when
        is_cycle = has_cycle(ll)
        # then
        self.assertFalse(is_cycle)

    def test_single_list_with(self):
        # given
        ll = LinkedList2()
        ll.add_in_tail(Node(1))
        ll.head.next = ll.head
        # when
        is_cycle = has_cycle(ll)
        # then
        self.assertTrue(is_cycle)

    def test_double_list_without(self):
        # given
        ll = LinkedList2()
        ll.add_in_tail(Node(1))
        ll.add_in_tail(Node(2))
        # when
        is_cycle = has_cycle(ll)
        # then
        self.assertFalse(is_cycle)

    def test_double_list_with(self):
        # given
        ll = LinkedList2()
        ll.add_in_tail(Node(1))
        ll.add_in_tail(Node(2))
        ll.tail.next = ll.head
        # when
        is_cycle = has_cycle(ll)
        # then
        self.assertTrue(is_cycle)

    def test_many_el_without(self):
        # given
        ll = create_1234_linked_list()
        # when
        is_cycle = has_cycle(ll)
        # then
        self.assertFalse(is_cycle)

    def test_many_el_with(self):
        # given
        ll = create_1234_linked_list()
        ll.tail.next = ll.head.next
        # when
        is_cycle = has_cycle(ll)
        # then
        self.assertTrue(is_cycle)

    def test_many_el_with_full(self):
        # given
        ll = create_1234_linked_list()
        ll.tail.next = ll.head
        # when
        is_cycle = has_cycle(ll)
        # then
        self.assertTrue(is_cycle)

class TestSortList(unittest.TestCase):

    def test_empty_list(self):
        # given
        ll = LinkedList2()
        # when
        sort_list(ll)
        # then
        self.assertEqual(ll.head, None)
        self.assertEqual(ll.tail, None)

    def test_single_el(self):
        # given
        ll = LinkedList2()
        ll.add_in_tail(Node(1))
        # when
        sort_list(ll)
        # then
        self.assertEqual(ll.head.value, 1)
        self.assertEqual(ll.tail.value, 1)

    def test_two_els(self):
        # given
        ll = LinkedList2()
        ll.add_in_tail(Node(2))
        ll.add_in_tail(Node(1))
        # when
        sort_list(ll)
        # then
        self.assertEqual(ll.head.value, 1)
        self.assertEqual(ll.tail.value, 2)

    def test_three_els(self):
        # given
        ll = LinkedList2()
        ll.add_in_tail(Node(2))
        ll.add_in_tail(Node(1))
        ll.add_in_tail(Node(3))
        # when
        sort_list(ll)
        # then
        self.assertEqual(ll.head.value, 1)
        self.assertEqual(ll.head.next.value, 2)
        self.assertEqual(ll.tail.value, 3)
        self.assertEqual(ll.tail.prev.value, 2)

    def test_many_els(self):
        # given
        ll = create_shuffled_linked_list()
        # when
        sort_list(ll)
        # then
        self.assertEqual(ll.head.value, 1)
        self.assertEqual(ll.head.next.value, 2)
        self.assertEqual(ll.head.next.next.value, 3)
        self.assertEqual(ll.head.next.next.next.value, 4)
        self.assertEqual(ll.tail.value, 5)

    def test_duplicated_els(self):
        # given
        ll = create_duplicated_linked_list()
        # when
        sort_list(ll)
        # then
        self.assertEqual(ll.head.value, 1)
        self.assertEqual(ll.tail.value, 7)

class TestSortAndMerge(unittest.TestCase):

    def test_empty_lists(self):
        # given
        ll1 = LinkedList2()
        ll2 = LinkedList2()
        # when
        merged = sort_and_merge_list(ll1, ll2)
        # then
        self.assertEqual(merged.head, None)
        self.assertEqual(merged.tail, None)

    def test_single_and_empty_lists(self):
        # given
        ll1 = LinkedList2()
        ll1.add_in_head(Node(1))
        ll2 = LinkedList2()
        # when
        merged = sort_and_merge_list(ll1, ll2)
        # then
        self.assertEqual(merged.head.value, 1)
        self.assertEqual(merged.tail.value, 1)

    def test_empty_and_single_lists(self):
        # given
        ll1 = LinkedList2()
        ll2 = LinkedList2()
        ll2.add_in_head(Node(1))
        # when
        merged = sort_and_merge_list(ll1, ll2)
        # then
        self.assertEqual(merged.head.value, 1)
        self.assertEqual(merged.tail.value, 1)

    def test_single_lists(self):
        # given
        ll1 = LinkedList2()
        ll1.add_in_head(Node(2))
        ll2 = LinkedList2()
        ll2.add_in_head(Node(1))
        # when
        merged = sort_and_merge_list(ll1, ll2)
        # then
        self.assertEqual(merged.head.value, 1)
        self.assertEqual(merged.head.prev, None)
        self.assertEqual(merged.tail.value, 2)
        self.assertEqual(merged.tail.next, None)

    def test_single_two_lists(self):
        # given
        ll1 = LinkedList2()
        ll1.add_in_head(Node(2))
        ll2 = LinkedList2()
        ll2.add_in_head(Node(1))
        ll2.add_in_head(Node(6))
        # when
        merged = sort_and_merge_list(ll1, ll2)
        # then
        self.assertEqual(merged.head.value, 1)
        self.assertEqual(merged.head.prev, None)
        self.assertEqual(merged.head.next.value, 2)
        self.assertEqual(merged.tail.value, 6)
        self.assertEqual(merged.tail.next, None)

    def test_single_many_lists(self):
        # given
        ll1 = LinkedList2()
        ll1.add_in_head(Node(8))
        ll2 = create_shuffled_linked_list()
        # when
        merged = sort_and_merge_list(ll1, ll2)
        # then
        self.assertEqual(merged.head.value, 1)
        self.assertEqual(merged.head.prev, None)
        self.assertEqual(merged.tail.value, 8)
        self.assertEqual(merged.tail.next, None)

    def test_many_els(self):
        # given
        ll1 = create_1234_linked_list()
        ll2 = create_shuffled_linked_list()
        # when
        merged = sort_and_merge_list(ll1, ll2)
        # then
        self.assertEqual(merged.head.value, 1)
        self.assertEqual(merged.head.prev, None)
        self.assertEqual(merged.tail.value, 5)
        self.assertEqual(merged.tail.next, None)
        self.assertEqual(merged.len(), 9)

    def test_many_duplicated_els(self):
        # given
        ll1 = create_duplicated_linked_list()
        ll2 = create_shuffled_linked_list()
        # when
        merged = sort_and_merge_list(ll1, ll2)
        # then
        self.assertEqual(merged.head.value, 1)
        self.assertEqual(merged.head.prev, None)
        self.assertEqual(merged.tail.value, 7)
        self.assertEqual(merged.tail.next, None)
        self.assertEqual(merged.len(), ll2.len() + ll1.len())


def create_head_linked_list():
    node1 = Node(1)
    node2 = Node(1)
    node3 = Node(1)

    list = LinkedList2()
    list.add_in_tail(node1)
    list.add_in_tail(node2)
    list.add_in_tail(node3)

    return list

def create_pairs_linked_list():
    node1 = Node(1)
    node2 = Node(1)
    node3 = Node(2)
    node4 = Node(2)
    node5 = Node(3)
    node6 = Node(3)

    list = LinkedList2()
    list.add_in_tail(node1)
    list.add_in_tail(node2)
    list.add_in_tail(node3)
    list.add_in_tail(node4)
    list.add_in_tail(node5)
    list.add_in_tail(node6)

    return list

def create_duplicated_linked_list():
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(7)
    node4 = Node(1)
    node5 = Node(5)
    node6 = Node(6)
    node7 = Node(7)
    node8 = Node(5)


    list = LinkedList2()
    list.add_in_tail(node1)
    list.add_in_tail(node2)
    list.add_in_tail(node3)
    list.add_in_tail(node4)
    list.add_in_tail(node5)
    list.add_in_tail(node6)
    list.add_in_tail(node7)
    list.add_in_tail(node8)

    return list


def create_1234_linked_list():
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)

    list = LinkedList2()
    list.add_in_tail(node1)
    list.add_in_tail(node2)
    list.add_in_tail(node3)
    list.add_in_tail(node4)
    return list

def create_shuffled_linked_list():
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)

    list = LinkedList2()
    list.add_in_tail(node2)
    list.add_in_tail(node1)
    list.add_in_tail(node5)
    list.add_in_tail(node4)
    list.add_in_tail(node3)
    return list