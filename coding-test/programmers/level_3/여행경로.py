from collections import deque
def solution(tickets):
    
    def make_ticketmap():
        M = {}
        for from_, to in tickets:
            if from_ not in M:
                M[from_] = {to: 1}
            else:
                if to in M[from_]: M[from_][to] += 1
                else: M[from_][to] = 1
        return M
    
    def dfs(from_):
        visited.append(from_)
        if used_ticket[0] == len(tickets):
            answers.append(list(visited))
        if from_ in tmap:
            for to in tmap[from_]:
                if tmap[from_][to] == 0: continue
                tmap[from_][to] -= 1
                used_ticket[0] += 1
                dfs(to)
                tmap[from_][to] += 1
                used_ticket[0] -= 1
        visited.pop()
    answers = []
    used_ticket = [0]
    tmap = make_ticketmap()
    visited = deque()
    dfs("ICN")
    return min(answers)