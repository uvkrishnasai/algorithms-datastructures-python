class Solution:

    def solve(self, stack):
        stack2 = []
        while stack:
            val = stack.pop()
            while stack2 and stack2[-1] < val:
                stack.append(stack2.pop())
            stack2.append(val)

        while stack2:
            stack.append(stack2.pop())


input = [3, 5, 6, 2, 8, 1]
soln = Solution()
soln.solve(input)
print(input)
