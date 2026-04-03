# Implementation of N - Queeen problem 
# Approach: BackTracking all possible combinations of queens non-attacking position 

class Solution:
    def nQueen(self, n):
        # Create a chess board with all positions as 0
        board = [[0 for _ in range(n)] for _ in range(n)]
        results = []

        self.solve_queens(board, 0, n, [], results)
        return results
    
    def is_valid(self, board, row, col):

        # Check: Queen not in previous row 
        for r in range(row):
            if (board[r][col] == 1):
                return False
        
        r, c = row, col 
        while (c >= 0 and r >= 0):
            if (board[r][c] == 1):
                return False
            
            r -= 1
            c -= 1

        r, c = row, col
        while (r >= 0 and c < len(board)):
            if (board[r][c] == 1):
                return False
            
            r -= 1
            c += 1
        
        # No queen is present in previous row and diagonals
        return True 

    def solve_queens(self, board, row, n, comb, results):

        # Base Conditon: 
        if (row == n):
            results.append(comb[:])
            return

        # Number of rows 
        # Each row has n choices 
        for col in range(0, n):
            # Controlled Recursion 
            if (self.is_valid(board, row, col)):
                # Add queen in this row and track board and comb position 
                board[row][col] = 1
                comb.append(col + 1)

                # Recursive call to next row 
                self.solve_queens(board, row + 1, n, comb, results)

                # BackTrack, unselect board and comb position 
                board[row][col] = 0
                comb.pop()



sol = Solution()
n = 9
print(sol.nQueen(n))