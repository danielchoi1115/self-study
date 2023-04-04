# [1484] 다이어트
# https://www.acmicpc.net/problem/1484

G = int(input())
found = 0
for i in range(1, G):
    num = G + i**2
    inum = int((G + i**2)**0.5)
    if num == inum**2:
        print(inum)
        found = 1
if not found:
    print(-1)