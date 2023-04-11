# [2121] 넷이 놀기
# https://www.acmicpc.net/problem/2121

import sys
N = int(input())
A, B = map(int, input().split())

P = {}
for p in sys.stdin.read().strip().split('\n'):
    a, b = map(int, p.split())
    if a in P:
        P[a].add(b)
    else:
        P[a] = {b}
ans = 0
for a in P:
    for b in P[a]:
        if (a+A in P and (b in P[a+A] and b+B in P[a+A]) and 
            b+B in P[a]):
            ans += 1
print(ans)