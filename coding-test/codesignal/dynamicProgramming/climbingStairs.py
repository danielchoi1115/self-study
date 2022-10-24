def solution(n):
    dp = [0]*n
    def fibo(n):
        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            if dp[n-1] != 0:
                return dp[n-1]
            else:
                dp[n-1] = fibo(n-1) + fibo(n-2)
                return dp[n-1]
        
    return fibo(n)

# 200% smarter, shorter, faster, solution. Also uses less space 
# by maksym_k1
def solution(n):
    a, b = 1, 0
    for _ in range(n):
        a, b = a + b, a
    return a

print(26 in range(10, 26))