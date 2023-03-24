# [17286] 유미
# https://www.acmicpc.net/problem/17286

import sys
Y = tuple(map(int, sys.stdin.readline().split()))
P = [tuple(map(int, sys.stdin.readline().split())) for _ in range(3)]

ans = 0
while P:
    dist = [(abs(Y[0]-p[0])**2 + abs(Y[1]-p[1])**2)**0.5 for p in P]
    min_dist = min(dist)
    Y = P.pop(dist.index(min_dist))
    ans += min_dist
    
print(int(ans))