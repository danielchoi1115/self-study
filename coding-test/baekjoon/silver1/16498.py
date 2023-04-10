# [16598] 작은 벌점
# https://www.acmicpc.net/problem/16498

from bisect import bisect_left
input()

A = sorted(list(map(int, input().split())))
B = list(map(int, input().split()))
C = sorted(list(map(int, input().split())))

ans = float('inf')
for b in B:
    ai = bisect_left(A, b)
    ci = bisect_left(C, b)
    for aj in range(max(0, ai-1), min(len(A), ai+2)):
        for cj in range(max(0, ci-1), min(len(C), ci+2)):
            a = A[aj]
            c = C[cj]
            ans = min(ans, abs(max(a,b,c) - min(a,b,c)))
print(ans)