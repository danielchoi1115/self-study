# https://leetcode.com/problems/container-with-most-water/

from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        maxArea = 0
        while l < r:
            curMin = min(height[l], height[r])
            maxArea = max(maxArea, (r - l) * min(height[r], height[l]))
            
            while l < r and height[l] <= curMin:
                l = l + 1
            while l < r and height[r] <= curMin:
                r = r - 1

        return maxArea
        
height = [1,8,6,2,5,4,8,3,7]
s = Solution()

print(s.maxArea(height))