# Implementation of largest number in k swaps 
class Solution:
    
    #Function to find the largest number after k swaps.
    def findMaximumNum(self, s, k):
        #code here
        
        # Solving problem with backTracking approach 
        results = []
        digit = list(s)
        self.get_combinations(digit, 0, k, results)
        print(results)
        return max(results)
    
    def get_combinations(self, d: list[str], start: int, k: int, results: list[str]):
        
        # Base condition: 
        if (start == len(d) - 1 or k == 0):
            results.append("".join(d))
            return 
        
        max_value = max(d[start:])
        if (d[start] == max_value):
            # k remains same but start will move forward
            self.get_combinations(d, start + 1, k, results)

        else:     
        # Number of choices 
            for i in range(start, len(d)):
                # Controlled Recursion:
                # Get maximum number and avoid swapping to smaller digits
                if (d[i] == max_value):
                    # Swap the position 
                    d[start], d[i] = d[i], d[start]
                    
                    # Recursive call and reduce number of swap value 
                    self.get_combinations(d, start + 1, k - 1, results)
                    
                    # Backtrack: Get original position of digits
                    d[start], d[i] = d[i], d[start] 
        

sol = Solution()
s = "3488"
print(sol.findMaximumNum(s, 2))