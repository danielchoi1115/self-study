# [2004] 조합 0의 개수
# https://www.acmicpc.net/problem/2004

def get_pow(n, a):
    ans = 0
    while n:
        n //= a
        ans += n
    return ans

N, M = map(int, input().split())
n2 = get_pow(N, 2)
n5 = get_pow(N, 5)
m2 = get_pow(M, 2)
m5 = get_pow(M, 5)
nm2 = get_pow((N-M), 2)
nm5 = get_pow((N-M), 5)
print(min(n2-m2-nm2, n5-m5-nm5))
