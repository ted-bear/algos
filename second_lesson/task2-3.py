from second_lesson.task2 import LinkedList2, Node
import unittest

if __name__ == '__main__':
    unittest.main()
    print('Everything passed')

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
        ll = create_linked_list()
        # when
        node = ll.find(2)
        # then
        self.assertIsNotNone(node)
        self.assertEqual(2, node.value)

    def test_many_el_not_found(self):
        # given
        ll = create_linked_list()
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
        linked_list = create_linked_list()
        # when
        linked_list.delete(1)
        # then
        self.assertEqual(linked_list.head.value, 2)
        self.assertEqual(linked_list.head.next.value, 3)
        self.assertEqual(linked_list.tail.value, 4)

    def test_delete_tail_el(self):
        # given
        linked_list = create_linked_list()
        # when
        linked_list.delete(4)
        # then
        self.assertEqual(linked_list.head.value, 1)
        self.assertEqual(linked_list.head.next.value, 2)
        self.assertEqual(linked_list.tail.value, 3)

    def test_delete_middle_el(self):
        # given
        linked_list = create_linked_list()
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

        # when
        linked_list.insert(None, node1)
        linked_list.insert(node1, node2)

        # then
        self.assertEqual(2, linked_list.len())
        self.assertEqual(1, linked_list.head.value)
        self.assertEqual(2, linked_list.tail.value)

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
        ll = create_linked_list()
        # when
        ll.add_in_head(Node(3))
        # then
        self.assertEqual(5, ll.len())
        self.assertEqual(3, ll.head.value)
        self.assertEqual(4, ll.tail.value)

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


def create_linked_list():
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