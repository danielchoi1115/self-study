# https://leetcode.com/problems/spiral-matrix/

from typing import List

# Skills
# Set, Matrix traversal

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        d_index = 0
        hashset = set()
        size = len(matrix) * len(matrix[0])
        order = []
        
        def isValid(r, c):
            if (r, c) in hashset or r >= len(matrix) or c >= len(matrix[0]) or r < 0 or c < 0:
                return False
            return True
        
        d = directions[d_index]
        r = c = 0
        while len(hashset) < size:
            if isValid(r, c) == False:
                r -= d[0]
                c -= d[1]
                d_index = (d_index+1) % 4
                d = directions[d_index]
                r += d[0]
                c += d[1]
                continue
            order.append(matrix[r][c])
            hashset.add((r, c))
            r += d[0]
            c += d[1]
        return order


s = Solution()
m = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
s.spiralOrder(m)
