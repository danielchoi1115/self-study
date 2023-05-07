# [1520] 내리막 길
# https://www.acmicpc.net/problem/1520

import sys
sys.setrecursionlimit(500000)
X, Y = map(int, input().split())
M = [list(map(int, s.split())) for s in sys.stdin.read().rstrip().split('\n')]

dp = [[-1]*Y for _ in range(X)]
vector = [(1,0), (0,1), (-1,0), (0,-1)]

def dfs(x, y):
    if x == X-1 and y == Y-1: return 1
    if dp[x][y] != -1: return dp[x][y]
    dp[x][y] = 0
    for dx, dy in vector:
        if 0 <= x+dx < X and 0 <= y+dy < Y and M[x+dx][y+dy] < M[x][y]:
            dp[x][y] += dfs(x+dx, y+dy)
    return dp[x][y]
print(dfs(0,0))
