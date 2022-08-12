# https://leetcode.com/problems/maximum-subarray/
# 53. Maximum Subarray

from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        count = len(nums)
        if count == 1:
            return nums[0]
        # dp = [-999999] * (count + 1)
        nums = [-99999] + nums
        for idx in range(1, count+1):
            nums[idx] = max(nums[idx - 1] + nums[idx], nums[idx])

        return max(nums)


s = Solution()
nums = [5, 4, -1, 7, 8]

print(s.maxSubArray(nums))
