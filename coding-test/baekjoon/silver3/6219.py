# [6219] 소수의 자격
# https://www.acmicpc.net/problem/6219

def primes_under(n):
    n, c = n + 6 - n % 6, 2 - (n % 6 > 1)
    sieve = [True] * (n // 3)
    for i in range(1, int(n**0.5) // 3 + 1):
        if sieve[i]:
            d, s, j = (k := 1 | 3 * i + 1) * 2, k * k, k * (k + 4 - 2 * (i & 1))
            sieve[s // 3 :: d] = [False] * ((n // 6 - s // 6 - 1) // k + 1)
            sieve[j // 3 :: d] = [False] * ((n // 6 - j // 6 - 1) // k + 1)
    return [2, 3] + [1 | 3 * i + 1 for i in range(1, n // 3 - c) if sieve[i]]

A, B, D = map(int, input().strip().split())


primes = primes_under(B)
ans = 0
for p in primes:
    if p < A: continue
    if str(D) in str(p):
        ans += 1
print(ans)


