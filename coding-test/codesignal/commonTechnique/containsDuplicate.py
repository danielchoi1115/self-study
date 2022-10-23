def solution(a):
    return len(a) != len(list(set(a)))



# don't even need list-ifying

def solution(a):
    return len(a) != len(set(a))