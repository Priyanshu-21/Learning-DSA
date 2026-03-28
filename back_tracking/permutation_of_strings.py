# Permutation of string: Approach using BackTracking = Recursion + Reference 

class Permutation():
    def permutation_strings(self, s1: str, s2: str):

        # Approach: 
        # Backtracking: Controlled Recursion (duplicate elements) + Refrences (swaping elements in-place)
        results = []
        s = list(s1) # convert to list  
        self.get_permutations(s, 0, results)

        print(results)
        # Results contains permuations of string "s1", now we need to check if sub-string present 
        for ele in results:
            if (ele in s2):
                return True
        
        # No sub-string present 
        return False
    
    def get_permutations(self, s1: list[str], start: int, results: list[str]):

        # Base Condition: 
        if (start == len(s1) - 1):
            results.append("".join(s1)) # list -> string of ele
            return 
        
        unordered_set = set()
        # Number of choices 
        for i in range(start, len(s1)):
            # Controlled Recursion: To avoid recursive call's to duplicate element
            if not(s1[i] in unordered_set):
                unordered_set.add(s1[i])

                # Changes in variable, change in order (reference)
                s1[start], s1[i] = s1[i], s1[start]

                # Recursive call 
                self.get_permutations(s1, start + 1, results)

                # BackTrack: Revert original combination of elements 
                s1[start], s1[i] = s1[i], s1[start]
        


sol = Permutation()
s1 = "dinitrophenylhydrazine"
s2 = "acetylphenylhydrazine"

print(sol.permutation_strings(s1, s2))

# This is also not an optimal approach, sliding windows + frequency count

