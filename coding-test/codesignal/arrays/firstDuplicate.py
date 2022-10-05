def solution(a):
    cache: dict = {}
    
    for i in a:
        if i not in cache:
            cache[i] = True
        else:
            return i
    else:
        return -1