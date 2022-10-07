def solution(nums, k):
    hashtable = {}
    for idx, n in enumerate(nums):
        hashtable.setdefault(n, []).append(idx)
    
    for num, indexes in hashtable.items():
        if len(indexes) > 1:
            for i in range(len(indexes)-1):
                if indexes[i+1] - indexes[i] <= k:
                    return True
    return False

# one loop solution by k_lee
def solution(nums, k):
    dic = {}
    for i, x in enumerate(nums):
        if x in dic and i - dic[x] <= k:
            return True
        dic[x] = i
    return False