# https://leetcode.com/problems/count-binary-substrings/
# 696. Count Binary Substrings
from collections import deque


class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        substrings = []
        clusters = []
        
        # 001100011
        100
        output = 0
        q = deque()
        
        for c in s:
            while q and q[-1] == c and q[0] != c:
                q.pop()
                
            if q and q[-1] != c:
                q.pop()
                output += 1
            q.appendleft()
        return len(substrings)
# get largest substring

# 