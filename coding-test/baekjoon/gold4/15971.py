# [15971] 두 로봇
# https://www.acmicpc.net/problem/15971

import sys
from collections import deque

N, START, DEST = map(int, input().split())
P = sys.stdin.read().strip()
P = P.split('\n') if P else []

visited = [0] * (N+1)
parent = [0] * (N+1)
M = {}
D = {}

for r in P:
    r1, r2, d = map(int, r.split())
    M.setdefault(r1, []).append(r2)
    M.setdefault(r2, []).append(r1)
    D[(r1,r2)] = D[(r2,r1)] =d


def bfs():
    if N == 1: return
    while dq:
        node = dq.popleft()
        visited[node] = 1
        for cand in M[node]:
            if visited[cand]:
                continue
            parent[cand] = node
            if cand == DEST: return
            dq.appendleft(cand)

dq = deque([START])

bfs()

start = DEST
total = 0
max_ = 0
while parent[start] != 0:
    pair = (start, parent[start])
    if D[pair] > max_:
        max_ = D[pair]
    total += D[pair]
    start = parent[start]
    
print(total - max_)