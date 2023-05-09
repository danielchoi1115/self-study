# [2606] 바이러스
# https://www.acmicpc.net/problem/2606
import sys
from collections import deque
V = int(input())
E = int(input())

M = {}
for p in sys.stdin.read().strip().split("\n"):
    v1, v2 = map(int, p.split())
    M.setdefault(v1, []).append(v2)
    M.setdefault(v2, []).append(v1)
dq = deque([1])
visited = [0] * (V + 1)
while dq:
    cand = dq.pop()
    if visited[cand]:
        continue
    visited[cand] = 1
    if cand in M:
        dq.extend(M[cand])
    
print(sum(visited)-1)