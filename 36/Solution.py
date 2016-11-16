class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        rcDist = [[{},{},{}],[{},{},{}],[{},{},{}]]
        for i in range(0,9):
            rowDist = {}
            columnDist = {}
            for j in range(0,9):
                if board[i][j] == '.':
                    pass
                elif board[i][j] in rowDist:
                    return False
                else:
                    rowDist[board[i][j]] = 1

                if board[j][i] == '.':
                    pass
                elif board[j][i] in columnDist:
                    return False
                else:
                    columnDist[board[j][i]] = 1

                if board[i][j] == '.':
                    pass
                elif board[i][j] in rcDist[i/3][j/3]:
                    return False
                else:
                    rcDist[i/3][j/3][board[i][j]] = 1

        return True

solution = Solution()
print(solution.isValidSudoku(["..4...63.",".........","5......9.","...56....","4.3.....1","...7.....","...5.....",".........","........."]))
