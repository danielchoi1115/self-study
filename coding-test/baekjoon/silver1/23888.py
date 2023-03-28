# [23888] 등차수열과 쿼리
# https://www.acmicpc.net/problem/23888

import math
import sys
inp = sys.stdin.readline

def seq_sum(a, d, n):
    return n*(2*a + (n-1)*d)//2

a, d = map(int, inp().strip().split())
N = int(inp())

for _ in range(N):
    c, l, r = map(int, inp().strip().split())
    a1 = a+d*(l-1)
    if c == 1:
        print(seq_sum(a1, d, r-l+1))
    elif r == l:
        print(a1)
    else:
        print(math.gcd(a1, d))