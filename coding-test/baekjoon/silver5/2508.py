# 2503 사탕 박사 고창영
# https://www.acmicpc.net/problem/2503

import sys
N = int(sys.stdin.readline().strip())

for _ in range(N):
    sys.stdin.readline()
    row, col = map(int, sys.stdin.readline().split())
    M = [sys.stdin.readline().strip() for _ in range(row)]
    ans = 0
    for r in range(row):
        for c in range(col):
            if M[r][c] != "o": continue
            if (c-1 >= 0 and M[r][c-1] == ">") and (c+1 < col and M[r][c+1] == "<"): 
                ans += 1
            if (r-1 >= 0 and M[r-1][c] == "v") and (r+1 < row and M[r+1][c] == "^"): 
                ans += 1
    print(ans)