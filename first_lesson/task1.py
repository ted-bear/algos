class Node:

    def __init__(self, v):
        self.value = v
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
        else:
            self.tail.next = item
        self.tail = item
        self._size += 1

    def print_all_nodes(self):
        node = self.head
        while node is not None:
            print(node.value)
            node = node.next

    def find(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    def find_all(self, val):
        """
        Exercise 1.4. Find all elements with the val
        Time complexity: O(N)
        Memory complexity: O(N)
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
        Exercise 1.1 and 1.2. Delete one el and all els
        # Time complexity: O(n)
        # Memory complexity: O(1)
        """
        prev_node = None
        cur_node = self.head
        while cur_node is not None:
            if cur_node.value == val:
                self._size -= 1
                if cur_node == self.head and cur_node == self.tail:
                    self.head = None
                    self.tail = None
                elif cur_node == self.head:
                    self.head = self.head.next
                elif cur_node == self.tail:
                    prev_node.next = None
                    self.tail = prev_node
                else:
                    prev_node.next = cur_node.next
                cur_node = cur_node.next
                if not all:
                    return
            else:
                prev_node = cur_node
                cur_node = cur_node.next


    def clean(self):
        """
        Exercise 1.3. Clean current list
        Time complexity: O(1)
        Memory complexity: O(1)
        """
        self.head = None
        self.tail = None
        self._size = 0

    def len(self):
        """
        Exercise 1.5. Method returns current length of the linked list
        Time complexity: O(1)
        Memory complexity: O(1)
        """
        return self._size

    def insert(self, afterNode, newNode):
        """
        Exercise 1.6. Inserts newNode after afterNode
        Time complexity: O(N)
        Memory complexity: O(1)
        """
        if afterNode is None:
            self._size += 1
            newNode.next = self.head
            self.head = newNode
            if self.tail is None:
                self.tail = newNode
            return

        cur = self.head
        while cur is not None:
            if cur == afterNode:
                self._size += 1
                newNode.next = cur.next
                cur.next = newNode
                if cur is self.tail:
                    self.tail = newNode
                return
            cur = cur.next