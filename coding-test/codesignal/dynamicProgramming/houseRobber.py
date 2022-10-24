def solution(nums):
    length = len(nums)
    dp = [0]* (length + 2)
    for i in range(2, length+2):
        dp[i] = max(dp[i-1], nums[i-2]+dp[i-2])
    return max(dp)
    
# solution using less space
# by AWice
def solution(A):
    a = b = 0
    for x in A:
        a, b = b + x, max(a, b)
    return max(a, b)