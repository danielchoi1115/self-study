
def solution(dishes):
    hashtable = {}
    for d in dishes:
        dish = d[0]
        ingredients = d[1:]
        
        for i in ingredients:
            if i in hashtable:
                hashtable[i].append(dish)
            else:
                hashtable[i] = [dish]
                
    return [[k]+sorted(hashtable[k]) 
            for k in sorted(hashtable.keys())
            if len(hashtable[k]) > 1]



# Smarter way using setdefault
# by k_lee

def solution(dishes):
    groups = {}
    for d, *v in dishes:
        for x in v:
            groups.setdefault(x, []).append(d)
    ans = []
    for x in sorted(groups):
        if len(groups[x]) >= 2:
            ans.append([x] + sorted(groups[x]))
    return ans
