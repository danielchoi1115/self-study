# 17252 삼삼한 수
# https://www.acmicpc.net/problem/17252

n = N = int(input().strip())
for e in range(21, -1, -1):
    if 3**e <= n: n -= 3**e
print("YES" if n == 0 and N != 0 else "NO")