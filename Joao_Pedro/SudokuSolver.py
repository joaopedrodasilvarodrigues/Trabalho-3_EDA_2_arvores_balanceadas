class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """

        def is_valid(row, col, num):
            # Verifica a linha
            for j in range(9):
                if board[row][j] == num:
                    return False

            # Verifica a coluna
            for i in range(9):
                if board[i][col] == num:
                    return False

            # Verifica a subgrade 3x3
            start_row, start_col = 3 * (row // 3), 3 * (col // 3)
            for i in range(start_row, start_row + 3):
                for j in range(start_col, start_col + 3):
                    if board[i][j] == num:
                        return False

            return True

        def backtrack():
            for i in range(9):
                for j in range(9):
                    if board[i][j] == ".":  # célula vazia
                        for num in map(str, range(1, 10)):
                            if is_valid(i, j, num):
                                board[i][j] = num
                                if backtrack():
                                    return True
                                board[i][j] = "."  # desfaz a escolha
                        return False
            return True  # terminou sem vazios → solução encontrada

        backtrack()
