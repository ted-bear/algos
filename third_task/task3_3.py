import unittest
from third_task.task3 import DynArray

if __name__ == "__main__":
    unittest.main()


class TestMove(unittest.TestCase):

    def test_move_start(self):
        array = DynArray()
        array.append(1)
        array.append(2)
        array.append(3)
        array.append(4)
        array.append(5)

        # when
        array.move_right_elements(0)

        # then
        self.assertEqual(1, array.array[0])
        self.assertEqual(1, array.array[1])
        self.assertEqual(2, array.array[2])
        self.assertEqual(3, array.array[3])
        self.assertEqual(4, array.array[4])
        self.assertEqual(5, array.array[5])

    def test_move_middle(self):
        array = DynArray()
        array.append(1)
        array.append(2)
        array.append(3)
        array.append(4)
        array.append(5)

        # when
        array.move_right_elements(2)

        # then
        self.assertEqual(3, array.array[2])
        self.assertEqual(3, array.array[3])
        self.assertEqual(4, array.array[4])
        self.assertEqual(5, array.array[5])

    def test_move_last(self):
        array = DynArray()
        array.append(1)
        array.append(2)
        array.append(3)
        array.append(4)
        array.append(5)

        # when
        array.move_right_elements(4)

        # then
        self.assertEqual(5, array.array[4])
        self.assertEqual(5, array.array[5])

    def test_move_after_last(self):
        array = DynArray()
        array.append(1)
        array.append(2)
        array.append(3)
        array.append(4)
        array.append(5)

        # when
        array.move_right_elements(5)

        # then
        self.assertEqual(5, array.array[4])

    def test_left_last(self):
        # given
        array = get_1234_array()
        # when
        array.move_left_elements(3)
        # then
        self.assertEqual(1, array.__getitem__(0))
        self.assertEqual(2, array.__getitem__(1))
        self.assertEqual(3, array.__getitem__(2))
        self.assertEqual(4, array.__getitem__(3))

    def test_left_first(self):
        # given
        array = get_1234_array()
        # when
        array.move_left_elements(0)
        # then
        self.assertEqual(2, array.__getitem__(0))
        self.assertEqual(3, array.__getitem__(1))
        self.assertEqual(4, array.__getitem__(2))
        self.assertEqual(4, array.__getitem__(3))

    def test_left_middle(self):
        # given
        array = get_1234_array()
        # when
        array.move_left_elements(2)
        # then
        self.assertEqual(1, array.__getitem__(0))
        self.assertEqual(2, array.__getitem__(1))
        self.assertEqual(4, array.__getitem__(2))
        self.assertEqual(4, array.__getitem__(3))

    def test_left(self):
        # given
        array = get_1234_array()
        # when
        array.move_left_elements(1)
        # then
        self.assertEqual(1, array.__getitem__(0))
        self.assertEqual(3, array.__getitem__(1))
        self.assertEqual(4, array.__getitem__(2))
        self.assertEqual(4, array.__getitem__(3))


class TestInsert(unittest.TestCase):

    def test_empty_array(self):
        # given
        arr = DynArray()
        # when
        arr.insert(0, 12)
        # then
        self.assertEqual(1, arr.count)
        self.assertEqual(16, arr.capacity)
        self.assertEqual(12, arr.__getitem__(0))

    def test_single_array(self):
        # given
        arr = DynArray()
        # when
        arr.append(1)
        arr.insert(0, 2)
        # then
        self.assertEqual(2, arr.count)
        self.assertEqual(16, arr.capacity)
        self.assertEqual(2, arr.__getitem__(0))
        self.assertEqual(1, arr.__getitem__(1))

    def test_insert_first(self):
        # given
        arr = get_1234_array()
        # when
        arr.insert(0, 10)
        # then
        self.assertEqual(5, arr.count)
        self.assertEqual(16, arr.capacity)
        self.assertEqual(10, arr.__getitem__(0))
        self.assertEqual(1, arr.__getitem__(1))
        self.assertEqual(2, arr.__getitem__(2))
        self.assertEqual(3, arr.__getitem__(3))
        self.assertEqual(4, arr.__getitem__(4))

    def test_middle(self):
        # given
        arr = get_1234_array()
        # when
        arr.insert(2, 10)
        # then
        self.assertEqual(5, arr.count)
        self.assertEqual(16, arr.capacity)
        self.assertEqual(1, arr.__getitem__(0))
        self.assertEqual(2, arr.__getitem__(1))
        self.assertEqual(10, arr.__getitem__(2))
        self.assertEqual(3, arr.__getitem__(3))
        self.assertEqual(4, arr.__getitem__(4))

    def test_before_last(self):
        # given
        arr = get_1234_array()
        # when
        arr.insert(3, 10)
        # then
        self.assertEqual(5, arr.count)
        self.assertEqual(16, arr.capacity)
        self.assertEqual(1, arr.__getitem__(0))
        self.assertEqual(2, arr.__getitem__(1))
        self.assertEqual(3, arr.__getitem__(2))
        self.assertEqual(10, arr.__getitem__(3))
        self.assertEqual(4, arr.__getitem__(4))

    def test_after_last(self):
        # given
        arr = get_1234_array()
        # when
        arr.insert(4, 10)
        # then
        self.assertEqual(5, arr.count)
        self.assertEqual(16, arr.capacity)
        self.assertEqual(1, arr.__getitem__(0))
        self.assertEqual(2, arr.__getitem__(1))
        self.assertEqual(3, arr.__getitem__(2))
        self.assertEqual(4, arr.__getitem__(3))
        self.assertEqual(10, arr.__getitem__(4))

    def test_throw(self):
        # given
        arr = get_1234_array()
        # when
        # then
        with self.assertRaises(IndexError):
            arr.insert(5, 12)

    def test_insert_with_resize(self):
        # given
        arr = get_full_array()
        # when
        arr.insert(16, 17)
        # then
        self.assertEqual(17, arr.count)
        self.assertEqual(32, arr.capacity)
        for i in range(0, 17):
            self.assertEqual(i + 1, arr.array[i])

    def test_insert_in_start_with_resize(self):
        # given
        arr = get_full_array()
        # when
        arr.insert(0, 17)
        # then
        self.assertEqual(17, arr.count)
        self.assertEqual(32, arr.capacity)
        self.assertEqual(17, arr.array[0])
        self.assertEqual(16, arr.array[16])
        for i in range(1, 17):
            self.assertEqual(i, arr.array[i])

    def test_insert_in_middle_with_resize(self):
        # given
        arr = get_full_array()
        # when
        arr.insert(5, 17)
        # then
        self.assertEqual(17, arr.count)
        self.assertEqual(32, arr.capacity)
        self.assertEqual(17, arr.array[5])
        for i in range(6, 17):
            self.assertEqual(i, arr.array[i])


class TestDelete(unittest.TestCase):

    def test_delete_last_without_resize(self):
        # given
        array = get_1234_array()
        # when
        array.delete(3)
        # then
        self.assertEqual(1, array.__getitem__(0))
        self.assertEqual(2, array.__getitem__(1))
        self.assertEqual(3, array.__getitem__(2))
        self.assertEqual(3, array.count)
        self.assertEqual(16, array.capacity)

    def test_delete_first_without_resize(self):
        # given
        array = get_1234_array()
        # when
        array.delete(0)
        # then
        self.assertEqual(2, array.__getitem__(0))
        self.assertEqual(3, array.__getitem__(1))
        self.assertEqual(4, array.__getitem__(2))
        self.assertEqual(3, array.count)
        self.assertEqual(16, array.capacity)

    def test_delete_middle_without_resize(self):
        # given
        array = get_1234_array()
        # when
        array.delete(1)
        # then
        self.assertEqual(1, array.__getitem__(0))
        self.assertEqual(3, array.__getitem__(1))
        self.assertEqual(4, array.__getitem__(2))
        self.assertEqual(3, array.count)
        self.assertEqual(16, array.capacity)

    def test_delete_first_with_resize(self):
        # given
        array = get_half_full_array()
        self.assertEqual(32, array.capacity)
        # when
        array.delete(0)
        array.delete(0)
        array.delete(0)
        array.delete(0)
        array.delete(0)
        array.delete(0)
        # then
        self.assertEqual(7, array.__getitem__(0))
        self.assertEqual(15, array.count)
        self.assertEqual(21, array.capacity)


class TestMulti(unittest.TestCase):

    def test_expand_and_squeeze(self):
        # step 1: get init array
        array = get_1234_array()
        self.assertEqual(4, array.count)
        self.assertEqual(16, array.capacity)

        # step 2: append elements
        for i in range(5, 17):
            array.insert(array.count, i)
        self.assertEqual(16, array.count)
        self.assertEqual(16, array.capacity)

        # step 3: append element and expand
        array.insert(array.count, 17)
        self.assertEqual(17, array.count)
        self.assertEqual(32, array.capacity)

        # step 4: remove two elements and squeeze array
        array.delete(array.count - 1)
        array.delete(array.count - 1)
        self.assertEqual(15, array.count)
        self.assertEqual(21, array.capacity)

        # step 5: remove all element except one
        for i in range(array.count - 1):
            array.delete(array.count - 1)
        self.assertEqual(1, array.count)
        self.assertEqual(1, array.__getitem__(0))
        self.assertEqual(21, array.capacity)

        # step 6: add elements
        for i in range(2, 22):
            array.append(i)
        self.assertEqual(1, array.__getitem__(0))
        self.assertEqual(21, array.__getitem__(array.count - 1))
        self.assertEqual(21, array.capacity)
        self.assertEqual(21, array.count)

        # step 7: add element and expand array
        array.append(22)
        self.assertEqual(1, array.__getitem__(0))
        self.assertEqual(22, array.__getitem__(array.count - 1))
        self.assertEqual(42, array.capacity)
        self.assertEqual(22, array.count)

        # step 8: fills array
        for i in range(23, 43):
            array.append(i)
        self.assertEqual(1, array.__getitem__(0))
        self.assertEqual(42, array.__getitem__(array.count - 1))
        self.assertEqual(42, array.capacity)
        self.assertEqual(42, array.count)

        # step 9: delete element for squeezing
        for i in range(22):
            array.delete(array.count - 1)
        self.assertEqual(1, array.__getitem__(0))
        self.assertEqual(20, array.__getitem__(array.count - 1))
        self.assertEqual(28, array.capacity)
        self.assertEqual(20, array.count)

def get_1234_array():
    arr = DynArray()
    arr.append(1)
    arr.append(2)
    arr.append(3)
    arr.append(4)
    return arr

def get_full_array():
    arr = DynArray()
    for i in range(1, 17):
        arr.append(i)
    return arr

def get_half_full_array():
    arr = DynArray()
    for i in range(1, 22):
        arr.append(i)
    return arr