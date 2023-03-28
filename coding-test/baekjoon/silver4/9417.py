# [9417] 최대 GCD
# https://www.acmicpc.net/problem/9417

from itertools import combinations
import math

N = int(input())
for _ in range(N):
    combi = combinations(list(map(int, input().strip().split())), 2)
    m = 1
    for a, b in combi:
        m = max(m, math.gcd(a, b))
    print(m)