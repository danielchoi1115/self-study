# 2017 연세대학교 프로그래밍 경시대회 
# https://www.acmicpc.net/problem/14568
N = int(input())
ans = 0
for t in range(2,N-1, 2):
    ans += (N-t-2)//2
print(ans)
