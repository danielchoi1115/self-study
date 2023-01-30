# https://leetcode.com/problems/rotate-array/

from typing import List
from collections import deque


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        dq = deque(nums)
        for _ in range(k):
            dq.appendleft(dq.pop())
        nums[:] = list(dq)

# smarter solution
# class Solution:
#     def rotate(self, nums: List[int], k: int) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         n = len(nums)
#         k = k%len(nums)
#         a = nums[n-k:] + nums[:n-k]
#         nums[:] = a


nums = [1, 2]
k = 3
s = Solution()
s.rotate(nums, k)
