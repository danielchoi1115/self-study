# [2003] 수들의 합 2
# https://www.acmicpc.net/problem/2003

# 만약 총합이 같으면 ans 하나를 더함
# 만약 총합이 M보다 작으면 가장 오른쪽 값(n[r])을 더하고 r을 앞으로 한 칸 이동
# 만약 총합이 M보다 같거나 크면 가장 왼쪽 값(n[l])을 빼고 l을 앞으로 한 칸 이동
    
N, M = map(int, input().split())
n = list(map(int, input().split()))
ans = t = l = r = 0

while l < N and (t >= M or r < N):
    if t == M:
        ans += 1
    if t < M:
        t += n[r]
        r += 1
    else:
        t -= n[l]
        l += 1
print(ans)
