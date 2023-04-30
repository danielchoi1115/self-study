# [1699] 제곱수의 합
# https://www.acmicpc.net/problem/1699

N = int(input())

nums = [i**2 for i in range(1, int(N**0.5)+1)]  
dp = [0] * (N+1)
for n in range(1, N+1):
    min_ = 100001
    for i in range(int(n**0.5)):
        if dp[n - nums[i]] + 1 < min_:
            min_ = dp[n - nums[i]] + 1
    dp[n] = min_
    
print(dp[-1])