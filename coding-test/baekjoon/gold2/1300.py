N = int(input())
K = int(input())
def cal(N, K):
    if K in (1, N**2): 
        return K
    weight = 1
    step = 1
    D = 1
    total = 1
    while True:
        if D == N:
            step = -1
        weight += step
        if total + weight >= K:
            D += 1
            break
        total += weight
        D += 1

    x0, y0 = min(N, D), max(1, D+1-N)
    mult = (K-total-1)//2
    return (x0-mult)*(y0+mult)

print(cal(N, K))
