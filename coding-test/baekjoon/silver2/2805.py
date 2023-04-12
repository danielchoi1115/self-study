# [2805] 나무 자르기
# https://www.acmicpc.net/problem/2805

N, M = map(int, input().split())
T = sorted(map(int, input().split()), reverse=True)
l, r = 0, T[0]
while l <= r:
    c = (l+r) // 2
    cut = 0
    for t in T:
        cut += max(0, t-c)
        if cut >= M: break
    if cut < M: r = c - 1
    else: l = c + 1
print(r)
