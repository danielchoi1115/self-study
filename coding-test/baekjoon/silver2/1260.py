# [1260] DFS와 BFS
# https://www.acmicpc.net/problem/1260
import sys
from collections import deque
N, M, start = map(int, input().split())
V = sys.stdin.read().strip().split('\n')

E = {}
def add(k, v):
    if k not in E:
        E[k] = [v]
    else:
        E[k].append(v)
for v in V:
    _f, _t = map(int, v.split())
    add(_f, _t)
    add(_t, _f)
for e in E:
    E[e].sort()

def run(isDfs):
    rt = dfs if isDfs else bfs
    while q:
        m = q.popleft()
        rt.append(m)
        _N = E[m] if m in E else []
        for node in _N:
            if not visited[node]:
                visited[node] = True
                q.append(node)
                if isDfs:
                    run(True)

dfs=[]
bfs=[]

visited = [False] * (N + 1)
visited[start] = True
q = deque([start])
run(True)

visited = [False] * (N + 1)
visited[start] = True
q = deque([start])
run(False)

print(*dfs)
print(*bfs)