def solution(str, pairs):
    p_set = {}
    hashmap = {}
    strmap = {idx:s for idx, s in enumerate(str)}
    
    for p1, p2 in pairs:
        pt1 = hashmap.get(p1)
        pt2 = hashmap.get(p2)
        if (pt1 and pt2) and (p_set[pt1] != p_set[pt2]):
            p_set[pt1].update(p_set[pt2])
            p_set[pt1].update({p1, p2})
            for t in p_set[pt2]:
                hashmap[t] = pt1
            del(p_set[pt2])
        elif pt1 or pt2:
            pt = pt1 or pt2
            p_set[pt].update({p1, p2})
            hashmap[p1] = hashmap[p2] = pt
        else:
            hashmap[p1] = hashmap[p2] = p1
            p_set[p1] = {p1, p2}
    print(p_set)
    for p in p_set.values():
        chars = sorted([str[i-1] for i in p])
        sorted_p = sorted(p)
        for idx in sorted_p:
            strmap[idx-1] = chars.pop()
    return ''.join(strmap.values())

import random
s= ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(20000))
'E2C6B2E19E4A7777'
pairs=[[random.randint(1,10000), random.randint(10001,20000)] for _ in range(5000)]
print(len(s), len(pairs))
print(solution(s, pairs))