# Wasn't meaningful because I read the solution from YouTube...

def solution(s) -> int:
    l = len(s)
    dp = {l: 1}
    for i in range(l-1, -1, -1):
        if s[i] == '0':
            dp[i] = 0
        else:
            dp[i] = dp[i + 1]
        if (i + 1 < l and 
            (s[i] == '1' or 
                s[i] == '2' and s[i+1] in '0123456')
        ):
            dp[i] += dp[i + 2]
        
    return dp[0] % (pow(10,9)+7)


# smarter solution using O(1) extra space
# by k_lee
def solution(msg):
    a, b = 1, 0
    M = 10 ** 9 + 7
    for i in range(len(msg)-1, -1, -1):
        if msg[i] == "0":
            a, b = 0, a
        else:
            a, b = (a + (i+2 <= len(msg) and msg[i:i+2] <= "26") * b) % M, a
    return a
