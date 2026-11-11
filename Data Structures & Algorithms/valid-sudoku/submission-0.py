class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # rows and cols
        for i in range(9):
            row = {}
            col = {}
            for j in range(9):
                if not board[i][j] == "." and board[i][j] in row:
                    return False
                row[board[i][j]] = True
                if not board[j][i] == "." and board[j][i] in col:
                    return False
                col[board[j][i]] = True

        for i in range(3):
            # Rows
            for j in range(3):
                seen = {}
                for row in range(3):
                    for col in range(3):
                        if not board[row+3*i][col+3*j] == "." and board[row+3*i][col+3*j] in seen:
                            return False
                        seen[board[row+3*i][col+3*j]] = True

        return True