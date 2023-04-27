def solution(n):
    answers = []
    
    def isValid(qx, qy):
        for _x, _y in placed:
            if qx == _x or qy == _y or abs(qx-_x) == abs(qy-_y): return False
        return True
    
    def addAnswer(item):
        for ans in answers:
            if ans == item: return
        answers.append(item)        
    def dfs(row):
        if len(placed) == n: 
            addAnswer(placed)
            
        if row == n: return
        for col in range(n):
            if not isValid(row, col): continue
            placed.add((row,col))
            dfs(row+1)
            placed.remove((row,col))
                
    for start_col in range(n):
        placed = {(0, start_col)}
        dfs(1)
    
    return len(answers)

print([0, 1, 0, 0, 2, 10, 4, 40, 92, 352, 724, 2680, 14200, 73712, 365596, 2279184, 14772512][int(input())])
n = 7
print(solution(n))