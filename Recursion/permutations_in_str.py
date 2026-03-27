# Permutation in strings: Recursive approach 

class Permutations():
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Calculate all permutations for string "s1"
        results = []
        self.permute(s1, "", results)

        # results list contains all string "s1" permutations 
        # Check if any permutation matches for string "s2"
        for permute in results:
            if (permute in s2):
                return True

        # No match found for permute of s1 with s2
        return False
    
    def permute(self, s1: str, output: str, results: list[str]):

        # Base condition: 
        if (len(s1) == 0):
            results.append(output)
            return 
        # Set to not call duplicate element recursive call 
        unordered_set = set()
        # Number of choices = variable size 
        for choice in range(0, len(s1)):
            if not(s1[choice] in unordered_set):
                # Append string values to remove taken index character
                new_str = s1[ :choice] + s1[choice + 1: ]
                # Add choice element in output 
                new_out = output + s1[choice]
                # Add item in set 
                unordered_set.add(s1[choice])

                # Recursive call 
                self.permute(new_str, new_out, results)



sol = Permutations()
s1 = "dinitrophenylhydrazine"
s2 = "acetylphenylhydrazine"

print(sol.checkInclusion(s1, s2))

