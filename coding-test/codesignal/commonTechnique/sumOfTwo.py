def solution(a, b, v):
    s = set([v - i for i in b])
    return any(i in s for i in a)
