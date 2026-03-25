class PowerSet:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        
        results = []
        self.solve(nums, [], results)

        return results
    
    def solve(self, nums: list[int], output: list[int], res: list[list[int]]):
        # Base Condition: 
        if (len(nums) == 0):
            res.append(output[:])
            return
        
        # Pick current element and skip it
        ele = nums[0]
        remain = nums[1:]
        # Left Part: Not taken element
        self.solve(remain, output, res)

        # Right Part: Taken element 
        self.solve(remain, output + [ele], res)


sol = PowerSet()
nums = [1, 2, 3]
result = sol.subsets(nums)
print(result)