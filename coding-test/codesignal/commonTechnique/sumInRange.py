def solution(nums, queries):
    s = 0
    for q in queries:
        s += sum(nums[q[0]:q[1]+1])
    return s % (10**9 + 7)
