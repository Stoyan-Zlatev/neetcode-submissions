class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        for row in range(9):
            for col in range(9):
                symbol = board[row][col]
                if symbol == ".":
                    continue
                if symbol in rows[row] or symbol in cols[col] or symbol in squares[(row//3)*3+col//3]:
                    return False
                rows[row].add(symbol)
                cols[col].add(symbol)
                squares[(row//3)*3+col//3].add(symbol)

        return True