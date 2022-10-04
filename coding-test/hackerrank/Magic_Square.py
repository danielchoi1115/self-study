# https://www.hackerrank.com/challenges/magic-square-forming/problem?isFullScreen=true

import itertools


def formingMagicSquare(s):
    L = range(1, 10)
    magic_squares = []
    for p in itertools.permutations(L):
        if (p[0] + p[1] + p[2] ==
            p[3] + p[4] + p[5] ==
            p[6] + p[7] + p[8] ==
            p[0] + p[3] + p[6] ==
            p[1] + p[4] + p[7] ==
            p[2] + p[5] + p[8] ==
            p[0] + p[4] + p[8] ==
                p[2] + p[4] + p[6]):
            magic_squares.append(p)

    s_1d = []
    for i in range(3):
        for j in range(3):
            s_1d.append(s[i][j])

    min_cost = 100
    for m in magic_squares:
        diff = 0
        for i in range(9):
            diff += abs(s_1d[i] - m[i])
        min_cost = min(diff, min_cost)
    return min_cost


s = [[5, 3, 4], [1, 5, 8], [6, 4, 2]]
s = [[4, 8, 2], [4, 5, 7], [6, 1, 6]]
print(formingMagicSquare(s))
