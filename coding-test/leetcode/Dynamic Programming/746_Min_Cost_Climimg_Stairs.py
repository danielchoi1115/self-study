# https://leetcode.com/problems/min-cost-climbing-stairs/
# 746. Min Cost Climbing Stairs


from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n_stairs = len(cost) - 1
        cost.extend((0, 0))
        while n_stairs >= 0:
            cost1 = cost[n_stairs] + cost[n_stairs + 1]
            cost2 = cost[n_stairs] + cost[n_stairs + 2]
            cost[n_stairs] = min(cost1, cost2)
            n_stairs -= 1
        return min(cost[0], cost[1])


s = Solution()
cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]  # min cost = 6
# cost = [0, 2, 2, 1] # min cost = 2
print(s.minCostClimbingStairs(cost))
