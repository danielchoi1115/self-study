# [1987] 알파벳
# https://www.acmicpc.net/problem/1987

import sys

R, C = map(int, input().split())
B = sys.stdin.read().strip()
MAX = len(set(B)-{'\n'})
B = list(B.strip().split("\n"))

ans = 0
vector = [(1,0), (0,1), (-1,0), (0,-1)]
alpha = [0] * 26
memo = {}

def dfs(r, c, visited):
    global ans
    if ans == MAX: return
    key = (r, c, tuple(visited))
    if key in memo:
        ans = max(ans, memo[key])
        return
    ans = max(ans, sum(visited))
    for dr, dc in vector:
        if not (0 <= r+dr < R and 0 <= c+dc < C):
            continue
        idx = ord(B[r+dr][c+dc])-65
        if visited[idx] == 1:
            continue
        visited[idx] = 1
        dfs(r+dr, c+dc, visited)
        visited[idx] = 0
    memo[key] = ans
    
alpha[ord(B[0][0])-65] = 1
dfs(0, 0, alpha)
print(ans)