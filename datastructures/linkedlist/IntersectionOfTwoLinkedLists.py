"""
Write a program to find the node at which the intersection of two singly linked lists begins.


For example, the following two linked lists:

A:          a1 → a2
                   ↘
                     c1 → c2 → c3
                   ↗
B:     b1 → b2 → b3
begin to intersect at node c1.


Notes:

If the two linked lists have no intersection at all, return null.
The linked lists must retain their original structure after the function returns.
You may assume there are no cycles anywhere in the entire linked structure.
Your code should preferably run in O(n) time and use only O(1) memory.
Credits:
Special thanks to @stellari for adding this problem and creating all test cases.
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def get_intersection_node(self, headA, headB):
        headA_size = self.size_of_node(headA)
        headB_size = self.size_of_node(headB)

        #print(headA_size)
        #print(headB_size)

        i = 0 if headA_size <= headB_size else headA_size - headB_size
        j = 0 if headB_size <= headA_size else headB_size - headA_size

        #print("i: {}".format(i))
        #print("j: {}".format(j))

        first, second = headA, headB
        for p in range(0, i):
            first = first.next
        for q in range(0, j):
            second = second.next

        while True:
            if not first:
                break
            if first == second:
                return first
            first = first.next
            second = second.next

        return None

    def size_of_node(self, node):
        size, temp = 0, node
        while temp:
            size += 1
            temp = temp.next
        return size
