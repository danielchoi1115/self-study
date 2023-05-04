# [12865] 평범한 배낭
# https://www.acmicpc.net/problem/12865
import sys
N, K = map(int, input().split())
items = [(0,0)] + sorted(tuple(map(int, i.split())) for i in sys.stdin.read().strip().split('\n'))

dp = [[0]*(K+1) for _ in range(N+1)]

for i in range(1, N+1):
    for k in range(1, K+1):
        if items[i][0] > k:
            dp[i][k] = dp[i-1][k]
            continue
        dp[i][k] = max(dp[i-1][k], dp[i-1][k-items[i][0]]+items[i][1])

print(dp[-1][-1])