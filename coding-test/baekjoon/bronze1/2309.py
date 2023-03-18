# https://www.acmicpc.net/problem/2309
# [2309] 일곱 난쟁이
from itertools import combinations
import sys
s = [int(sys.stdin.readline()) for _ in range(9)]
seven = combinations(s, 7)
for item in seven:
    if sum(item) == 100:
        for i in sorted(item):
            print(i)
        break