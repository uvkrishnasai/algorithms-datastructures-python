class Solution:

    def solve(self, matrix):
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return [[]]

        n = len(matrix)
        for i in range(0, n//2):
            first, last = i, n-i-1
            for j in range(first, last):
                offset = j-first
                print(first, last, offset, last-offset)

                temp = matrix[first][j]

                # left -> top
                matrix[first][j] = matrix[last-offset][first]

                # bottom -> left
                matrix[last-offset][first] = matrix[last][last-offset]

                # right -> bottom
                matrix[last][last - offset] = matrix[j][last]

                # top -> right
                matrix[j][last] = temp

                #print(matrix)

        print(matrix)


table = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

#[
#    [7, 4, 1],
#    [8, 5, 2],
#    [9, 6, 3]
#]

soln = Solution()
soln.solve(table)