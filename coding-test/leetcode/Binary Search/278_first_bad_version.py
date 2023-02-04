# https://leetcode.com/problems/first-bad-version/

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l = 0
        r = n
        while l < r:
            m = (l+r)//2
            isBad = isBadVersion(m)
            isBadPrev = isBadVersion(m-1)
            if isBad and not isBadPrev:
                return m
            elif isBad and isBadPrev:
                r = m-1
            else:
                l = m+1
        return l
