# [10655] 마라톤 1
# https://www.acmicpc.net/problem/10655

import sys
N = int(sys.stdin.readline())
P = [tuple(map(int,sys.stdin.readline().split())) for _ in range(N)]

def dist(p1, p2):
    return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])

s, max_d, skip_d = 0, 0, 0
for i in range(1, N):
    prv = dist(P[i], P[i-1])
    s += prv
    if i == N - 1: 
        continue
    max_d = max(max_d, dist(P[i+1], P[i]) + prv - dist(P[i+1], P[i-1]))
print(s-max_d)

# 0 8 3 3