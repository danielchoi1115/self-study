# https://leetcode.com/problems/binary-search
from typing import List
from bisect import bisect_left


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)
        while l < r:
            m = (l+r)//2
            if nums[m] == target:
                return m
            elif nums[m] > target:
                r = m
            else:
                l = m+1
        return -1

# Solution 2
# class Solution:
#     def search(self, nums: List[int], target: int) -> int:
#         idx = bisect_left(nums, target)
#         return idx if target == nums[idx] else -1


nums = [-1, 0, 3, 5, 9, 12]
target = 9

s = Solution()
ans = s.search(nums, target)
print(ans)
