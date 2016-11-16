class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        rowSet = [set([]) for i in range(9)]
        columnSet = [set([]) for i in range(9)]
        gridSet = [set([]) for i in range(9)]

        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue

                grid = (i/3)*3 + j/3

                if board[i][j]  in rowSet[i]:
                    return False

                if board[i][j] in columnSet[j]:
                    return False

                if board[i][j] in gridSet[grid]:
                    return False

                rowSet[i].add(board[i][j])
                columnSet[j].add(board[i][j])
                gridSet[grid].add(board[i][j])

        return True

solution = Solution()
print(solution.isValidSudoku(["..4...63.",".........","5......9.","...56....","4.3.....1","...7.....","...5.....",".........","........."]))
