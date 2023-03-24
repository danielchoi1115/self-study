# [2082] 시계
# https://www.acmicpc.net/problem/2082

import sys
T = [
    "####.##.##.####",
    "..#..#..#..#..#",
    "###..#####..###",
    "###..####..####",
    "#.##.####..#..#",
    "####..###..####",
    "####..####.####",
    "###..#..#..#..#",
    "####.#####.####",
    "####.####..####"
]
N = [sys.stdin.readline().split() for _ in range(5)]
nums = [N[0][i]+N[1][i]+N[2][i]+N[3][i]+N[4][i] for i in range(4)]

ans = []
for n in nums:
    for i, t in enumerate(T):
        if not any(a == "#" and b == "." for a, b in zip(n, t)): 
            ans.append(i)
            break
print(f"{ans[0]}{ans[1]}:{ans[2]}{ans[3]}")
