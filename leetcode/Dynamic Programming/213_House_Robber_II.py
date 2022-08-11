# https://leetcode.com/problems/house-robber-ii/
# 213. House Robber II
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        def helper(nums: List[int]) -> int:
            n = len(nums)
            dp = [0] * (n + 2)

            for i in range(n - 1, -1, -1):
                dp[i] = max(dp[i+1], dp[i+2] + nums[i])

            return max(dp[0], dp[1])
        if len(nums) == 1:
            return nums[0]
        l = helper(nums[:-1])
        r = helper(nums[1:])

        return max(l, r)


s = Solution()
nums = [1]
print(s.rob(nums))
