# [11053] 가장 긴 증가하는 부분 수열
# https://www.acmicpc.net/problem/11053

N = int(input())
A = [0] + list(map(int, input().split()))

dp = [0] * (N+1)
for i in range(1, N+1):
    for j in range(i):
        if A[j] < A[i] and dp[j] + 1 > dp[i]:
            dp[i] = dp[j] + 1

print(max(dp))