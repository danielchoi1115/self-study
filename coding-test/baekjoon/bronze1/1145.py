# https://www.acmicpc.net/problem/1145
import sys
from itertools import combinations
from math import lcm
nums = list(map(int, sys.stdin.readline().split()))
combi = [lcm(*c) for c in combinations(nums, 3)]
print(min(combi))
