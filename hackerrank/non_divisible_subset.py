# https://www.hackerrank.com/challenges/non-divisible-subset/problem?isFullScreen=true

def nonDivisibleSubset(k, s):
    length = 0
    remHash = {k: [] for k in range(k)}
    for num in s:
        remainder = num % k
        remHash[remainder].append(num)
    for i in range(k//2 + 1):
        if i == 0:
            if remHash[0]:
                length += 1
        elif i == k-i:
            if remHash[i]:
                length += 1
        else:
            s1 = remHash[i]
            s2 = remHash[k-i]
            length += max(len(s1), len(s2))
    return length


# k = 4
# s = [19, 10, 12, 10, 24, 25, 22]
k = 3
s = [1, 7, 2, 4]

print(nonDivisibleSubset(k, s))
