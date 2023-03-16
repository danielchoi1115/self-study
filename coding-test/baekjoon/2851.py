# https://www.acmicpc.net/problem/2851
import sys
N = [int(sys.stdin.readline()) for _ in range(10)] 

_sum = 0
_prevSum = 0
threshold = 100

for num in N:
    _sum += num
    if _sum > threshold:
        _prevSum = _sum - num
        break

diff1 = abs(threshold-_sum)
diff2 = abs(threshold-_prevSum)

if diff1 == diff2:
    print(max(_sum, _prevSum))
elif diff1 < diff2:
    print(_sum)
else:
    print(_prevSum)
