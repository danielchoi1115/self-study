# 14697 방 배정하기
# https://www.acmicpc.net/problem/14697
import sys
a, b, c, N = map(int, sys.stdin.readline().split())
found = False
for i in range(0, N+1, c):
    if found: break
    for j in range(0, N+1, b):
        for k in range(0, N+1, a):
            if (i+j+k) == N:
                found = True
                break
            
print(1 if found else 0)