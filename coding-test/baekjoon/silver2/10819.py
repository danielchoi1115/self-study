# [10819] 차이를 최대로
# https://www.acmicpc.net/problem/10819

from itertools import permutations
N = int(input())
ans = -10**4
for perm in permutations(map(int, input().split()), N):
    s = 0
    for i in range(N-1):
        s += abs(perm[i]-perm[i+1])
    if s > ans:
        ans = s
print(ans)
