# Implementation of Permutation with different variation problem 
 
class Permutation:
    # 1. Permutation with Spaces
    def letter_spaces(self, s: str):

        output = str(s[0])
        s = s[1:]
        result = []
        
        return self.solve(s, output, result)
    
    def solve(self, s: str, output: str, result: list[str]):
        # Base condition: 
        if (len(s) == 0):
            result.append(output)
            return 
        
        # Hypothesis + Induction 
        element = s[0]
        remain = s[1:]

        # Decision: To add space in between characters or not 
        # Left Part: Not add spaces
        left_out = output + element
        self.solve(remain, left_out, result)
        
        # Rigth Part: Add spaces
        right_out = output + " " + element
        self.solve(remain, right_out, result)

        return result
    
    # 2. Permutation with change change
    def case_change(self, s: str):
        output = ""
        result = []

        return self.solve_case_change(s, output, result)
    
    def solve_case_change(self, s: str, output: str, result: list[str]):
        # Base Condition:
        if (len(s) == 0):
            result.append(output)
            return 
        
        # Induction + Hypothesis
        element = s[0]
        remain = s[1:]

        # checking if element is numeric
        # TODO: need to work on numeric condition
        if (element.isnumeric()):
            # Move to next character 
            output = output + element
            if (len(remain) > 1):
                element = remain[0]
                remain = remain[1]

        # Now, characters are not numberic 
        # Left Part: Choice to make character lowercase 
        left_out = output + element.lower()
        self.solve_case_change(remain, left_out, result)

        # Right Part: Choice to make character uppercase
        right_out = output + element.upper()
        self.solve_case_change(remain, right_out, result)

        return result






sol = Permutation()
print(sol.letter_spaces("ABC"))

print(sol.case_change("a1b2"))


