# [11724] 연결 요소의 개수
# https://www.acmicpc.net/problem/2667

import sys
from collections import deque

N, M = map(int, input().split())
P = sys.stdin.read().strip()
P = P.split('\n') if P else []
pmap = {}

for p in P:
    p1, p2 = map(int, p.split())
    pmap.setdefault(p1, []).append(p2)
    pmap.setdefault(p2, []).append(p1)
    
visited = [0] * (N+1)

dq = deque()

def bfs():
    isComponent = False
    while dq:
        toVisit = dq.popleft()
        if visited[toVisit]: continue
        isComponent = True
        visited[toVisit] = 1
        if toVisit not in pmap: continue
        dq.extend(pmap[toVisit])
    return isComponent

ans = 0
for i in range(1, N+1):
    dq.append(i)
    if bfs():
        ans += 1
print(ans)