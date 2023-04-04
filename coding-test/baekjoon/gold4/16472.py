# [16472] 고냥이
# https://www.acmicpc.net/problem/16472

N = int(input())
S = input()
ans = 0
l = r = 0
M = {}

def update(m, k, v):
    if k not in M:
        m[k] = v
    else:
        m[k] += v
    if not m[k]: 
        del m[k]
n = len(S)
while r < n:
    update(M, S[r], 1)
    r += 1
    if len(M) <= N:
        ans = max(ans, r-l)
    if len(M) > N:
        update(M, S[l], -1)
        l += 1
print(ans)