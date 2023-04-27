# 게임 맵 최단거리
# https://school.programmers.co.kr/learn/courses/30/lessons/1844#
from collections import deque
def solution(maps):
    answer = 0
    N, M = len(maps), len(maps[0])
    vectors = [(0,1),(0,-1),(1,0),(-1,0)]
    visited = [[0]*M for _ in range(N)]
    def isValid(x, y):
        return x >= 0 and x < N and y >= 0 and y < M and maps[x][y]
    dist = -1
    dq = deque([(0,0,1)])
    while dq:
        x, y, dist = dq.popleft()
        visited[x][y] = 2
        if x == N-1 and y == M-1:
            break
        for dx, dy in vectors:
            if not isValid(x+dx, y+dy) or visited[x+dx][y+dy]: continue
            dq.append((x+dx, y+dy, dist+1))
            visited[x+dx][y+dy] = 1
    return dist if visited[N-1][M-1] == 2 else -1

from time import time
maps = [[1]*100 for _ in range(100)]
# maps = [[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 0], [0, 0, 0, 0, 1]]
t1 = time()
print(solution(maps))
print(time()-t1)