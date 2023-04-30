# [15486] 퇴사 2
# https://www.acmicpc.net/problem/15486
import sys
N = int(input())
arr = [tuple(map(int, m.split())) for m in sys.stdin.read().strip().split('\n')]+[(0,0)]
dp = [0] * (N+1)

ans = 0
for i in range(N+1):
    ans = max(ans, dp[i])
    if i+arr[i][0] > N: continue
    dp[i+arr[i][0]] = max(ans+arr[i][1], dp[i+arr[i][0]])
print(ans)