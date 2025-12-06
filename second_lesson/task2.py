from tarfile import tar_filter


class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None

class LinkedList2:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
            item.prev = None
            item.next = None
        else:
            self.tail.next = item
            item.prev = self.tail
        self.tail = item
        self.size += 1

    def find(self, val):
        """
        Time complexity: O(n)
        Memory complexity: O(n)

        :param val: value to find
        :return: node with value
        """
        node = self.head

        while node is not None:
            if node.value == val:
                return node
            node = node.next

        return node

    def find_all(self, val):
        """
        Time complexity: O(n)
        Memory complexity: O(n)

        :param val: value to find
        :return: list with nodes
        """
        nodes = []
        node = self.head

        while node is not None:
            if node.value == val:
                nodes.append(node)
            node = node.next

        return nodes

    def delete(self, val, all=False):
        """
        Time complexity: O(n)
        Memory complexity: O(1)

        :param val: value to delete
        :param all: delete all elements equals val
        """

        prev = None
        cur = self.head

        while cur is not None:
            if cur.value == val:
                self.size -= 1
                if cur == self.head and cur == self.tail:
                    self.head = None
                    self.tail = None
                elif cur == self.head:
                    self.head = self.head.next
                    self.head.prev = None
                elif cur == self.tail:
                    self.tail = prev
                    self.tail.next = None
                else:
                    cur.next.prev = prev
                    prev.next = cur.next
                cur = cur.next
                if not all:
                   break
            else:
                prev = cur
                cur = cur.next

    def clean(self):
        """
        Time complexity: O(1)
        Memory complexity: O(1)
        """
        self.head = None
        self.tail = None
        self.size = 0

    def len(self):
        """
        Time complexity: O(1)
        Memory complexity: O(1)

        :return: length of linked list
        """

        return self.size

    def insert(self, afterNode, newNode):
        """
        Time complexity: O(n)
        Memory complexity: O(1)
        """

        if afterNode is None:
            self.size += 1
            if self.head is None:
                self.head = newNode
                self.tail = newNode
            else:
                newNode.prev = self.tail
                self.tail.next = newNode
                self.tail = newNode
            return

        cur = self.head

        while cur is not None:
            if cur is afterNode:
                self.size += 1
                if cur is self.tail:
                    self.tail.next = newNode
                    newNode.prev = self.tail.prev
                    self.tail = newNode
                else:
                    newNode.prev = cur
                    newNode.next = cur.next
                    cur.next.prev = newNode
                    cur.next = newNode
                return
            cur = cur.next

    def add_in_head(self, newNode):
        """
        Time complexity: O(1)
        Memory complexity: O(1)
        """

        self.size += 1
        if self.head is None:
            self.head = newNode
            self.tail = newNode
            return

        newNode.next = self.head
        self.head.prev = newNode
        self.head = newNode