# https://www.acmicpc.net/problem/17945

import sys
B, C = map(int,sys.stdin.readline().split())

z = pow(2*B,2)-4*C

x1 = int((-2*B + z**0.5)/2)
x2 = int((-2*B - z**0.5)/2)
if x1 == x2: 
    print(x1)
else:
    ans=[x1, x2]
    ans.sort()
    print(" ".join(map(str,ans)))