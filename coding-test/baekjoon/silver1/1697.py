# [1697] 숨바꼭질
# https://www.acmicpc.net/problem/1697
from collections import deque

N, K = map(int, input().split())

### DFS 풀이 ###
def dfs(n, k):
    if n >= k: 
        return n - k
    if k == 1: 
        return 1
    if k % 2: 
        return min(dfs(n, k+1), dfs(n, k-1))+1
    return min(k-n, dfs(n, k//2)+1)

print(dfs(N, K))

### BFS 풀이 ###
def bfs():
    time = [100001]*100001
    dq = deque([(N, 0)])
    while dq:
        n, t = dq.popleft()
        if time[n] < t: continue
        time[n] = t
        if n >= K:
            time[K] = min(time[K], t+n-K)
        else:
            if t == time[K]: continue
            if n+1 <= K:
                dq.append((n+1, t+1))
            if n < 50001:
                dq.append((n*2, t+1))
            if n > 0:
                dq.append((n-1, t+1))
    return time[K]
print(bfs())

