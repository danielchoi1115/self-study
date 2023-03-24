# [15970] 화살표 그리기
# https://www.acmicpc.net/problem/15970
import sys
N = int(sys.stdin.readline())
dots = {}
for _ in range(N):
    x, c = map(int, sys.stdin.readline().split())
    if c in dots:
        dots[c].append(x)
    else:
        dots[c] = [x]
ans = 0
for X in dots.values():
    X.sort()
    for i in range(len(X)):
        if len(X) == 1:
            val = 0
        elif i == 0:
            val = X[i+1] - X[i]
        elif i == len(X)-1:
            val = X[i] - X[i-1]
        else: 
            val = min(X[i] - X[i-1], X[i+1] - X[i])
        ans += val
print(ans)
