# [1759] 암호 만들기
# https://www.acmicpc.net/problem/1759
import sys
L, C = map(int, sys.stdin.readline().split())
chars = sorted(sys.stdin.read().rstrip().split())
used = [0] * C
vowels = {'a', 'e', 'i', 'o', 'u'}

def dfs(start, v, c):
    if (v+c == L-1 and c == 0): return
    if v+c == L:
        if v and c >= 2:
            sys.stdout.write("".join(chars[i] for i in range(C) if used[i])+"\n")
        return
    for i in range(start, C):
        used[i] = 1
        if chars[i] in vowels:
            dfs(i+1, v+1, c)
        else:
            dfs(i+1, v, c+1)
        used[i] = 0
dfs(0, 0, 0)