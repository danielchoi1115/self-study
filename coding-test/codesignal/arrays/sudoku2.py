def solution(grid):
    def check(r_offset: int, c_offset: int):
        # check sub-grids
        cache: dict = {}
        for i in range(3):
            for j in range(3):
                num = grid[i+r_offset][j+c_offset]
                if num == '.':
                    continue
                elif num not in cache:
                    cache[num] = None
                else:
                    return False
                    
    for i in range(9):
            row = [grid[i][j] for j in range(9) if grid[i][j] != '.']
            col = [grid[j][i] for j in range(9) if grid[j][i] != '.']
            # check rows and cols
            if len(row) != len(set(row)) or len(col) != len(set(col)):
                return False
    
    for i in range(3):
        for j in range(3):
            if check(j*3, i*3) == False:
                return False
    
    return True
