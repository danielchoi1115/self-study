# [10859] 뒤집어진 소수
# https://www.acmicpc.net/problem/10859

def isPrime(n):
    return (n % 2 != 0) and all(n % i != 0 for i in range(3, round(n**0.5)+1, 2))

def check(n):
    if n == '1': return False
    if n == '2': return True
    invN = ""
    numMap = {
        '0': '0', '2': '2', '5': '5', '8': '8', '1': '1', '6': '9', '9': '6'
    }
    for c in n:
        if c not in numMap:
            return False
        else:
            invN = numMap.get(c) + invN
    return isPrime(int(n)) and isPrime(int(invN))

N = input().strip()
print("yes" if check(N) else "no")

