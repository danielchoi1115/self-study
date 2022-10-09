def solution(n):
    dp = {
        1: 1,
        2: 5
    }
    def dfs(n):
        if n <= 0:
            return 0
        
        if n in dp:
            return dp[n]
        else:
           # set vertically   # set horizontally
            print(n, dp)
            dp[n] = dfs(n-1) + dfs(n-2)*5 + dfs(n-3) + dfs(n-4)
            
            return dp[n]

    dfs(n)
    return dp[n]

