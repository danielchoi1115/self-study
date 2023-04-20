# [15649] N과 M (1)
# https://www.acmicpc.net/problem/15649
import sys
from itertools import permutations
N, M = map(int, input().split())
sys.stdout.write("\n".join(list(map(" ".join, permutations(map(str, range(1, N+1)), M)))))
