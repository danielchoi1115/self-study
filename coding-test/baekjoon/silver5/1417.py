# [1417] 국회의원 선거
# https://www.acmicpc.net/problem/1417

import heapq

import sys
N = int(sys.stdin.readline())
D = int(sys.stdin.readline())
heap = [int(sys.stdin.readline())*-1 for _ in range(N-1)]
ans = 0
    
heapq.heapify(heap)
while heap and heap[0]*-1 >= D+ans:
    heapq.heappush(heap, heapq.heappop(heap)+1)
    ans+=1
print(ans)
