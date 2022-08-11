# https://leetcode.com/problems/climbing-stairs/
# 70. Climbing Stairs

import time


class Solution:
    def climbStairs(self, n: int) -> int:
        climbHash = {
            0: 0,
            1: 1,
            2: 2,
            3: 3
        }

        def helper(n: int, totalWays: int) -> int:
            if n not in climbHash:
                ways = helper(n - 1, totalWays) + helper(n - 2, totalWays)
                climbHash[n] = ways
                totalWays += ways
            else:
                totalWays += climbHash[n]
            return totalWays
        return helper(n, 0)

    def climbStairs2(self, n: int) -> int:
        l, r = 1, 1
        for _ in range(n-1):
            temp = l
            l = l+r
            r = temp
        return l


s = Solution()
n = 70
s.climbStairs(n)

