# 2503 숫자야구
# https://www.acmicpc.net/problem/2503

import sys
import itertools
_input = sys.stdin.readline
N = int(_input())
guesses = [_input().split() for _ in range(N)]
nums = itertools.permutations('123456789', 3)

cnt = 0
for target in nums:
    for guess in guesses:
        s = sum(guess[0][i] == target[i] for i in range(3))
        b = len(set(guess[0]) & set(target)) - s
        if s != int(guess[1]) or b != int(guess[2]):
            break
    else:
        cnt += 1
print(cnt)