
# [14465] 소가 길을 건너간 이유 5
# https://www.acmicpc.net/problem/14465
import sys
N, r, ans = map(int, input().split())
broken = set(map(int, sys.stdin.read().split()))
cnt = sum(s in broken for s in range(1, r+1))
l = 1
while r < N:
    if l in broken: 
        cnt -= 1
    l += 1
    r += 1
    if r in broken: 
        cnt += 1
    ans = min(ans, cnt)
print(ans)
