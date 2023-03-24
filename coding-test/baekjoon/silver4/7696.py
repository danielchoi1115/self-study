# [7696] 반복하지 않는 수
# https://www.acmicpc.net/problem/7696
from time import time

# nums = []
# while True:
#     num = int(input().strip())
#     if not num: break
#     nums.append(num)



# def checkHasDup(n):
#     d = set()
#     while n:
#         rem = n % 10
#         if rem in d: 
#             return True
#         d.add(rem)
#         n //= 10
#     return False

# def checkHasDup2(n):
#     d = str(n)
#     return len(set(d)) != len(d) 

# nums = []
# while True:
#     num = int(input().strip())
#     if not num: break
#     nums.append(num)
# n = nth = 1
# numSet = set(nums)
# max_num = max(nums)

# while n <= max_num:
#     if not checkHasDup2(nth): 
#         if n in numSet:
#             print(nth)
#         n += 1
#     nth += 1

import sys
input = sys.stdin.readline
idx = count = 0
answer = [""]
I = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
while count<1000001:
    for i in I:
        if idx == 0 and i == "0":
            continue
        if i not in answer[idx]:
            answer.append(answer[idx]+i)
            count+=1
    idx += 1

while True:
    N = int(input())
    if N ==0 :
        break
    print(int(answer[N]))

