# [4375] 1
# https://www.acmicpc.net/problem/4375

import sys
for num in map(int, sys.stdin.read().split()):
    a = cnt = 1
    while True:
        if a % num == 0:
            print(cnt)
            break
        a = a*10+1
        a %= num
        cnt+=1