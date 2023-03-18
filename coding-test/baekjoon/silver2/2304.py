# 풀이
# 양쪽에서 접근해서 품

import sys
N = int(sys.stdin.readline())
s = dict(sorted([tuple(map(int,sys.stdin.readline().split())) for _ in range(N)]))

lmax, ll = 0, []
for i, h in s.items():
    if lmax <= h:
        ll.append(i)
    lmax = max(lmax, h)

rmax, rl = 0, []
for i, h in reversed(s.items()):
    if rmax <= h:
        rl.append(i)
    rmax = max(rmax, h)
    if h >= lmax: break


def cal(L):
    return sum(abs(L[i+1]-L[i]) * s[L[i]] for i in range(len(L)-1))

print(cal(ll) + cal(rl) + lmax)
