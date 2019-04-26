class Stack:

    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.items:
            return None

        return self.items.pop()

    def peek(self):
        if not self.items:
            return None
        return self.items[-1]

    def print(self):
        print(self.items)


class MaxStack(Stack):

    def __init__(self):
        Stack.__init__(self)
        self.max_stack = Stack()
        pass

    def push(self, item):
        if not self.max_stack.peek() or item >= self.max_stack.peek():
            self.max_stack.push(item)
        Stack.push(self, item)

    def pop(self):
        val = Stack.pop(self)
        if self.max_stack.peek() == val:
            return  self.max_stack.pop()
        return val

    def get_max(self):
        return self.max_stack.peek()


class Test():

    def __init__(self):
        max_stack = MaxStack()

        max_stack.push(5)

        actual = max_stack.get_max()
        expected = 5
        assert(actual == expected)

        max_stack.push(4)
        max_stack.push(7)
        max_stack.push(7)
        max_stack.push(8)

        actual = max_stack.get_max()
        expected = 8
        assert(actual == expected)

        actual = max_stack.pop()
        expected = 8
        assert(actual == expected)

        actual = max_stack.get_max()
        expected = 7
        assert(actual == expected)

        actual = max_stack.pop()
        expected = 7
        assert(actual == expected)

        actual = max_stack.get_max()
        expected = 7
        assert(actual == expected)

        actual = max_stack.pop()
        expected = 7
        assert(actual == expected)

        actual = max_stack.get_max()
        expected = 5
        assert(actual == expected)

        actual = max_stack.pop()
        expected = 4
        assert(actual == expected)

        actual = max_stack.get_max()
        expected = 5
        assert(actual == expected)


test = Test()
