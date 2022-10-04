# https://leetcode.com/problems/jump-game-iii/
# 1306. Jump Game III
from typing import List
class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        visited = {}

        def helper(arr: List[int], start: int) -> bool:
            if arr[start] == 0:
                return True

            visited[start] = True
            num = arr[start]
            left = start - num
            right = start + num

            isLeft = False
            isRight = False

            if left > -1:
                if left not in visited:
                    isLeft = helper(arr, left)

            if right < len(arr):
                if right not in visited:
                    isRight = helper(arr, right)

            return isLeft or isRight

        return helper(arr, start)


a = Solution()
arr = [4, 2, 3, 0, 3, 1, 2]
arr = [3, 0, 1, 2]
start = 0

print(a.canReach(arr, start))
