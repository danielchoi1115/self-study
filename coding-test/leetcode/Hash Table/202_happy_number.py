# https://leetcode.com/problems/happy-number

class Solution:
    def isHappy(self, n: int) -> bool:
        hashset = set()
        num = 0
        while num != 1:
            for digit in str(n):
                num += int(digit)**2
            if num in hashset:
                break
            hashset.add(num)
            n = num
            num = 0
        if num == 1:
            return True
        return False

# modulo is faster
# class Solution:
#     def isHappy(self, n: int) -> bool:
#         def sum_digit_squares(num: int) -> int:
#             res = 0
#             while num :
#                 res += (num % 10) ** 2
#                 num //= 10
#             return res

#         num = n
#         cache = set()
#         while num != 1:
#             cache.add(num)
#             num = sum_digit_squares(num)

#             if num in cache:
#                 return False
#         return True


s = Solution()
n = 19
ans = s.isHappy(n)
print(ans)
