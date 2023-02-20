# https://leetcode.com/problems/longest-substring-without-repeating-characters/submissions/901558245/

from collections import deque

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charset = set()
        dq = deque()
        ans = 0
        for char in s:
            if char in charset:
                while (c:=dq.popleft()) != char:
                    charset.remove(c)
            charset.add(char)
            dq.append(char)
            ans = max(ans, len(dq))
        return ans