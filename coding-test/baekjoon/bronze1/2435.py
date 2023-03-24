# [2435] 기상청 인턴 신현수
# https://www.acmicpc.net/problem/2435

import sys
N, K = map(int, sys.stdin.readline().split())
T = list(map(int, sys.stdin.readline().split()))
ans = -(10*10)
for i in range(N-K+1):
    ans = max(ans, sum(T[i:i+K]))
print(ans)