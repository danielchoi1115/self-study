# 16955 오목, 이길 수 있을까?
# https://www.acmicpc.net/problem/16955
import sys
M = [sys.stdin.readline().strip() for _ in range(10)]
vectors = [(-1,  1), ( 1, -1), ( 0,  1), ( 1,  1), ( 1,  0), ( 0, -1), (-1, -1), (-1,  0)]
def isValid(row, col, dr, dc):
    return row+dr >= 0 and row+dr <= 9 and col+dc >= 0 and col+dc <= 9
ans = False
for row in range(10):
    for col in range(10):
        if M[row][col] != 'X': continue
        for dr, dc in vectors:
            dcnt = xcnt = 0
            newR = row
            newC = col
            for _ in range(5):
                if (
                    newR < 0
                    or newR > 9
                    or newC < 0
                    or newC > 9
                ):
                    break
                if M[newR][newC] == '.':
                    dcnt += 1
                elif M[newR][newC] == 'X':
                    xcnt += 1
                newR += dr
                newC += dc
            if dcnt == 1 and xcnt == 4:
                ans = True
print("1" if ans else "0")