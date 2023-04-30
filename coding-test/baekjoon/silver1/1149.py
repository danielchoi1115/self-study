# [1149] RGB거리
# https://www.acmicpc.net/problem/1149

import sys
N = int(input())
RGB = sys.stdin.read().strip().split('\n')
dp_map = { 0: [1,2], 1: [0,2], 2: [0,1]}
dp = [[0,0,0] for _ in range(N+1)]
for n in range(1, N+1):
    rgb = list(map(int, RGB[n-1].split()))
    for i in range(3):
        dp[n][i] = rgb[i] + min(dp[n-1][v] for v in dp_map[i])
print(min(dp[N]))
