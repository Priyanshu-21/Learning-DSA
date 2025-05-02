# Leetcode Problem: - Container with most water 
class Solution:
    def maxArea(self, height: list[int]) -> int:
        # First Approach 
        first = 0
        last = len(height) - 1
        max = 0
        while (first <= last):
            currentMax = 0
            if (height[first] < height[last]):
                currentMax = (last - first) * min(height[first], height[last])
                first = first + 1
            elif (height[first] >= height[last]):
                currentMax = (last - first) * min(height[first], height[last])
                last = last - 1
            if (currentMax > max):
                max = currentMax
        return max
    
if __name__ == "__main__":
    res = Solution()
    height = [1,7,6,2,5,4,8,3,1]
    result = res.maxArea(height)
    print(result)
    