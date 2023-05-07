# [9251] LCS
# https://www.acmicpc.net/problem/9251

A = input()
B = input()

dp = [[0] * (len(A)+1) for _ in range(len(B)+1)]

for r in range(1, len(B)+1):
    for c in range(1, len(A)+1):
        if A[c-1] == B[r-1]:
            dp[r][c] = max(dp[r][c-1], dp[r-1][c], dp[r-1][c-1] + 1)
        else:
            dp[r][c] = max(dp[r][c-1], dp[r-1][c])

print(dp[-1][-1])