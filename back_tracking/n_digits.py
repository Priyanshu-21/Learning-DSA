# Implementation of n digits with increasing order (Combinations)

class Digit():
    def get_combinations(self, n: int): 
        # BackTracking approach
        results = [] # list to store the digits
        if (n == 1):
            # Edge Condition: 
            for i in range(0, 10):
                results.append(i)
            return results
        
        digits = list() # array to store digits in order, later need to convert to int
    
        self.solve_combinations(n, digits, results)
        return results
    
    def solve_combinations(self, n: int, digits: list[int], results: list[int]):

        # Base Condition: n == number of digits  
        if (n == 0):
            # Converting digits to numbers 
            number = 0
            for d in digits:
                number = number * 10 + d

            results.append(number)
            return

        # Number of choices = large (1 - 9)
        for choice in range(1, 10):
            # Controlled Recursion: rightmost element should be always greater than leftmost element
            if (len(digits) == 0 or digits[len(digits) - 1] < choice):
                # Append to digits list 
                digits.append(choice)

                # Recursive call:
                self.solve_combinations(n - 1, digits, results)
                
                # BackTrack remove from digits list
                digits.pop()


sol = Digit()
n = 8
print(sol.get_combinations(n))