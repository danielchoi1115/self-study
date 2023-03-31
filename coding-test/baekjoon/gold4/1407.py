# [1407] 2로 몇 번 나누어질까
# https://www.acmicpc.net/problem/1407
A, B = map(int, input().split())
def dfs(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return (n // 2 + 2*dfs(n//2) + 1) if n % 2 else (n // 2 + 2*dfs(n//2))
print(dfs(B)-dfs(A-1))