# 16283 Farm 
# https://www.acmicpc.net/problem/16283
a, b, n, w = map(int,input().split())
ans = [(num_a, n-num_a) for num_a in range(1,n) if num_a * a + (n-num_a) * b == w]
if len(ans) == 0 or len(ans) > 1:
    print(-1)
else:
    print(ans[0][0], ans[0][1])