# [14002] 가장 긴 증가하는 부분 수열 4 
# https://www.acmicpc.net/problem/14002
from bisect import bisect_left
N = int(input())
A = list(map(int, input().split()))

active = {A[0]: [A[0]]}
ends = [A[0]]
for a in A[1:]:
    pos = bisect_left(ends, a)
    if a in active: continue
    if pos == 0:
        active.pop(ends[0])
        ends[0] = a
        active[a] = [a]
    elif pos == len(ends):
        active[a] = active[ends[-1]][:] + [a]
        ends.append(a)
    else:
        target = ends[pos-1]
        active[a] = active[target][:] + [a]
        ends.insert(pos, a)
        targetlength = len(active[a])
        
        for k in list(active.keys()):
            if len(active[k]) == targetlength and k != a:
                active.pop(k)
                ends.pop(bisect_left(ends, k))

ans = max(active.values())
print(len(ans))
print(*ans)