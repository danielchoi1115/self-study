# [16970] 정수 좌표의 개수
# https://www.acmicpc.net/problem/16970

import math
import itertools
from time import time
N, M, K = map(int, input().split())

t1 = time()
def isValid(x, y):
    return x >= 0 and y >= 0 and x <= N and y <= M
S = set()
for x_from, y_from in itertools.product(range(N+1), range(M+1)):
    for x_to, y_to in itertools.product(range(N+1), range(M+1)):
        if x_from == x_to and y_from == y_to: continue
        dx = x_to - x_from
        dy = y_to - y_from
        
        gcd = math.gcd(dx, dy)
        slope_x = dx // gcd
        slope_y = dy // gcd

        x_k = x_from + slope_x * (K - 1)
        y_k = y_from + slope_y * (K - 1)

        if isValid(x_k, y_k):
            S.add(frozenset({(x_from, y_from), (x_k, y_k)}))
print(time()-t1)
print(len(S))
