class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        l, r = 0, (rows * cols)-1
        while l <= r:
            mid = l - (l - r) // 2
            curr_row, curr_col = mid // cols, mid % cols
            if matrix[curr_row][curr_col] == target:
                return True
            elif matrix[curr_row][curr_col] > target:
                r -= 1
            else:
                l += 1

        return False