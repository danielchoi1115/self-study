# [7576] 토마토
# https://www.acmicpc.net/problem/7576

import sys
from collections import deque

C, R = map(int, input().split())
box, dq = [], deque()
total, ripen, ans = C*R, 0, -1

for line in sys.stdin.read().strip().split('\n'):
    box.append(list(map(int, line.split())))
    for col, val in enumerate(box[-1]):
        if val == -1: 
            total -= 1
        elif val == 1: 
            dq.append((len(box)-1, col, 0))
            box[-1][col] = 0

vectors = [(1,0), (0,1), (-1,0), (0,-1)]

while dq:
    r, c, day = dq.popleft()
    if box[r][c] != 0: continue
    ripen += 1
    box[r][c] = 1
    if total == ripen: 
        ans = day
        break
    for dr, dc in vectors: 
        if 0 <= r+dr < R and 0 <= c+dc < C and box[r+dr][c+dc] == 0:
            dq.append((r+dr, c+dc, day+1))

print(ans)