# [16970] 정수 좌표의 개수
# https://www.acmicpc.net/problem/16970

import math
import itertools
from time import time
N, M, K = map(int, input().split())

t1 = time()
def isValid(x, y):
    return x >= 0 and y >= 0 and x <= N and y <= M
s=  0
for x_from, y_from in itertools.product(range(N+1), range(M+1)):
    for x_to, y_to in itertools.product(range(N+1), range(M+1)):
        if math.gcd(abs(x_from-x_to), abs(y_from-y_to)) == K - 1:
            s += 1
print(time()-t1)
print(s//2)
