# Recursive Implementation of Tower of Hanoi Problem 
class Tower:
    def tower_of_hanoi(self, n: int, fromm: int, aux: int, to: int) -> int:

        # Base Condition: 
        if (n == 0):
            return 0
        
        # Hypothesis Condition
        left = self.tower_of_hanoi(n - 1, fromm, aux, to)
        # Induction Condition
        move = 1
        right = self.tower_of_hanoi(n - 1, aux, fromm, to)
        print(f'move disk {n} from {fromm} pole to {to} pole')

        return left + move + right
    

# Condition: n <= 20 (because 2^n -1 will be the running time complexity of this approach)
# 2 ^ 64 - 1 ---> 550 Billion years

tw = Tower()
result = tw.tower_of_hanoi(3, 1, 2, 3)
print(result)
