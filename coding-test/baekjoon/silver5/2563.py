# 2563 색종이
# https://www.acmicpc.net/problem/2563

import sys
N = int(sys.stdin.readline())
m = [[0] * 100 for _ in range(100)]
for i in range(N):
    x, y = map(int,sys.stdin.readline().split())
    for i in range(x, x+10):
        for j in range(y, y+10):
            m[i][j] = 1
print(sum(sum(row) for row in m))