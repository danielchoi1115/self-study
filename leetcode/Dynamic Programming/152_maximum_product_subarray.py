# https://leetcode.com/problems/maximum-product-subarray/
# 152. Maximum Product Subarray

from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        count = len(nums)
        if count == 1:
            return nums[0]
        dp_max = [0] * count
        dp_min = [0] * count

        for idx in range(count):
            if idx == 0:
                dp_max[0] = nums[0]
                dp_min[0] = nums[0]
                continue
            dp_max[idx] = max(dp_max[idx - 1] * nums[idx], dp_min[idx - 1] * nums[idx], nums[idx])
            dp_min[idx] = min(dp_max[idx - 1] * nums[idx], dp_min[idx - 1] * nums[idx], nums[idx])
        return max(dp_max + dp_min)


s = Solution()
nums = [-2, 3, -4]

print(s.maxProduct(nums))
