# [2792] 보석상자
# https://www.acmicpc.net/problem/2792

import sys
N, M = map(int, input().split())
S = list(map(int, sys.stdin.read().strip().split('\n')))
l, r = 1, max(S)
def check(j):
    cnt = 0
    for s in S:
        if s > j:
            cnt += s // j
        if s <= j or s % j:
            cnt += 1
    return cnt <= N
while l < r:
    mid = (l+r)//2
    
    if check(mid):
        r = mid
    else:
        l = mid + 1
print(l)