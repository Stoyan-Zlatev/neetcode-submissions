class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # rows and cols
        for i in range(9):
            row = set()
            col = set()
            for j in range(9):
                if not board[i][j] == "." and board[i][j] in row:
                    return False
                row.add(board[i][j])
                if not board[j][i] == "." and board[j][i] in col:
                    return False
                col.add(board[j][i])

        for i in range(3):
            # Rows
            for j in range(3):
                seen = set()
                for row in range(3):
                    for col in range(3):
                        if not board[row+3*i][col+3*j] == "." and board[row+3*i][col+3*j] in seen:
                            return False
                        seen.add(board[row+3*i][col+3*j])

        return True