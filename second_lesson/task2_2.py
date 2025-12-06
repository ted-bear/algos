import unittest

from second_lesson.task2 import LinkedList2, Node

def reverse_linked_list(linked_list):
    """
    Time complexity: O(n)
    Memory complexity: O(1)

    Рефлексия: много раз делал переворот односвязного списка,
    но переворт двусвязног попадался всего один раз, и как это всегда бывает
    сначала в голове все выглядело сложно, но когда руками нарисовал все
    переходы ссылок у узлов, увидел, что это задача с приятным подвохом, особенно
    учитывая встроенную возможность swap'а элементов в питоне. Интересная задача
    для того, чтобы посмотреть как быстро щелкает в голове
    """
    cur = linked_list.head

    while cur is not None:
        cur.prev, cur.next = cur.next, cur.prev
        cur = cur.prev

    linked_list.head, linked_list.tail = linked_list.tail, linked_list.head


def has_cycle(linked_list):
    """
    Time complexity: O(n)
    Memory complexity: O(1)

    Рефлексия: Интересная задача на концепцию быстрого и медленного
    указателей, без знания этой идеи как будто невозможно додуматься
    до решения, решал еще более зубодробящую задачу, где нужно найти
    начало этого цикла и там уже совсем неочевидно почему повторный
    запуск двух указателей приводит нас в точку начала
    """
    slow = linked_list.head
    fast = linked_list.head

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

        if slow is fast:
            return True

    return False

def sort_list(linked_list):
    """
    Time complexity: O(n*log(n))
    Memory complexity: O(1)

    Рефлексия: Как приятно пользоваться встроенными структурами
    для сортировки, всегда в исходниках Java пугали запутанные
    алгоритмы сортировки и никогда не понимал зачем писать их
    самому, но наверное я просто чего то не знаю...
    """
    if linked_list.len() == 0 or linked_list.len() == 1:
        return

    tmp_list = []

    cur = linked_list.head

    while cur is not None:
        tmp_list.append(cur)
        cur = cur.next

    tmp_list.sort(key=lambda node: node.value)

    linked_list.head = tmp_list[0]
    linked_list.tail = tmp_list[-1]

    for i in range(len(tmp_list)):
        if i == 0:
            tmp_list[i].prev = None
            tmp_list[i].next = tmp_list[i + 1]
        elif i == len(tmp_list) - 1:
            tmp_list[i].prev = tmp_list[i - 1]
            tmp_list[i].next = None
        else:
            tmp_list[i].prev = tmp_list[i - 1]
            tmp_list[i].next = tmp_list[i + 1]


def sort_and_merge_list(ll1, ll2):
    """
    Time complexity: O(n*log(n) + n)
    Memory complexity: O(1)

    Рефлексия:
    """
    sort_list(ll1)
    sort_list(ll2)

    if ll1.len() == 0:
        return ll2

    if ll2.len() == 0:
        return ll1

    merged = LinkedList2()
    first_ptr = ll1.head
    second_ptr = ll2.head

    if first_ptr.value < second_ptr.value:
        merged.head = first_ptr
        first_ptr = first_ptr.next
    else:
        merged.head = second_ptr
        second_ptr = second_ptr.next

    merged.size += 1
    cur = merged.head

    while first_ptr is not None and second_ptr is not None:
        merged.size += 1
        if first_ptr.value < second_ptr.value:
            cur.next = first_ptr
            cur.next.prev = cur
            cur = cur.next
            first_ptr = first_ptr.next
        else:
            cur.next = second_ptr
            cur.next.prev = cur
            cur = cur.next
            second_ptr = second_ptr.next

    while first_ptr is not None:
        if first_ptr.next is None:
            merged.tail = first_ptr
        cur.next = first_ptr
        cur.next.prev = cur
        cur = cur.next
        first_ptr = first_ptr.next
        merged.size += 1

    while second_ptr is not None:
        if second_ptr.next is None:
            merged.tail = second_ptr
        cur.next = second_ptr
        cur.next.prev = cur
        cur = cur.next
        second_ptr = second_ptr.next
        merged.size += 1

    return merged