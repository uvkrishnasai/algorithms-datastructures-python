class LinkedListNode:

    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def get_values(self):
        node = self
        values = []
        while node is not None:
            values.append(node.value)
            node = node.next
        return values


def delete_node(node_to_delete):
    assert node_to_delete
    if node_to_delete.next:
        node_to_delete.value = node_to_delete.next.value
        node_to_delete.next = node_to_delete.next.next
    else:
        node_to_delete = None


class Test:

    def __init__(self):
        self.fourth = LinkedListNode(4)
        self.third = LinkedListNode(3, self.fourth)
        self.second = LinkedListNode(2, self.third)
        self.first = LinkedListNode(1, self.second)
        pass

    def set_up(self):
        self.fourth = LinkedListNode(4)
        self.third = LinkedListNode(3, self.fourth)
        self.second = LinkedListNode(2, self.third)
        self.first = LinkedListNode(1, self.second)

    def test_node_at_beginning(self):
        self.set_up()
        delete_node(self.first)
        actual = self.first.get_values()
        expected = [2, 3, 4]
        assert(actual == expected)

    def test_node_in_middle(self):
        self.set_up()
        delete_node(self.second)
        actual = self.first.get_values()
        expected = [1, 3, 4]
        assert(actual == expected)

    def test_node_at_end(self):
        self.set_up()
        try:
            delete_node(self.fourth)
        except AssertionError:
            print("Assertion Error!")

    def test_one_node_in_list(self):
        try:
            unique = LinkedListNode(1)
            delete_node(unique)
        except AssertionError:
            print("Assertion Error!")


test = Test()
test.test_node_at_beginning()
test.test_node_in_middle()
test.test_node_at_end()
test.test_one_node_in_list()
