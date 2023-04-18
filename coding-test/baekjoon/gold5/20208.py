# [20208] 진우의 민트초코우유
# https://www.acmicpc.net/problem/20208
import sys
N, M, H = map(int, input().split())

MAP = [list(map(int, l.split())) for l in sys.stdin.read().strip().split('\n')]

ans, X0, Y0 = [0], 0, 0
MINTS = {}
for i in range(N):
    for j in range(N):
        if MAP[i][j] == 1: 
            X0, Y0 = i, j
        if MAP[i][j] == 2:
            MINTS[(i,j)] = 0
total_mints = len(MINTS)

def manhattan(x1, y1, x2, y2):
    return abs(x1-x2) + abs(y1-y2)

def dfs(x, y, health):
    if total_mints == ans[0]: return
    for mint, visited in MINTS.items():
        if visited: continue
        mx, my = mint
        dist = manhattan(x, y, mx, my)
        if health-dist >= 0:
            MINTS[mint] = 1
            dfs(mx, my, health-dist+H)
            MINTS[mint] = 0
    if health-manhattan(x, y, X0, Y0) >= 0:
        ans[0] = max(ans[0], sum(MINTS.values()))
    
dfs(X0, Y0, M)
print(ans[0])