class Solution:
    def solve(self, expression):

        def isMatchingPair(char1, char2):
            if char1 == '(' and char2 == ')':
                return True
            if char1 == '{' and char2 == '}':
                return True
            if char1 == '[' and char2 == ']':
                return True
            return False

        def isBalanced(exp):
            stack = []
            for char in exp:
                if char in ['{', '(', '[']:
                    stack.append(char)

                if char in ['}', ')', ']']:
                    if not stack:
                        return False
                    if not isMatchingPair(stack.pop(), char):
                        return False
            if stack:
                return False
            return True

        chars = list(expression)
        #print(chars)
        return isBalanced(chars)


soln = Solution()
print(soln.solve("{()}[]"))
print(soln.solve("{()[]"))
print(soln.solve("{)}[]"))
