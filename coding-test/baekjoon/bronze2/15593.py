# 15593 Lifeguards (Bronze)
# https://www.acmicpc.net/problem/15593

import sys
N = int(sys.stdin.readline())
s = list(sorted([list(map(int,sys.stdin.readline().split())) for _ in range(N)]))

ans = 0

for ex in range(N):
    if N == 1: break
    stack = [s[1][:]] if ex == 0 else [s[0][:]]

    for j in range(1, len(s)):
        if j == ex: continue
        if s[j][0] <= stack[-1][1]:
            stack[-1][1] = max(stack[-1][1], s[j][1])
        else:
            stack.append(s[j][:])
    ans = max(ans, sum(s[1]-s[0] for s in stack))
print(ans)
