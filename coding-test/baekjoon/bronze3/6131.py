# https://www.acmicpc.net/problem/6131

import sys
N = int(sys.stdin.readline().strip())

powerList = [pow(i, 2) for i in range(1,501)]
sub = {p-N for p in powerList if p > N}

print(sum(p in sub for p in powerList))