def solution(arr, num):
    sol = []
    temp = []
    def backtrack(i, temp):
        total = sum(temp)
        if total == num:
            if temp not in sol:
                sol.append(temp[:])
            temp = []
            return 
        elif total > num:
            return
        for j in range(i, len(arr)):
            temp.append(arr[j])
            backtrack(j+1, temp)
            temp.pop()
            
    # for i in range(len(arr)):
    backtrack(0, temp)
    sol.sort()
    return sol
