# Implementation of Letter combinations of phone number 
class Solution:
    def __init__(self):
        
        self.phone_dict = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }

    def letterCombinations(self, digits: str) -> list[str]:
        # BackTacking Approach 
        results = []

        self.solve_combination(digits, 0, [], results)

        return results
    
    
    def solve_combination(self, digits, start, comb, results):

        # Base condition 
        if (start == len(digits)):
            results.append("".join(comb))
            return 
        
        digit = digits[start]
        # Number of choices per digit 
        # Controlled Recursion: digit should not be 1 or 0 [2, 9]
        if (digits not in ["0", "1"]):
            for choice in self.phone_dict[digit]:
                # add choice in combination 
                comb.append(choice)

                # Recursive call 
                self.solve_combination(digits, start + 1, comb, results)

                # BackTrack 
                comb.pop()


sol = Solution()
print(sol.letterCombinations("37"))