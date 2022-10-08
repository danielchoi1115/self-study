# Studying well-known code patterns
# Find the number of islands | Set 1 (Using DFS)
# https://www.geeksforgeeks.org/find-number-of-islands/
class Graph:
 
    def __init__(self, row, col, g):
        self.ROW = row
        self.COL = col
        self.graph = g
    
    def isSafe(self, r, c):
        return r >= 0 and r < self.ROW and c >= 0 and c < self.COL and self.graph[r][c]
    
    def travel(self, r, c, visited):
        if self.isSafe(r, c) and not visited[r][c]:
            visited[r][c] = True
        else: 
            return

        trow = [1, -1, 0, 0, 1, -1, 1, -1]
        tcol = [0, 0, 1, -1, 1, -1, -1, 1]
        for t1, t2 in zip(trow, tcol):
            self.travel(r+t1, c+t2, visited)
        
    def countIslands(self):
        visited = [[False for j in range(self.COL)] for i in range(self.ROW)]
        count = 0
        for i in range(self.ROW):
            for j in range(self.COL):
                if not visited[i][j] and self.graph[i][j] == 1:
                    self.travel(i, j, visited)
                    count += 1
        return count
graph = [[1, 1, 0, 0, 0],
        [0, 1, 0, 0, 1],
        [1, 0, 0, 1, 1],
        [0, 0, 1, 0, 0],
        [1, 0, 1, 0, 1]]
 
 
row = len(graph)
col = len(graph[0])
 
g = Graph(row, col, graph)
 
print ("Number of islands is:")
print (g.countIslands())