class Solution:

    def largestRectangleArea(self, heights):
        stack = list()
        max_area = 0
        index = 0

        while index < len(heights):
            #print('stack: ', stack, ' , heights: ', heights, end=' , ')
            if (not stack) or (heights[stack[-1]] <= heights[index]):
                #print('append ', index)
                stack.append(index)
                index += 1

            else:
                top_of_stack = stack.pop()
                #print('pop', top_of_stack, end=' , ')

                prev_height = heights[top_of_stack]

                area = prev_height * ((index - stack[-1] - 1) if stack else index)
                #print('area: ', area, ' , index: ', index, end=' , ')
                max_area = max(area, max_area)
                #print('max_area: ', max_area)

        while stack:
            top_of_stack = stack.pop()
            area = (heights[top_of_stack] * ((index - stack[-1] - 1) if stack else index))
            max_area = max(max_area, area)

        return max_area


soln = Solution()
out = soln.largestRectangleArea([6, 2, 5, 4, 5, 1, 6])
print(out)
