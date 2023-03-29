# [15996] 팩토리얼 나누기
# https://www.acmicpc.net/problem/15996

N, A = map(int, input().split())
ans = 0
while N:
    N //= A
    ans += N
print(ans)