# 1816 암호 키
# https://www.acmicpc.net/problem/1816

import sys
N = int(sys.stdin.readline())
s = [int(sys.stdin.readline().strip()) for _ in range(N)]

# refer https://www.acmicpc.net/source/54267434
def primes_under(n):
    n, c = n + 6 - n % 6, 2 - (n % 6 > 1)
    sieve = [True] * (n // 3)
    for i in range(1, int(n**0.5) // 3 + 1):
        if sieve[i]:
            d, s, j = (k := 1 | 3 * i + 1) * 2, k * k, k * (k + 4 - 2 * (i & 1))
            sieve[s // 3 :: d] = [False] * ((n // 6 - s // 6 - 1) // k + 1)
            sieve[j // 3 :: d] = [False] * ((n // 6 - j // 6 - 1) // k + 1)
    return [2, 3] + [1 | 3 * i + 1 for i in range(1, n // 3 - c) if sieve[i]]

primes = primes_under(1000000)
for num in s:
    for i in primes:
        if num % i == 0:
            print("NO")
            break
    else:
        print("YES")