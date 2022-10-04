from typing import List


def solution(crypt, solution):
    hashmap = {sol[0]:sol[1] for sol in solution}
    
    l = ''.join([hashmap[c] for c in crypt[0]])
    r = ''.join([hashmap[c] for c in crypt[1]])
    ans = ''.join([hashmap[c] for c in crypt[2]])
    if ((len(l) != 1 and l[0] == '0') or 
        (len(r) != 1 and r[0] == '0') or 
        (len(ans) != 1 and ans[0] == '0')):
        return False
    
    else:
        if int(ans) == int(l) + int(r):
            return True
    return False
    
    
    

# 200% smarter sol by jlhamilton
def solution(crypt: List[str], solution):
    table = str.maketrans(dict(solution))
    t = tuple(s.translate(table) for s in crypt)
    zeroes = any(s[0] == '0' for s in t if len(s) > 1)
    return not zeroes and int(t[0]) + int(t[1]) == int(t[2])
