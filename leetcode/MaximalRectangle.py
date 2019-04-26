class Solution:

    def maximalRectangle(self, matrix):

        if len(matrix) == 0:
            return 0

        if len(matrix) == 1 and matrix[0][0] == 1:
            return 1

        result_matrix = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        max_area = [0]
        self.helper(0, 0, matrix, result_matrix, max_area)
        #print(result_matrix)
        return max_area[0]

    def helper(self, row, col, matrix, result_matrix, max_area):
        if row >= len(matrix) or col >= len(matrix[0]):
            return

        cell = matrix[row][col]
        curr_area = result_matrix[row][col]

        if cell == 1:
            result_matrix[row][col] = result_matrix[row][col]+1
            max_area[0] = max(curr_area, max_area[0])

        return self.helper(row, col+1, matrix, result_matrix, max_area) or self.helper(row+1, col, matrix, result_matrix, max_area)


input_ = [
    [0, 0, 1, 0, 0],
    [1, 1, 0, 1, 1],
    [1, 1, 1, 1, 1]
]
soln = Solution()
out = soln.maximalRectangle(input_)
print(out)