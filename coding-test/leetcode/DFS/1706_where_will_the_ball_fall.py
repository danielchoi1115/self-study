# https://leetcode.com/problems/where-will-the-ball-fall/
from typing import List


class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        answer = []

        def travel(b, rows=len(grid)):
            depth = 0
            while depth < rows:
                d1 = grid[depth][b]
                d2_idx = b + d1
                if d2_idx < 0 or d2_idx >= len(grid[0]):
                    return -1
                d2 = grid[depth][d2_idx]
                if d1 + d2 == 0:
                    return -1
                depth += 1
                b += d1
            return b
        for b in range(len(grid[0])):
            answer.append(travel(b))
        return answer
