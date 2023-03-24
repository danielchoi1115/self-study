# [23351] 물 주기
# https://www.acmicpc.net/problem/23351

import sys

N, K, A, B = map(int,sys.stdin.readline().split())
flowers = [K] * N
ans = 1
pos = 0
died = False
while not died:
    for _ in range(A):
        flowers[pos] += B
        pos = (pos+1) % N
    
    for i in range(N):
        flowers[i] -= 1
        if not flowers[i]: 
            died = True
            break
    else:
        ans += 1
print(ans)
    