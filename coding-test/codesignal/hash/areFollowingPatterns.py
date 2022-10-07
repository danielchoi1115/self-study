def solution(strings, patterns):
    stringtable = {}
    patterntable = {}
    for s, p in zip(strings, patterns):
        if s not in stringtable and p not in patterntable:
            patterntable[p] = s
            stringtable[s] = p
        
        if patterntable.get(p) != s or stringtable.get(s) != p:
            return False
    else:
        return True


# 200% smarter 1 line solution
# by kottenator
def solution(strings, patterns):
    return len(set(strings)) == len(set(patterns)) == len(set(zip(strings, patterns)))

strings=["aaa", 
        "aab", 
        "aaa"]
patterns=["aaa", 
        "aaa", 
        "aaa"]

solution(strings, patterns)