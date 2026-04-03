# Implementation of N - Queeen problem 
# Approach: BackTracking all possible combinations of queens non-attacking position 
# Optimized apporach: Using set to track 

class Solution:
    def nQueen(self, n):
        results = []
        # Edge conditon
        if (n == 0):
            return results
        
        # Update queen's positon in column, left_diagonal and right_diagonal 
        column = set()
        l_diag = set() # (row - column)
        r_diag = set() # (row + column)

        self.solve_queens(0, n, [], column, l_diag, r_diag, results)
        return results
    
    def is_valid(self, row, col, column, l_diag, r_diag):

        # Check: Queen not in previous row 
        # check: Queen not present in left and right diagonal 
        if (col in column or (row - col) in l_diag or (row + col) in r_diag):
            return False
        
        # No queen is present in previous row and diagonals
        return True 

    def solve_queens(self, row, n, comb, column, l_diag, r_diag, results):

        # Base Conditon: 
        if (row == n):
            results.append(comb[:])
            return

        # Number of rows 
        # Each row has n choices 
        for col in range(0, n):
            # Controlled Recursion 
            if (self.is_valid(row, col, column, l_diag, r_diag)):
                # Add queen in this row and track position and comb position 
                column.add(col)
                l_diag.add(row - col)
                r_diag.add(row + col)

                comb.append(col + 1)

                # Recursive call to next row 
                self.solve_queens(row + 1, n, comb, column, l_diag, r_diag, results)

                # BackTrack, unselect board and comb position 
                column.remove(col)
                l_diag.remove(row - col)
                r_diag.remove(row + col)

                comb.pop()



sol = Solution()
n = 9
print(sol.nQueen(n))