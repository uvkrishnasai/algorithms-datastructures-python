class Solution:

    def solve(self, node, partition):
        befStart = befEnd = aftStart = aftEnd = None

        while node:
            #print_node(befStart)
            #print_node(aftStart)
            next = node.next
            node.next = None

            if node.val < partition:
                if not befStart:
                    befStart = node
                    befEnd = befStart
                else:
                    befEnd.next = node
                    befEnd = befEnd.next

            else:
                if not aftStart:
                    aftStart = node
                    aftEnd = aftStart
                else:
                    aftEnd.next = node
                    aftEnd = aftEnd.next

            node = next

        if not befStart:
            return aftStart

        befEnd.next = aftStart
        return befStart


class Node:

    def __init__(self, val):
        self.val = val
        self.next = None


def print_node(node):
    while node:
        print(node.val, sep=" | ", end="")
        node = node.next
    print()


input = Node(3)
input.next = Node(5)
input.next.next = Node(8)
input.next.next.next = Node(5)
input.next.next.next.next = Node(10)
input.next.next.next.next.next = Node(2)
input.next.next.next.next.next.next = Node(1)
print_node(input)

soln = Solution()
output = soln.solve(input, 5)
print_node(output)
