class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        counts_row = collections.defaultdict(set)
        counts_col = collections.defaultdict(set)
        counts_cell = collections.defaultdict(set)

        for i in range(len(board)):
            for j in range(len(board[0])):

                if board[i][j] == ".":
                    continue

                if (board[i][j] in counts_row[i] or
                    board[i][j] in counts_col[j] or
                    board[i][j] in counts_cell[(i//3, j//3)]):
                    return False

                counts_row[i].add(board[i][j])
                counts_col[j].add(board[i][j])
                counts_cell[(i//3, j//3)].add(board[i][j])

        return True

