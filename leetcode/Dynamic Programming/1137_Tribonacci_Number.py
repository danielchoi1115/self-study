# https://leetcode.com/problems/n-th-tribonacci-number/
# 1137. N-th Tribonacci Number

class Solution:
    def tribonacci(self, n: int) -> int:
        fiboHash = {
            0: 0,
            1: 1,
            2: 1
        }

        def helper(n: int) -> int:
            if n in fiboHash:
                return fiboHash[n]
            fibo = helper(n-1) + helper(n-2) + helper(n-3)
            fiboHash[n] = fibo
            return fibo
        return helper(n)


# 1 1 2 3 5 8 13 21
a = Solution()
n = 25
print(a.tribonacci(n))
