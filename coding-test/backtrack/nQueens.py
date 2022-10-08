def solution(n):
    sol = []
    queens = []
    def isSafe(row, col):
        if len(queens) < row or col in queens:
            return False
        for r, c in enumerate(queens):
            if c == -1:
                continue
            if (abs(r-row) == abs(c-col)):
                return False
        return True
    
    def backtrack(n, row, queens):
        if n == len(queens):
            new_sol = [i+1 for i in queens]
            if new_sol not in sol:
                sol.append(new_sol)
            queens = []
            return
        
        for i in range(n):
            if isSafe(row, i):
                queens.append(i)
                backtrack(n, row+1, queens)
                queens.pop()
                

    backtrack(n, 0, queens)
    
    sol.sort()
    return sol

s = solution(8)
print(s)
print(len(s))
