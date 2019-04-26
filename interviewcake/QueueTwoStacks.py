class QueueTwoStacks():

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, item):
        assert item

        while self.stack2:
            self.stack1.append(self.stack2.pop())

        self.stack1.append(item)

    def dequeue(self):
        if self.stack2:
            return self.stack2.pop()

        while self.stack1:
            self.stack2.append(self.stack1.pop())

        assert self.stack2

        return self.stack2.pop()


class Test:

    def test_basic_queue_operations(self):
        queue = QueueTwoStacks()

        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)

        actual = queue.dequeue()
        expected = 1
        print("actual: {}, expected:{}".format(actual, expected))
        assert(actual == expected)

        actual = queue.dequeue()
        expected = 2
        print("actual: {}, expected:{}".format(actual, expected))
        assert(actual == expected)

        queue.enqueue(4)

        actual = queue.dequeue()
        expected = 3
        print("actual: {}, expected:{}".format(actual, expected))
        assert(actual == expected)

        actual = queue.dequeue()
        expected = 4
        print("actual: {}, expected:{}".format(actual, expected))
        assert(actual == expected)

    def test_error_when_dequeue_from_new_queue(self):
        try:
            queue = QueueTwoStacks()
            queue.dequeue()
        except AssertionError:
            print("Assertion Error!")

    def test_error_when_dequeue_from_empty_queue(self):
        queue = QueueTwoStacks()

        queue.enqueue(1)
        queue.enqueue(2)

        actual = queue.dequeue()
        expected = 1
        print("actual: {}, expected:{}".format(actual, expected))
        assert(actual == expected)

        actual = queue.dequeue()
        expected = 2
        print("actual: {}, expected:{}".format(actual, expected))
        assert(actual == expected)

        try:
            queue.dequeue()
        except AssertionError:
            print("Assertion Error!")


test = Test()
test.test_basic_queue_operations()
test.test_error_when_dequeue_from_new_queue()
test.test_error_when_dequeue_from_empty_queue()
