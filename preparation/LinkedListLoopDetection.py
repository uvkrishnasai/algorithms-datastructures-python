class Solution:

    def solve(self, head):
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                # collision detected
                break

        if not fast or not fast.next:
            # No Collision
            return None

        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next

        # fast == slow meeting point
        return fast


class Node:

    def __init__(self, val):
        self.val = val
        self.next = None

    def __str__(self):
        return self.val


def print_node(node, cnt):
    while node and cnt > 0:
        print(node.val, sep=" | ", end="")
        node = node.next
        cnt -= 1
    print()


node = Node('C')
node.next = Node('D')
node.next.next = Node('E')
node.next.next.next = node
input = Node('A')
input.next = Node('B')
input.next.next = node

input.next.next.next.next.next = node
print_node(input, 7)

soln = Solution()
output = soln.solve(input)
print(output)
