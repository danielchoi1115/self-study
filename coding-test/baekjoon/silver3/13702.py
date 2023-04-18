# [13702] 이상한 술집
# https://www.acmicpc.net/problem/13702

import sys
N, K = map(int, input().split())
M = list(map(int, sys.stdin.read().strip().split()))
l, r = 0, max(M)
while l <= r:
    mid = (l+r)//2
    if mid == 0: break
    cnt = 0
    for m in M:
        cnt += m//mid
    if cnt < K:
        r = mid - 1
    else:
        l = mid + 1
print(r)