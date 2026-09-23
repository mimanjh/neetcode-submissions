class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # check if value exists in a specific row
        rows = len(matrix)

        l = 0
        r = rows - 1

        while l <= r:
            m = (l + r) // 2
            if target > matrix[m][-1]:
                l = m + 1
            elif target < matrix[m][0]:
                r = m - 1
            else: break

        # go through that row
        row = (l + r) // 2
        cols = len(matrix[0])

        l = 0
        r = cols - 1

        while l <= r:
            m = (l + r) // 2

            if target > matrix[row][m]:
                l = m + 1
            elif target < matrix[row][m]:
                r = m - 1
            else:
                return True

        return False
        