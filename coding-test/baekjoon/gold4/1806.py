# [1806] 부분합
# https://www.acmicpc.net/problem/1806

import sys
N, S = map(int, sys.stdin.readline().split())
m = [*map(int, sys.stdin.readline().split())]

ans = 10**8+1
l = r = s = 0
while l < N and (s >= S or r < N):
    if s < S:
        s += m[r]
        r += 1
    else:
        s -= m[l]
        l += 1
    if s >= S and l != r:
        ans = min(ans, r-l)

if S == 0:
    ans = 1
print(0 if ans == 10**8+1 else ans)