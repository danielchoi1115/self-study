def solution(nums):
    sol = []
    if len(nums) < 2:
        return [str(n) for n in nums]
    start = end = nums[0]
    def getRange(start, end):
        if start == end:
            return str(start)
        else:
            return f"{start}->{end}"
    
    for i in range(len(nums) - 1):
        if nums[i+1] - nums[i] > 1:
            sol.append(getRange(start, end))
            start = end = nums[i+1]
        else:
            end = nums[i+1]
    sol.append(getRange(start, end))
    return sol 
        
# Shorter solution
# by freemanlex
def solution(nums):
    ranges = []
    while nums:
        start = end = nums.pop(0)
        while nums and nums[0] - end == 1:
            end = nums.pop(0)
        ranges.append(str(start) + ('', '->' + str(end))[start != end])
    return ranges