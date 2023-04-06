
# [14465] 소가 길을 건너간 이유 5
# https://www.acmicpc.net/problem/14465
import sys
N, K, ans = map(int, input().split())
broken = set(map(int, sys.stdin.read().split()))
cnt = 0
for i in range(1, N):
    lst = i-K+1
    nxt = i
    if lst > 0 and lst in broken: 
        cnt -= 1
    if nxt in broken: 
        cnt += 1
    ans = min(ans, cnt) if lst > 0 else ans
print(ans)
