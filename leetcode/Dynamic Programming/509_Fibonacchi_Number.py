# https://leetcode.com/problems/fibonacci-number/
# 509. Fibonacci Number
class Solution:
    def fib(self, n: int) -> int:
        fiboHash = {
            0: 0,
            1: 1
        }

        def helper(n: int) -> int:
            if n in fiboHash:
                return fiboHash[n]
            fibo = helper(n-1) + helper(n-2)
            fiboHash[n] = fibo
            return fibo
        return helper(n)


# 1 1 2 3 5 8 13 21
a = Solution()
n = 30
print(a.fib(n))
