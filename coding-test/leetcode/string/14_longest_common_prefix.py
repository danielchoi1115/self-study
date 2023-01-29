# https://leetcode.com/problems/longest-common-prefix/

from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        idx = 0
        _max = len(strs[0])
        answer = ""
        found = True
        while idx < _max and found:
            char = strs[0][idx]
            for s in strs:
                if len(s) <= idx or char != s[idx]:
                    found = False
                    break
            if found:
                answer += char
            idx += 1
        return answer

# 200% smarter solution


class Solution2:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        shortest = min(strs, key=len)
        for i, character in enumerate(shortest):
            for other in strs:
                if other[i] != character:
                    return shortest[:i]
        return shortest
