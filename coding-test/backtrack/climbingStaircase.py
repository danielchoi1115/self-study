def solution(n, k):
    if not n:
        return [[]]
    res = []
    def jump(path, total, step):
        if total - step == 0:
            newlist = path + [step]
            res.append(newlist)
        elif total - step > 0:
            for i in range(1, k+1):
                jump(path + [step], total - step, i)
            
    for i in range(1, k+1):
        jump([], n, i)
    return res


# Smarter solution by k_lee
def solution(n, k):
    if n < 0: return []
    if n == 0: return [[]]
    ans = []
    for i in range(1, k+1):
        for seq in solution(n-i, k):
            ans.append([i] + seq)
    return ans
