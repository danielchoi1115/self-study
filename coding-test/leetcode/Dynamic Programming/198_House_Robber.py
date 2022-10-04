# https://leetcode.com/problems/house-robber/
# 198. House Robber

from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        # Incomplete DP Solution
        n_houses = len(nums) - 1
        nums.extend([0, 0])  # dummy house
        while n_houses >= 0:
            # maxMoney = 0
            # possible_houses = nums[n_houses + 2:]
            # for h in possible_houses:
            #     if h > maxMoney:
            #         maxMoney = h

            nums[n_houses] += max(nums[n_houses+1], nums[n_houses+2])
            n_houses -= 1
        return max(nums[0], nums[1])

    # Better Solution
    def rob2(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * (n + 2)

        for i in range(n - 1, -1, -1):
            dp[i] = max(dp[i + 1], dp[i + 2] + nums[i])

        return dp[0]


s = Solution()
nums = [1, 100, 1, 1, 100]
print(s.rob2(nums))
