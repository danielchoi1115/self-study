# [9012] 괄호
# https://www.acmicpc.net/problem/9012

from collections import deque
import sys
pin = sys.stdin.readline

N = int(pin())

for _ in range(N):
    dq = deque()
    for p in pin().strip():
        if dq and dq[-1] == '(' and p == ')':
            dq.pop()
        else:
            dq.append(p)
    print('NO' if len(dq) else 'YES')