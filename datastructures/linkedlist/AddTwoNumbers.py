"""
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order and each of their nodes contain a single digit.
Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def __init__(self):
        self.head = None

    def add_two_numbers(self, l1, l2):

        over_flow, prev, temp = 0, None, None

        while True:

            if l1 or l2 or over_flow != 0:

                l1 = ListNode(0) if not l1 else l1
                l2 = ListNode(0) if not l2 else l2

                total = sum([l1.val, l2.val, over_flow])

                temp = ListNode(total % 10)
                if not self.head:
                    self.head = temp
                else:
                    prev.next = temp

                prev = temp

                over_flow = total // 10

                l1 = l1.next
                l2 = l2.next

            else:
                break

        if not self.head:
            self.head = ListNode(0)

        return self.head

    def print_node(self):
        temp = self.head
        while temp:
            print(temp.val)
            temp = temp.next
        print("-------------")
