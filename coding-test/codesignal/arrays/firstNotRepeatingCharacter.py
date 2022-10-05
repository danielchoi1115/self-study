def solution(s):
    cache: dict = {}
    
    candidate: dict = {}
    
    for c in s:
        if c not in cache:
            cache[c] = True
            candidate[c] = True
        else:
            if c in candidate:
                del(candidate[c])
    
    if not candidate:
        return "_"
    else:
        return list(candidate)[0]
    
    
# 200% smarter solution by kirito4499
def solution(s):
    for c in s:
        if s.index(c) == s.rindex(c):
            return c
    return '_'